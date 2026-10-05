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
