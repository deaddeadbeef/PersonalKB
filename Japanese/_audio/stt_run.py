"""Compatibility wrapper for the source-aware STT spot check."""

from __future__ import annotations

from stt_spot_check import main


if __name__ == "__main__":
    raise SystemExit(main(["--live"]))
