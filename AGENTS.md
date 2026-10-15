# AGENTS.md — silent-failure-scanner

Machine-readable entry for AI agents.

## Purpose
Catch silent AI failures before they ship.

## Invocation
```bash
python scripts/silent_scanner.py <file|text> [--json]
```

## Output contract
- Structured JSON available via `--json` (fields: verdict, score, sha256_8, hits).
- Exit code: 0 = PASS, 1 = FAIL (fail-closed).

## Rules
- Static analysis only; never executes external commands.
- FAIL verdict requires human decision before proceeding.
- No placeholders in outputs.
