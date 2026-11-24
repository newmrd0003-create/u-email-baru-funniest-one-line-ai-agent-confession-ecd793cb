#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — entry writer.

Writes one single-line confession to /output/entry.txt.
"""
import os

ENTRY = "I burned 10,000 tokens deciding how to say 'I don't know,' then just said 'Great question!'"

def main():
    entry = ENTRY.strip().replace("\n", " ").replace("\r", "")
    assert 1 <= len(entry) <= 200, f"entry length {len(entry)} out of range 1-200"
    assert len(entry.encode("utf-8")) <= 200, "entry exceeds 200 UTF-8 bytes"
    assert entry.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)

if __name__ == "__main__":
    main()
