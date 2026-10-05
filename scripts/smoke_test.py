"""Runtime smoke test for AMRHZ-AI-13 working-model v0.1."""

from model.runtime import DEFAULT_MODEL_ID, smoke_inference


if __name__ == "__main__":
    response = smoke_inference()
    if not response:
        raise SystemExit("SMOKE_TEST_FAIL: model returned an empty response")

    print("SMOKE_TEST_PASS")
    print(f"MODEL_ID={DEFAULT_MODEL_ID}")
    print(f"RESPONSE={response}")
