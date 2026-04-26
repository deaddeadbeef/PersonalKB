import glob, os, re, json, subprocess, time, shutil

wiki_dir = r"D:\Vaults\PersonalKB\Japanese"
audio_dir = r"D:\Vaults\PersonalKB\Japanese\_audio"

jp_pattern = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]')
audio_embed = re.compile(r'\!\[\[.*?\.mp3\]\]')

# ============================================
# PHASE 1: Fix _audio/ prefix in all embeds
# ============================================
print("=== PHASE 1: Fixing _audio/ prefix ===")
prefix_fixes = 0
for filepath in glob.glob(os.path.join(wiki_dir, "**", "*.md"), recursive=True):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    if "![[_audio/" in content:
        new_content = content.replace("![[_audio/", "![[")
        count = content.count("![[_audio/")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        prefix_fixes += count
        print(f"  Fixed {count} prefix(es) in {os.path.basename(filepath)}")
print(f"Total prefix fixes: {prefix_fixes}")

# ============================================
# PHASE 2: Fix blank lines within tables
# ============================================
print("\n=== PHASE 2: Fixing table blank lines ===")
table_fixes = 0
for filepath in glob.glob(os.path.join(wiki_dir, "**", "*.md"), recursive=True):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split('\n')
    new_lines = []
    i = 0
    fixed_in_file = 0

    while i < len(lines):
        line = lines[i]
        new_lines.append(line)

        # If current line is a table row
        if line.strip().startswith('|') and line.strip().endswith('|'):
            # Look ahead: skip blank lines if followed by another table row
            # BUT only if the next table row is NOT a header row (|---|)
            j = i + 1
            blank_count = 0
            while j < len(lines) and lines[j].strip() == '':
                blank_count += 1
                j += 1

            # If blank lines found and next non-blank is a table row (not a new header)
            if blank_count > 0 and j < len(lines):
                next_line = lines[j].strip()
                if next_line.startswith('|') and next_line.endswith('|'):
                    # Check if this is a new table header by looking at line after
                    is_new_header = False
                    if j + 1 < len(lines):
                        following = lines[j + 1].strip()
                        if re.match(r'^\|[\s\-:|]+\|$', following):
                            is_new_header = True

                    if not is_new_header:
                        # Skip blank lines â€” they're within a table
                        fixed_in_file += blank_count
                        i = j
                        continue
            i += 1
        else:
            i += 1

    if fixed_in_file > 0:
        new_content = '\n'.join(new_lines)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        table_fixes += fixed_in_file
        print(f"  Removed {fixed_in_file} blank line(s) in {os.path.basename(filepath)}")

print(f"Total table blank lines removed: {table_fixes}")

# ============================================
# PHASE 3: Find table rows missing audio
# ============================================
print("\n=== PHASE 3: Finding table rows with Japanese but no audio ===")
missing = []

for filepath in glob.glob(os.path.join(wiki_dir, "**", "*.md"), recursive=True):
    if '_audio' in filepath or '_raw' in filepath or '_chunks' in filepath:
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped.startswith('|') or not stripped.endswith('|'):
            continue
        # Skip separator rows
        if re.match(r'^\|[\s\-:|]+\|$', stripped):
            continue
        # Skip header rows (check if next line is separator)
        if i + 1 < len(lines) and re.match(r'^\|[\s\-:|]+\|$', lines[i + 1].strip()):
            continue

        has_jp = bool(jp_pattern.search(stripped))
        has_audio = bool(audio_embed.search(stripped))

        if has_jp and not has_audio:
            # Extract Japanese text from first column
            cols = stripped.split('|')
            jp_text = ''
            for col in cols[1:]:  # skip first empty
                if jp_pattern.search(col):
                    jp_text = col.strip()
                    break

            missing.append({
                'file': filepath,
                'line_num': i,
                'japanese': jp_text,
                'basename': os.path.basename(filepath)
            })

print(f"Found {len(missing)} rows with Japanese text but no audio:")
for m in missing:
    print(f"  {m['basename']}:{m['line_num']+1} â€” {m['japanese']}")

# ============================================
# PHASE 4: Generate TTS for missing entries
# ============================================
if missing:
    print(f"\n=== PHASE 4: Generating TTS for {len(missing)} entries ===")

    # Create manifest
    manifest = []
    for idx, m in enumerate(missing, 1):
        jp = m['japanese']
        # Create safe romaji filename from Japanese
        safe = jp.replace(' ', '-').replace('ã€€', '-')
        # Remove non-ASCII for filename
        romaji = re.sub(r'[^\x00-\x7F]', '', safe).strip('-') or f"phrase"
        filename = f"gap-{idx:03d}-{romaji[:30]}.mp3" if romaji else f"gap-{idx:03d}-phrase.mp3"
        # Clean up filename
        filename = re.sub(r'[<>:"/\\|?*]', '', filename)
        filename = re.sub(r'-+', '-', filename)
        manifest.append({
            "filename": filename,
            "text": jp
        })
        m['audio_filename'] = filename

    manifest_path = os.path.join(audio_dir, "gap_manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"Manifest written: {manifest_path} ({len(manifest)} entries)")

    # Get Azure key
    az_exe = shutil.which("az") or shutil.which("az.cmd")
    key = ""
    if az_exe:
        result = subprocess.run(
            [az_exe, "cognitiveservices", "account", "keys", "list",
             "--name", "tts-tester", "--resource-group", "tts-resources",
             "--query", "key1", "-o", "tsv"],
            capture_output=True, text=True
        )
        key = result.stdout.strip()
    else:
        print("ERROR: Azure CLI not found")

    if key:
        # Run TTS generation
        gen_result = subprocess.run(
            ["python", os.path.join(audio_dir, "generate_tts.py"), key, "japaneast", manifest_path],
            capture_output=True, text=True, cwd=audio_dir
        )
        print(gen_result.stdout)
        if gen_result.stderr:
            print(f"TTS errors: {gen_result.stderr}")
    else:
        print("ERROR: Could not get Azure key")

    # ============================================
    # PHASE 5: Embed audio into table rows
    # ============================================
    print(f"\n=== PHASE 5: Embedding audio into {len(missing)} rows ===")

    # Group by file
    by_file = {}
    for m in missing:
        if m['file'] not in by_file:
            by_file[m['file']] = []
        by_file[m['file']].append(m)

    for filepath, entries in by_file.items():
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for entry in entries:
            line_num = entry['line_num']
            audio_fn = entry['audio_filename']
            line = lines[line_num]

            # Check if audio file was actually created
            if not os.path.exists(os.path.join(audio_dir, audio_fn)):
                print(f"  SKIP {audio_fn} â€” file not generated")
                continue

            cols = line.rstrip('\n').rstrip('|').split('|')

            # If there's an Audio column (3+ cols), fill the last one
            if len(cols) >= 3:
                # Check if last col is empty or whitespace
                if cols[-1].strip() == '':
                    cols[-1] = f" ![[{audio_fn}]] "
                else:
                    cols.append(f" ![[{audio_fn}]] ")
                lines[line_num] = '|'.join(cols) + '|\n'
            else:
                # No Audio column â€” append one
                line_clean = lines[line_num].rstrip('\n').rstrip('|')
                lines[line_num] = f"{line_clean}| ![[{audio_fn}]] |\n"

            print(f"  Embedded {audio_fn} in {os.path.basename(filepath)}:{line_num+1}")

        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(lines)

# ============================================
# PHASE 6: Normalize table headers after audio embeds
# ============================================
print("\n=== PHASE 6: Normalizing table audio headers ===")
header_fixes = 0
for filepath in glob.glob(os.path.join(wiki_dir, "**", "*.md"), recursive=True):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    fixed_in_file = 0
    i = 0
    while i < len(lines) - 2:
        header = lines[i].strip()
        separator = lines[i + 1].strip()
        if header.startswith('|') and header.endswith('|') and re.match(r'^\|[\s\-:|]+\|$', separator):
            header_cells = [cell.strip() for cell in header[1:-1].split('|')]
            sep_cells = [cell.strip() for cell in separator[1:-1].split('|')]
            max_row_cols = len(header_cells)
            has_audio_row = False
            j = i + 2
            while j < len(lines):
                row = lines[j].strip()
                if not (row.startswith('|') and row.endswith('|')) or re.match(r'^\|[\s\-:|]+\|$', row):
                    break
                max_row_cols = max(max_row_cols, len(row[1:-1].split('|')))
                if '.mp3]]' in row:
                    has_audio_row = True
                j += 1

            if has_audio_row:
                changed = False
                if header_cells and header_cells[-1] == 'Audio':
                    for idx in range(len(header_cells) - 1):
                        cleaned = re.sub(r'\s+Audio$', '', header_cells[idx]).strip()
                        if cleaned != header_cells[idx]:
                            header_cells[idx] = cleaned
                            changed = True
                if sep_cells and sep_cells[-1] == '---':
                    for idx in range(len(sep_cells) - 1):
                        cleaned = re.sub(r'\s+---$', '', sep_cells[idx]).strip()
                        if cleaned != sep_cells[idx]:
                            sep_cells[idx] = cleaned
                            changed = True
                while len(sep_cells) < len(header_cells):
                    sep_cells.append('---')
                    changed = True
                while len(header_cells) < max_row_cols:
                    header_cells.append('Audio')
                    changed = True
                while len(sep_cells) < max_row_cols:
                    sep_cells.append('---')
                    changed = True
                if changed:
                    lines[i] = '| ' + ' | '.join(header_cells) + ' |\n'
                    lines[i + 1] = '| ' + ' | '.join(sep_cells) + ' |\n'
                    fixed_in_file += 1
            i = j
        else:
            i += 1

    if fixed_in_file > 0:
        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(lines)
        header_fixes += fixed_in_file
        print(f"  Normalized {fixed_in_file} table header(s) in {os.path.basename(filepath)}")

print(f"Total table headers normalized: {header_fixes}")

print("\n=== DONE ===")
