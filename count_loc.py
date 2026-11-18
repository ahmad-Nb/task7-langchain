"""Count non-blank, non-comment lines of Python code.  Usage: python count_loc.py file1.py [file2.py ...]"""
import sys
from pathlib import Path

total = 0
for name in sys.argv[1:]:
    in_doc, n = False, 0
    for line in Path(name).read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith(('"""', "'''")):
            if not (len(s) > 3 and s.endswith(s[:3])):  # one-line docstrings are skipped
                in_doc = not in_doc
            continue
        if in_doc or not s or s.startswith("#"):
            continue
        n += 1
    print(f"{name:<30} {n:>5}")
    total += n
print(f"{'TOTAL':<30} {total:>5}")
