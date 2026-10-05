from model.runtime import DEFAULT_MODEL_ID, ModelRuntime


def test_runtime_defaults_to_declared_teacher_model():
    assert DEFAULT_MODEL_ID == "HuggingFaceTB/SmolLM2-135M-Instruct"


def test_runtime_starts_unloaded():
    runtime = ModelRuntime()
    assert runtime.loaded is False
