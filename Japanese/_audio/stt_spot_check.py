"""
STT Spot-Check: Verify Japanese TTS audio clips via Azure Speech-to-Text.
Samples 100 clips across 10 categories and compares transcriptions
against expected content derived from filenames.
"""

import os
import re
import random
import subprocess
import tempfile
import time
from pathlib import Path
from datetime import datetime

import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment

# ── Configuration ──────────────────────────────────────────────────────────
AUDIO_DIR = Path(r"D:\Vaults\PersonalKB\Japanese\_audio")
REPORT_PATH = AUDIO_DIR / "stt-spot-check-report.txt"
REGION = "japaneast"

# ── Romaji to Kana lookup (ordered long-to-short) ────────────────────────
ROMAJI_TO_HIRAGANA = {
    "ssha": "\u3063\u3057\u3083", "sshi": "\u3063\u3057",
    "sshu": "\u3063\u3057\u3085", "ssho": "\u3063\u3057\u3087",
    "ccha": "\u3063\u3061\u3083", "cchi": "\u3063\u3061",
    "cchu": "\u3063\u3061\u3085", "ccho": "\u3063\u3061\u3087",
    "ttsu": "\u3063\u3064",
    "kka": "\u3063\u304b", "kki": "\u3063\u304d", "kku": "\u3063\u304f",
    "kke": "\u3063\u3051", "kko": "\u3063\u3053",
    "ssa": "\u3063\u3055", "ssi": "\u3063\u3057", "ssu": "\u3063\u3059",
    "sse": "\u3063\u305b", "sso": "\u3063\u305d",
    "tta": "\u3063\u305f", "tti": "\u3063\u3061", "ttu": "\u3063\u3064",
    "tte": "\u3063\u3066", "tto": "\u3063\u3068",
    "ppa": "\u3063\u3071", "ppi": "\u3063\u3074", "ppu": "\u3063\u3077",
    "ppe": "\u3063\u307a", "ppo": "\u3063\u307d",
    "sha": "\u3057\u3083", "shi": "\u3057",
    "shu": "\u3057\u3085", "sho": "\u3057\u3087",
    "chi": "\u3061", "cha": "\u3061\u3083",
    "chu": "\u3061\u3085", "cho": "\u3061\u3087",
    "tsu": "\u3064",
    "nya": "\u306b\u3083", "nyu": "\u306b\u3085", "nyo": "\u306b\u3087",
    "hya": "\u3072\u3083", "hyu": "\u3072\u3085", "hyo": "\u3072\u3087",
    "mya": "\u307f\u3083", "myu": "\u307f\u3085", "myo": "\u307f\u3087",
    "rya": "\u308a\u3083", "ryu": "\u308a\u3085", "ryo": "\u308a\u3087",
    "gya": "\u304e\u3083", "gyu": "\u304e\u3085", "gyo": "\u304e\u3087",
    "bya": "\u3073\u3083", "byu": "\u3073\u3085", "byo": "\u3073\u3087",
    "pya": "\u3074\u3083", "pyu": "\u3074\u3085", "pyo": "\u3074\u3087",
    "kya": "\u304d\u3083", "kyu": "\u304d\u3085", "kyo": "\u304d\u3087",
    "jya": "\u3058\u3083", "jyu": "\u3058\u3085", "jyo": "\u3058\u3087",
    "ja": "\u3058\u3083", "ju": "\u3058\u3085", "jo": "\u3058\u3087",
    "fu": "\u3075",
    "ka": "\u304b", "ki": "\u304d", "ku": "\u304f", "ke": "\u3051", "ko": "\u3053",
    "sa": "\u3055", "su": "\u3059", "se": "\u305b", "so": "\u305d",
    "ta": "\u305f", "te": "\u3066", "to": "\u3068",
    "na": "\u306a", "ni": "\u306b", "nu": "\u306c", "ne": "\u306d", "no": "\u306e",
    "ha": "\u306f", "hi": "\u3072", "he": "\u3078", "ho": "\u307b",
    "ma": "\u307e", "mi": "\u307f", "mu": "\u3080", "me": "\u3081", "mo": "\u3082",
    "ya": "\u3084", "yu": "\u3086", "yo": "\u3088",
    "ra": "\u3089", "ri": "\u308a", "ru": "\u308b", "re": "\u308c", "ro": "\u308d",
    "wa": "\u308f", "wi": "\u3090", "we": "\u3091", "wo": "\u3092",
    "ga": "\u304c", "gi": "\u304e", "gu": "\u3050", "ge": "\u3052", "go": "\u3054",
    "za": "\u3056", "ji": "\u3058", "zu": "\u305a", "ze": "\u305c", "zo": "\u305e",
    "da": "\u3060", "di": "\u3062", "du": "\u3065", "de": "\u3067", "do": "\u3069",
    "ba": "\u3070", "bi": "\u3073", "bu": "\u3076", "be": "\u3079", "bo": "\u307c",
    "pa": "\u3071", "pi": "\u3074", "pu": "\u3077", "pe": "\u307a", "po": "\u307d",
    "si": "\u3057", "ti": "\u3061", "tu": "\u3064", "hu": "\u3075",
    "nn": "\u3093",
    "a": "\u3042", "i": "\u3044", "u": "\u3046", "e": "\u3048", "o": "\u304a",
    "n": "\u3093",
}


def _hira_to_kata(s):
    """Convert hiragana string to katakana."""
    return "".join(chr(ord(c) + 0x60) if "\u3041" <= c <= "\u3096" else c for c in s)


# ── Known word overrides (romaji -> acceptable transcriptions) ───────────
WORD_OVERRIDES = {
    # core100
    "watashi": ["\u308f\u305f\u3057", "\u79c1"],
    "anata": ["\u3042\u306a\u305f"],
    "kore": ["\u3053\u308c"], "sore": ["\u305d\u308c"], "are": ["\u3042\u308c"],
    "koko": ["\u3053\u3053"], "soko": ["\u305d\u3053"],
    "nani": ["\u306a\u306b", "\u4f55"], "dare": ["\u3060\u308c", "\u8ab0"],
    "doko": ["\u3069\u3053"], "itsu": ["\u3044\u3064"],
    "naze": ["\u306a\u305c"], "hai": ["\u306f\u3044"],
    "iie": ["\u3044\u3044\u3048"],
    "onegaishimasu": ["\u304a\u9858\u3044\u3057\u307e\u3059", "\u304a\u306d\u304c\u3044\u3057\u307e\u3059"],
    "arigatou": ["\u3042\u308a\u304c\u3068\u3046"],
    "gomen nasai": ["\u3054\u3081\u3093\u306a\u3055\u3044"],
    "gomennasai": ["\u3054\u3081\u3093\u306a\u3055\u3044"],
    "daijoubu": ["\u5927\u4e08\u592b", "\u3060\u3044\u3058\u3087\u3046\u3076"],
    "wakarimashita": ["\u308f\u304b\u308a\u307e\u3057\u305f", "\u5206\u304b\u308a\u307e\u3057\u305f"],
    "taberu": ["\u98df\u3079\u308b", "\u305f\u3079\u308b"],
    "nomu": ["\u98f2\u3080", "\u306e\u3080"],
    "iku": ["\u884c\u304f", "\u3044\u304f"],
    "kuru": ["\u6765\u308b", "\u304f\u308b"],
    "miru": ["\u898b\u308b", "\u307f\u308b"],
    "kiku": ["\u805e\u304f", "\u304d\u304f", "\u8074\u304f"],
    "hanasu": ["\u8a71\u3059", "\u306f\u306a\u3059"],
    "yomu": ["\u8aad\u3080", "\u3088\u3080"],
    "kaku": ["\u66f8\u304f", "\u304b\u304f"],
    "kau": ["\u8cb7\u3046", "\u304b\u3046"],
    "suru": ["\u3059\u308b"],
    "neru": ["\u5bdd\u308b", "\u306d\u308b"],
    "okiru": ["\u8d77\u304d\u308b", "\u304a\u304d\u308b"],
    "aruku": ["\u6b69\u304f", "\u3042\u308b\u304f"],
    "hashiru": ["\u8d70\u308b", "\u306f\u3057\u308b"],
    "tobu": ["\u98db\u3076", "\u3068\u3076"],
    "oyogu": ["\u6cf3\u3050", "\u304a\u3088\u3050"],
    "matsu": ["\u5f85\u3064", "\u307e\u3064"],
    "iru": ["\u3044\u308b"], "aru": ["\u3042\u308b"],
    "hito": ["\u4eba", "\u3072\u3068"],
    "kodomo": ["\u5b50\u3069\u3082", "\u3053\u3069\u3082", "\u5b50\u4f9b"],
    "tomodachi": ["\u53cb\u9054", "\u3068\u3082\u3060\u3061"],
    "sensei": ["\u5148\u751f", "\u305b\u3093\u305b\u3044"],
    "ie": ["\u5bb6", "\u3044\u3048", "\u4f9d\u6c5f"],
    "gakkou": ["\u5b66\u6821", "\u304c\u3063\u3053\u3046"],
    "eki": ["\u99c5", "\u3048\u304d"],
    "mizu": ["\u6c34", "\u307f\u305a"],
    "tabemono": ["\u98df\u3079\u7269", "\u305f\u3079\u3082\u306e"],
    "nomimono": ["\u98f2\u307f\u7269", "\u306e\u307f\u3082\u306e"],
    "hon": ["\u672c", "\u307b\u3093"],
    "denwa": ["\u96fb\u8a71", "\u3067\u3093\u308f"],
    "kuruma": ["\u8eca", "\u304f\u308b\u307e"],
    "densha": ["\u96fb\u8eca", "\u3067\u3093\u3057\u3083"],
    "ooi": ["\u591a\u3044", "\u304a\u304a\u3044"],
    "sukunai": ["\u5c11\u306a\u3044", "\u3059\u304f\u306a\u3044"],
    "takai": ["\u9ad8\u3044", "\u305f\u304b\u3044"],
    "yasui": ["\u5b89\u3044", "\u3084\u3059\u3044"],
    "hayai": ["\u65e9\u3044", "\u901f\u3044", "\u306f\u3084\u3044"],
    "osoi": ["\u9045\u3044", "\u304a\u305d\u3044"],
    "nagai": ["\u9577\u3044", "\u306a\u304c\u3044"],
    "mijikai": ["\u77ed\u3044", "\u307f\u3058\u304b\u3044"],
    "ima": ["\u4eca", "\u3044\u307e"],
    "kyou": ["\u4eca\u65e5", "\u304d\u3087\u3046", "\u5f37", "\u4eac"],
    "ashita": ["\u660e\u65e5", "\u3042\u3057\u305f"],
    "kinou": ["\u6628\u65e5", "\u304d\u306e\u3046"],
    "asa": ["\u671d", "\u3042\u3055"],
    "yoru": ["\u591c", "\u3088\u308b"],
    "mae": ["\u524d", "\u307e\u3048"],
    "ushiro": ["\u5f8c\u308d", "\u3046\u3057\u308d"],
    "ue": ["\u4e0a", "\u3046\u3048"],
    "shita": ["\u4e0b", "\u3057\u305f"],
    "naka": ["\u4e2d", "\u306a\u304b"],
    "soto": ["\u5916", "\u305d\u3068"],

    # Additional core100 words
    "nihongo": ["\u65e5\u672c\u8a9e", "\u306b\u307b\u3093\u3054"],
    "gakusei": ["\u5b66\u751f", "\u304c\u304f\u305b\u3044"],
    "ookii": ["\u5927\u304d\u3044", "\u304a\u304a\u304d\u3044"],

    # greetings
    "ohayou-gozaimasu": ["\u304a\u306f\u3088\u3046\u3054\u3056\u3044\u307e\u3059"],
    "ohayougozaimasu": ["\u304a\u306f\u3088\u3046\u3054\u3056\u3044\u307e\u3059"],
    "konnichiwa": ["\u3053\u3093\u306b\u3061\u306f"],
    "konbanwa": ["\u3053\u3093\u3070\u3093\u306f"],
    "oyasuminasai": ["\u304a\u3084\u3059\u307f\u306a\u3055\u3044"],
    "hajimemashite": ["\u306f\u3058\u3081\u307e\u3057\u3066", "\u521d\u3081\u307e\u3057\u3066"],
    "yoroshiku-onegaishimasu": ["\u3088\u308d\u3057\u304f\u304a\u9858\u3044\u3057\u307e\u3059"],
    "yoroshikuonegaishimasu": ["\u3088\u308d\u3057\u304f\u304a\u9858\u3044\u3057\u307e\u3059"],
    "ohisashiburi-desu": ["\u304a\u4e45\u3057\u3076\u308a\u3067\u3059", "\u304a\u3072\u3055\u3057\u3076\u308a\u3067\u3059"],
    "sayounara": ["\u3055\u3088\u3046\u306a\u3089"],
    "matane": ["\u307e\u305f\u306d"],
    "osaki-ni-shitsurei-shimasu": ["\u304a\u5148\u306b\u5931\u793c\u3057\u307e\u3059"],
    "ittekimasu": ["\u884c\u3063\u3066\u304d\u307e\u3059", "\u3044\u3063\u3066\u304d\u307e\u3059"],
    "itterasshai": ["\u3044\u3063\u3066\u3089\u3063\u3057\u3083\u3044"],
    "tadaima": ["\u305f\u3060\u3044\u307e"],
    "okaerinasai": ["\u304a\u304b\u3048\u308a\u306a\u3055\u3044"],

    # daily
    "irasshaimase": ["\u3044\u3089\u3063\u3057\u3083\u3044\u307e\u305b"],
    "kore-wo-kudasai": ["\u3053\u308c\u3092\u304f\u3060\u3055\u3044"],
    "ikura-desu-ka": ["\u3044\u304f\u3089\u3067\u3059\u304b"],
    "kaado-de-onegaishimasu": ["\u30ab\u30fc\u30c9\u3067\u304a\u9858\u3044\u3057\u307e\u3059"],
    "futari-desu": ["\u4e8c\u4eba\u3067\u3059", "\u3075\u305f\u308a\u3067\u3059"],
    "osusume-wa-nan-desu-ka": ["\u304a\u3059\u3059\u3081\u306f\u4f55\u3067\u3059\u304b"],
    "okaikei-onegaishimasu": ["\u304a\u4f1a\u8a08\u304a\u9858\u3044\u3057\u307e\u3059"],
    "sumimasen2": ["\u3059\u307f\u307e\u305b\u3093"],
    "sumimasen": ["\u3059\u307f\u307e\u305b\u3093"],
    "mou-ichido-onegaishimasu": ["\u3082\u3046\u4e00\u5ea6\u304a\u9858\u3044\u3057\u307e\u3059"],
    "yukkuri-onegaishimasu": ["\u3086\u3063\u304f\u308a\u304a\u9858\u3044\u3057\u307e\u3059"],
    "pointo-kaado": ["\u30dd\u30a4\u30f3\u30c8\u30ab\u30fc\u30c9"],
    "atatamemasu-ka": ["\u6e29\u3081\u307e\u3059\u304b", "\u3042\u305f\u305f\u3081\u307e\u3059\u304b"],
    "ohashi-wa-otsukeshimasu-ka": ["\u304a\u7b38\u306f\u304a\u4ed8\u3051\u3057\u307e\u3059\u304b"],
    "shichaku-shitemo-ii-desu-ka": ["\u8a66\u7740\u3057\u3066\u3082\u3044\u3044\u3067\u3059\u304b"],
    "hoka-no-iro-wa-arimasu-ka": ["\u4ed6\u306e\u8272\u306f\u3042\u308a\u307e\u3059\u304b", "\u307b\u304b\u306e\u8272\u306f\u3042\u308a\u307e\u3059\u304b"],
    "kono-densha-wa-toukyou": ["\u3053\u306e\u96fb\u8eca\u306f\u6771\u4eac"],
    "tsugi-no-eki-wa-doko": ["\u6b21\u306e\u99c5\u306f\u3069\u3053"],

    # verbs (conjugated forms)
    "masu": ["\u307e\u3059"], "kakimasu": ["\u66f8\u304d\u307e\u3059"],
    "tabemasu": ["\u98df\u3079\u307e\u3059"], "shimasu": ["\u3057\u307e\u3059"],
    "kimasu": ["\u6765\u307e\u3059", "\u304d\u307e\u3059"],
    "te": ["\u3066"], "ite": ["\u3044\u3066"],
    "kaite": ["\u66f8\u3044\u3066", "\u304b\u3044\u3066"],
    "ide": ["\u3044\u3067"],
    "shite": ["\u3057\u3066"],
    "hanashite": ["\u8a71\u3057\u3066", "\u306f\u306a\u3057\u3066"],
    "nde": ["\u3093\u3067"],
    "tonde": ["\u98db\u3093\u3067", "\u3068\u3093\u3067"],
    "tte": ["\u3063\u3066"],
    "matte": ["\u5f85\u3063\u3066", "\u307e\u3063\u3066"],
    "itte": ["\u884c\u3063\u3066", "\u3044\u3063\u3066", "\u8a00\u3063\u3066"],
    "oyoide": ["\u6cf3\u3044\u3067", "\u304a\u3088\u3044\u3067"],
    "teimasu": ["\u3066\u3044\u307e\u3059"],
    "tabete-imasu": ["\u98df\u3079\u3066\u3044\u307e\u3059"],
    "tabeteimasu": ["\u98df\u3079\u3066\u3044\u307e\u3059"],
    "tehaikemasen": ["\u3066\u306f\u3044\u3051\u307e\u305b\u3093"],
    "tabete-haikemasen": ["\u98df\u3079\u3066\u306f\u3044\u3051\u307e\u305b\u3093"],
    "nai": ["\u306a\u3044"], "kakanai": ["\u66f8\u304b\u306a\u3044"],
    "tabenai": ["\u98df\u3079\u306a\u3044"],
    "shinai": ["\u3057\u306a\u3044"],
    "konai": ["\u6765\u306a\u3044", "\u3053\u306a\u3044"],
    "ta": ["\u305f"],
    "kaita": ["\u66f8\u3044\u305f"], "tabeta": ["\u98df\u3079\u305f"],
    "kaki-masen": ["\u66f8\u304d\u307e\u305b\u3093"],
    "kaki-mashita": ["\u66f8\u304d\u307e\u3057\u305f"],
    "tabe-masen": ["\u98df\u3079\u307e\u305b\u3093"],
    "tabe-mashita": ["\u98df\u3079\u307e\u3057\u305f"],
    "shimasen": ["\u3057\u307e\u305b\u3093"],
    "shimashita": ["\u3057\u307e\u3057\u305f"],

    # adjectives
    "okii": ["\u5927\u304d\u3044", "\u304a\u304a\u304d\u3044"],
    "chiisai": ["\u5c0f\u3055\u3044", "\u3061\u3044\u3055\u3044"],
    "atarashii": ["\u65b0\u3057\u3044", "\u3042\u305f\u3089\u3057\u3044"],
    "furui": ["\u53e4\u3044", "\u3075\u308b\u3044"],
    "utsukushii": ["\u7f8e\u3057\u3044", "\u3046\u3064\u304f\u3057\u3044"],
    "oishii": ["\u304a\u3044\u3057\u3044", "\u7f8e\u5473\u3057\u3044"],
    "atsui": ["\u6691\u3044", "\u71b1\u3044", "\u3042\u3064\u3044"],
    "samui": ["\u5bd2\u3044", "\u3055\u3080\u3044"],
    "oishikunai": ["\u304a\u3044\u3057\u304f\u306a\u3044"],
    "oishikatta": ["\u304a\u3044\u3057\u304b\u3063\u305f"],
    "oishikunakatta": ["\u304a\u3044\u3057\u304f\u306a\u304b\u3063\u305f"],
    "oishiku": ["\u304a\u3044\u3057\u304f"],
    "oishii-desu": ["\u304a\u3044\u3057\u3044\u3067\u3059"],
    "oishiidesu": ["\u304a\u3044\u3057\u3044\u3067\u3059"],
    "yokunai": ["\u3088\u304f\u306a\u3044"],
    "yokatta": ["\u3088\u304b\u3063\u305f"],
    "yokunakatta": ["\u3088\u304f\u306a\u304b\u3063\u305f"],
    "genki-na": ["\u5143\u6c17\u306a"],
    "shizuka-na": ["\u9759\u304b\u306a"],
    "yumei-na": ["\u6709\u540d\u306a"],
    "kirei-na": ["\u304d\u308c\u3044\u306a", "\u7dba\u9e97\u306a"],
    "benri-na": ["\u4fbf\u5229\u306a"],
    "suki-na": ["\u597d\u304d\u306a"],
    "kirai-na": ["\u5acc\u3044\u306a"],
    "taihen-na": ["\u5927\u5909\u306a"],
    "genki-na-hito": ["\u5143\u6c17\u306a\u4eba"],
    "genki-desu": ["\u5143\u6c17\u3067\u3059"],
    "genki-ja-nai": ["\u5143\u6c17\u3058\u3083\u306a\u3044"],
    "genki-deshita": ["\u5143\u6c17\u3067\u3057\u305f"],
    "genki-janakatta": ["\u5143\u6c17\u3058\u3083\u306a\u304b\u3063\u305f"],
    "genki-ni": ["\u5143\u6c17\u306b"],
    "kirei": ["\u304d\u308c\u3044", "\u7dba\u9e97"],
    "kirai": ["\u5acc\u3044", "\u304d\u3089\u3044"],

    # kanjin5 (numbers)
    "ichi": ["\u4e00", "\u3044\u3061"],
    "ni": ["\u4e8c", "\u306b"],
    "san": ["\u4e09", "\u3055\u3093"],
    "shi": ["\u56db", "\u3057", "\u6b7b"],
    "go": ["\u4e94", "\u3054"],
    "roku": ["\u516d", "\u308d\u304f"],
    "shichi": ["\u4e03", "\u3057\u3061"],
    "hachi": ["\u516b", "\u306f\u3061"],
    "kyuu": ["\u4e5d", "\u304d\u3085\u3046"],
    "juu": ["\u5341", "\u3058\u3085\u3046"],
    "hyaku": ["\u767e", "\u3072\u3083\u304f"],
    "sen": ["\u5343", "\u305b\u3093"],
    "man": ["\u4e07", "\u307e\u3093"],
    "en": ["\u5186", "\u3048\u3093"],
    "nichi": ["\u65e5", "\u306b\u3061"],
    "gatsu": ["\u6708", "\u304c\u3064"],
    "hi": ["\u65e5", "\u3072", "\u706b"],
    "ki": ["\u6728", "\u304d", "\u6c17"],
    "kin": ["\u91d1", "\u304d\u3093"],

    # kanjin4
    "omoi": ["\u91cd\u3044", "\u304a\u3082\u3044", "\u601d\u3044"],
    "chi": ["\u5730", "\u3061", "\u8840"],
    "kou": ["\u9ad8", "\u3053\u3046", "\u516c", "\u5149"],
    "you": ["\u7528", "\u3088\u3046", "\u66dc"],
    "jaku": ["\u5f31", "\u3058\u3083\u304f"],
    "shin": ["\u65b0", "\u3057\u3093", "\u5fc3", "\u771f"],
    "ko": ["\u5b50", "\u3053", "\u500b", "\u53e4"],
    "shou": ["\u5c0f", "\u3057\u3087\u3046", "\u5c11"],
    "dou": ["\u9053", "\u3069\u3046", "\u540c"],
    "betsu": ["\u5225", "\u3079\u3064"],
    "ji": ["\u6642", "\u3058", "\u5b57"],
    "saku": ["\u4f5c", "\u3055\u304f"],
    "owari": ["\u7d42\u308f\u308a", "\u304a\u308f\u308a"],
    "tai": ["\u5927", "\u305f\u3044", "\u4f53"],
    "sou": ["\u8d70", "\u305d\u3046", "\u65e9"],
    "hen": ["\u5909", "\u3078\u3093", "\u8fba"],

    # nontbl
    "desu": ["\u3067\u3059"],
    "kara-kimashita": ["\u304b\u3089\u6765\u307e\u3057\u305f"],
    "karakimashita": ["\u304b\u3089\u6765\u307e\u3057\u305f"],
    "shumi-wa-desu": ["\u8da3\u5473\u306f\u3067\u3059", "\u8da3\u5473\u306f"],
    "to-moushimasu": ["\u3068\u7533\u3057\u307e\u3059"],
    "tomoushimasu": ["\u3068\u7533\u3057\u307e\u3059"],
    "hataraiteorimasu": ["\u50cd\u3044\u3066\u304a\u308a\u307e\u3059"],
    "nihongo-benkyouchuu": ["\u65e5\u672c\u8a9e\u52c9\u5f37\u4e2d"],
    "douzo-yoroshiku": ["\u3069\u3046\u305e\u3088\u308d\u3057\u304f"],
    "douzoyoroshiku": ["\u3069\u3046\u305e\u3088\u308d\u3057\u304f"],
    "osewa-ni-natte": ["\u304a\u4e16\u8a71\u306b\u306a\u3063\u3066"],
    "oisogashii-tokoro": ["\u304a\u5fd9\u3057\u3044\u3068\u3053\u308d"],
    "gokakunin-nohodo": ["\u3054\u78ba\u8a8d\u306e\u307b\u3069"],
    "onaka-ga-suita": ["\u304a\u8179\u304c\u7a7a\u3044\u305f", "\u304a\u306a\u304b\u304c\u3059\u3044\u305f"],
    "nodo-ga-kawaita": ["\u5589\u304c\u6e07\u3044\u305f", "\u306e\u3069\u304c\u304b\u308f\u3044\u305f"],
    "okawari": ["\u304a\u304b\u308f\u308a", "\u304a\u4ee3\u308f\u308a"],

    # hiragana/katakana labels
    "hiragana": ["\u3072\u3089\u304c\u306a", "\u5e73\u4eee\u540d"],
    "katakana": ["\u30ab\u30bf\u30ab\u30ca", "\u304b\u305f\u304b\u306a", "\u7247\u4eee\u540d"],
    # single kana - allow kanji STT readings
    "wa": ["\u308f", "\u306f", "\u30ef"],
    "di": ["\u3062", "\u30c2", "\u3058", "\u5b57"],
    "small-yo": ["\u3087", "\u30e7"],
    "small-ya": ["\u3083", "\u30e3"],
    "small-yu": ["\u3085", "\u30e5"],
    "hoteru": ["\u30db\u30c6\u30eb"],
    "resutoran": ["\u30ec\u30b9\u30c8\u30e9\u30f3"],
    "fa": ["\u30d5\u30a1", "\u3075\u3041"],

    # Additional kanjin readings
    "bun": ["\u6587", "\u3076\u3093"],
    "nama": ["\u751f", "\u306a\u307e"],
    "bai": ["\u500d", "\u3070\u3044", "\u6885", "\u58f2"],
    "sha": ["\u8eca", "\u3057\u3083", "\u793e", "\u8b1d"],
    "hana": ["\u82b1", "\u306f\u306a", "\u9f3b"],
    "shitsu": ["\u5ba4", "\u3057\u3064", "\u8cea"],

    # Additional nontbl
    "arubaito": ["\u30a2\u30eb\u30d0\u30a4\u30c8"],
    "dokidoki-suru": ["\u30c9\u30ad\u30c9\u30ad\u3059\u308b"],
    "jiko-shoukai": ["\u81ea\u5df1\u7d39\u4ecb"],
    "kenjougo": ["\u8b19\u8b72\u8a9e", "\u3051\u3093\u3058\u3087\u3046\u3054"],
    "ame-ga-zaazaa": ["\u96e8\u304c\u30b6\u30fc\u30b6\u30fc"],
    "imasu-arimasu": ["\u3044\u307e\u3059\u3042\u308a\u307e\u3059"],
    "shita-whispered": ["\u3057\u305f"],
    "hashi-chopsticks": ["\u7bb8", "\u306f\u3057"],
    "hashi-bridge": ["\u6a4b", "\u306f\u3057"],
    "ame-rain": ["\u96e8", "\u3042\u3081"],
    "ame-candy": ["\u98f4", "\u3042\u3081"],
    "hana-flower": ["\u82b1", "\u306f\u306a"],
    "hana-nose": ["\u9f3b", "\u306f\u306a"],
    "sake-alcohol": ["\u9152", "\u3055\u3051"],
    "sake-salmon": ["\u9bad", "\u3055\u3051", "\u30b7\u30e3\u30b1", "\u9bae"],
}


def romaji_to_kana(romaji):
    """Convert romaji string to hiragana (best-effort)."""
    result = []
    s = romaji.lower()
    i = 0
    while i < len(s):
        matched = False
        for length in (4, 3, 2, 1):
            chunk = s[i:i + length]
            if chunk in ROMAJI_TO_HIRAGANA:
                result.append(ROMAJI_TO_HIRAGANA[chunk])
                i += length
                matched = True
                break
        if not matched:
            result.append(s[i])
            i += 1
    return "".join(result)


def extract_expected(filename, prefix):
    """
    Given a filename like 'core100-020-taberu.mp3', return a list of
    acceptable transcription strings (kana, kanji, or katakana forms).
    """
    stem = Path(filename).stem
    m = re.match(rf"^{re.escape(prefix)}\d+-(.+)$", stem)
    if not m:
        return []
    hint = m.group(1)

    candidates = []
    # Check overrides (with hyphens and collapsed)
    if hint in WORD_OVERRIDES:
        candidates.extend(WORD_OVERRIDES[hint])
    collapsed = hint.replace("-", "")
    if collapsed != hint and collapsed in WORD_OVERRIDES:
        candidates.extend(WORD_OVERRIDES[collapsed])

    # Also generate kana from romaji
    for variant in (hint, collapsed):
        kana = romaji_to_kana(variant)
        if kana:
            candidates.append(kana)
            candidates.append(_hira_to_kata(kana))

    # Deduplicate preserving order
    seen = set()
    unique = []
    for c in candidates:
        if c not in seen:
            seen.add(c)
            unique.append(c)
    return unique


def check_match(transcription, expected_list):
    """Check if transcription contains any of the expected strings."""
    if not expected_list or not transcription:
        return False
    t = transcription.strip()
    # Remove all punctuation (Japanese and Western)
    t_clean = re.sub(r"[\u3002\u3001\uff0c\uff0e.!\uff1f?\u300c\u300d\u3000\s\uff01]", "", t)
    for exp in expected_list:
        e = exp.strip()
        if not e:
            continue
        e_clean = re.sub(r"[\u3002\u3001\uff0c\uff0e.!\uff1f?\u300c\u300d\u3000\s\uff01]", "", e)
        # Substring checks in both directions
        if e in t or t in e or e_clean in t_clean or t_clean in e_clean:
            return True
        if e in t_clean or t_clean in e:
            return True
    return False


def get_prefix_for_file(filename):
    for p in ("core100-", "hira-", "kata-", "verb-", "greet-", "daily-",
              "adj-", "kanjin5-", "kanjin4-", "gap-", "nontbl-", "pitch-"):
        if filename.startswith(p):
            return p
    return ""


def sample_files():
    """Sample ~100 files across the 10 categories."""
    categories = [
        ("core100-*.mp3", 10),
        ("hira-*.mp3", 10),
        ("kata-*.mp3", 10),
        ("verb-*.mp3", 10),
        (["greet-*.mp3", "daily-*.mp3"], 10),
        ("adj-*.mp3", 10),
        (["kanjin5-*.mp3", "kanjin4-*.mp3"], 10),
        ("gap-*.mp3", 10),
        ("nontbl-*.mp3", 10),
        ("pitch-*.mp3", 10),
    ]

    random.seed(42)
    selected = []

    for pattern, count in categories:
        if isinstance(pattern, list):
            files = []
            for p in pattern:
                files.extend(AUDIO_DIR.glob(p))
        else:
            files = list(AUDIO_DIR.glob(pattern))

        files.sort(key=lambda f: f.name)
        if len(files) <= count:
            selected.extend(files)
        else:
            selected.extend(random.sample(files, count))

    return selected


def main():
    # Get Azure key
    az_cmd = r"C:\Program Files\Microsoft SDKs\Azure\CLI2\wbin\az.cmd"
    r = subprocess.run(
        [az_cmd, "cognitiveservices", "account", "keys", "list",
         "--name", "tts-tester", "--resource-group", "tts-resources",
         "--query", "key1", "-o", "tsv"],
        capture_output=True, text=True, shell=True
    )
    key = r.stdout.strip()
    if not key:
        print(f"ERROR: Could not retrieve Azure key.\nstderr: {r.stderr}")
        return
    print(f"Azure key retrieved ({len(key)} chars)")

    # Sample files
    clips = sample_files()
    print(f"Sampled {len(clips)} clips across categories")

    # Set up Azure Speech config
    speech_config = speechsdk.SpeechConfig(subscription=key, region=REGION)
    speech_config.speech_recognition_language = "ja-JP"

    results = []  # (filename, category, expected_list, transcription, status)

    for idx, clip_path in enumerate(clips, 1):
        fname = clip_path.name
        prefix = get_prefix_for_file(fname)
        expected = extract_expected(fname, prefix)
        expected_str = " / ".join(expected[:5]) if expected else "[no expected]"

        print(f"[{idx}/{len(clips)}] {fname} ...", end=" ", flush=True)

        try:
            # Convert MP3 to WAV (16kHz mono 16-bit) for Azure SDK
            wav_path = clip_path.with_suffix(".tmp.wav")
            audio_seg = AudioSegment.from_mp3(str(clip_path))
            audio_seg = audio_seg.set_frame_rate(16000).set_channels(1).set_sample_width(2)
            audio_seg.export(str(wav_path), format="wav")

            audio_config = speechsdk.AudioConfig(filename=str(wav_path))
            recognizer = speechsdk.SpeechRecognizer(
                speech_config=speech_config, audio_config=audio_config
            )
            result = recognizer.recognize_once()

            # Clean up temp wav
            try:
                wav_path.unlink()
            except OSError:
                pass

            if result.reason == speechsdk.ResultReason.RecognizedSpeech:
                transcription = result.text
            elif result.reason == speechsdk.ResultReason.NoMatch:
                transcription = "[NO_MATCH]"
            else:
                transcription = f"[ERROR: {result.reason}]"
        except Exception as exc:
            transcription = f"[EXCEPTION: {exc}]"

        if transcription.startswith("["):
            status = "ERROR"
        elif check_match(transcription, expected):
            status = "MATCH"
        else:
            status = "MISMATCH"

        print(f"{transcription}  -> {status}")
        results.append((fname, prefix.rstrip("-"), expected_str, transcription, status))

        time.sleep(0.3)

    # Tally
    n_match = sum(1 for r in results if r[4] == "MATCH")
    n_mismatch = sum(1 for r in results if r[4] == "MISMATCH")
    n_error = sum(1 for r in results if r[4] == "ERROR")
    total = len(results)

    # Write report
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write("  STT SPOT-CHECK REPORT\n")
        f.write(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 80 + "\n\n")
        f.write("SUMMARY\n")
        f.write(f"  Total clips tested : {total}\n")
        f.write(f"  Matched            : {n_match}/{total}\n")
        f.write(f"  Mismatched         : {n_mismatch}/{total}\n")
        f.write(f"  Errors             : {n_error}/{total}\n")
        f.write(f"  Match rate         : {n_match/max(total,1)*100:.1f}%\n")
        f.write("\n" + "-" * 80 + "\n")

        # Category breakdown
        f.write("\nCATEGORY BREAKDOWN\n")
        cats = {}
        for row in results:
            cat = row[1]
            cats.setdefault(cat, {"match": 0, "mismatch": 0, "error": 0})
            cats[cat][row[4].lower()] = cats[cat].get(row[4].lower(), 0) + 1
        for cat in sorted(cats):
            c = cats[cat]
            t = c["match"] + c["mismatch"] + c["error"]
            f.write(f"  {cat:12s}  {c['match']}/{t} match, "
                    f"{c['mismatch']}/{t} mismatch, {c['error']}/{t} error\n")
        f.write("\n" + "-" * 80 + "\n\n")

        # Detail
        f.write("DETAILED RESULTS\n\n")
        for fname, cat, expected_str, transcription, status in results:
            marker = "OK" if status == "MATCH" else ("XX" if status == "MISMATCH" else "!!")
            f.write(f"  [{marker}] {status:8s}  {fname}\n")
            f.write(f"      Category    : {cat}\n")
            f.write(f"      Expected    : {expected_str}\n")
            f.write(f"      Transcribed : {transcription}\n\n")

        # Mismatches section
        mismatches = [r for r in results if r[4] == "MISMATCH"]
        if mismatches:
            f.write("-" * 80 + "\n")
            f.write(f"\nMISMATCHES ({len(mismatches)} clips)\n\n")
            for fname, cat, expected_str, transcription, _ in mismatches:
                f.write(f"  {fname}\n")
                f.write(f"    Expected    : {expected_str}\n")
                f.write(f"    Transcribed : {transcription}\n\n")

        # Errors section
        errors = [r for r in results if r[4] == "ERROR"]
        if errors:
            f.write("-" * 80 + "\n")
            f.write(f"\nERRORS ({len(errors)} clips)\n\n")
            for fname, cat, expected_str, transcription, _ in errors:
                f.write(f"  {fname}  ->  {transcription}\n")

    print(f"\nReport saved to: {REPORT_PATH}")
    print(f"Summary: {n_match}/{total} match, {n_mismatch}/{total} mismatch, "
          f"{n_error}/{total} error")


if __name__ == "__main__":
    main()
