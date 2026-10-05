# AMRHZ-AI-13 — Working Model v0.1

## Purpose

This checkpoint establishes the first **real runnable model layer** before AMRHZ-specific transformation.

## State

**DEVELOPMENT**

This file does **not** claim VERIFIED or LIVE. Verification requires executing the smoke test in a real environment.

## Current model

- Base/teacher model: `HuggingFaceTB/SmolLM2-135M-Instruct`
- Runtime: Hugging Face Transformers + PyTorch
- Entry point: `model.runtime.ModelRuntime`
- Smoke test: `scripts/smoke_test.py`

The selected model is an external base/teacher reference. Its weights are not being relabeled as AMRHZ-owned.

## Acceptance criteria

1. Dependencies install successfully.
2. Tokenizer loads.
3. Model weights load.
4. A non-empty response is generated.
5. Smoke test reports `SMOKE_TEST_PASS`.

Only after these pass do we move to the next stage:

**WORK → AMRHZ transformation → EVOLVE**


## Cross-Device Runtime Boundary — 2026-10-06

The working model follows the locked AMRHZ cross-device strategy:

> **Build portable infrastructure on Android, but reserve heavyweight model execution for environments that genuinely support it.**

### Android evidence

Environment tested: Android / Termux / ARM64 / Python 3.14.6.

- PyTorch 2.14.1: **VERIFIED** — import succeeds and CPU device is available.
- Transformers: **NOT AVAILABLE**.
- Required `tokenizers` binary wheel: **NOT AVAILABLE** for the tested PyPI environment.
- Native Termux `tokenizers` package: **NOT FOUND** in the checked package search.
- Source build: **BLOCKED** during Android API-level detection.
- Model inference: **NOT TESTED / NOT VERIFIED**.

### Interpretation

This is an **environment compatibility boundary**, not evidence that the model runtime code is broken.

The current Android environment is therefore:

**PARTIAL / ENVIRONMENT-BLOCKED**

No requirements or model architecture changes should be made merely to force this environment to pass.

### Portable runtime rule

The same repository, protocol, and evidence rules should work across Android and PC. Each device reports its own capability rather than pretending all environments are equivalent.

```
DEVICE
  ↓
DETECT
  ↓
CAPABILITY
  ↓
SUPPORTED EXECUTION
  ↓
VERIFY
  ↓
REAL STATE
```

The next implementation task is **AMRHZ Portable Runtime Layer v0.1**.
