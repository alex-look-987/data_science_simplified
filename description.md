# feat: Ruff Implementation

## Summary

Unifies formatting and linting tooling (black, flake8, isort) into Ruff,
and reclassifies code-quality dependencies as dev-dependencies in uv so
they are not installed in production.

## Issue / Motivation

Formatting and linting currently depend on three independent tools
(black, flake8, isort), leading to duplicated configuration, longer CI
times, and potential conflicts between them.

## Changes

- Replace `black`, `flake8`, and `isort` with `ruff` (formatter + linter
  + import sorter in a single tool)
- Update pre-commit configuration to use ruff hooks
- Move `mypy`, `interrogate`, and `pre-commit` from `dependencies` to
  `[dependency-groups.dev]` in `pyproject.toml`, so they're installed
  only in development/CI environments, not in production
- Update `uv.lock`

## Impact

- Single tool for the entire code-quality process → faster CI and
  simpler configuration
- `uv sync --no-dev` in production installs fewer packages (smaller
  deployment surface)
- No behavior changes to production code

## How to test

```bash
uv sync
uv run ruff check .
uv run ruff format --check .
uv run pre-commit run --all-files
```

## Checklist

- [ ] `uv.lock` updated and committed
- [ ] Pre-commit hooks passing
- [ ] CI passes with the new configuration
- [ ] Contributing docs/README updated if they reference black/flake8/isort