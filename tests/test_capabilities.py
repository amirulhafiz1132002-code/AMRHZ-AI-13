from runtime.capabilities import (
    RuntimeCapabilities,
    capability_status,
)


def test_ready_requires_all_model_runtime_dependencies() -> None:
    ready = RuntimeCapabilities(
        python_version="3.13.0",
        operating_system="Windows",
        machine="AMD64",
        torch_available=True,
        transformers_available=True,
        tokenizers_available=True,
        model_runtime_ready=True,
    )
    assert capability_status(ready) == "READY"


def test_missing_dependency_is_environment_blocked() -> None:
    partial = RuntimeCapabilities(
        python_version="3.14.6",
        operating_system="Linux",
        machine="aarch64",
        torch_available=True,
        transformers_available=False,
        tokenizers_available=False,
        model_runtime_ready=False,
    )
    assert capability_status(partial) == "PARTIAL / ENVIRONMENT-BLOCKED"
