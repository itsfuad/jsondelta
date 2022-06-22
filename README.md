# JSONDelta

Diff JSON settings and API fixtures with paths instead of noisy line diffs.
Uses only Python 3.9 standard-library modules.

## Usage

```
python cli.py examples/old.json examples/new.json
python cli.py examples/old.json examples/new.json --json
python -m unittest discover -s tests
```

Exit status is `0` for equal files, `1` for differences, and an exception for
unreadable or invalid JSON. Array element order is significant.
