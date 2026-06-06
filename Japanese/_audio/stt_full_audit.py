"""Compatibility wrapper for a full source-aware STT audit."""

from __future__ import annotations

from stt_spot_check import main


if __name__ == "__main__":
    raise SystemExit(main(["--live", "--all"]))
