"""Portable environment capability detection for AMRHZ-AI-13.

This layer detects what the current device can actually support. It does not
install dependencies, download models, or claim inference capability merely
because a package is present.
"""

from __future__ import annotations

import importlib.util
import platform
import sys
from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class RuntimeCapabilities:
    """Observed capabilities of the current Python runtime."""

    python_version: str
    operating_system: str
    machine: str
    torch_available: bool
    transformers_available: bool
    tokenizers_available: bool
    model_runtime_ready: bool

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _module_available(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def detect_capabilities() -> RuntimeCapabilities:
    """Detect installed/runtime capabilities without importing heavy packages."""
    torch_available = _module_available("torch")
    transformers_available = _module_available("transformers")
    tokenizers_available = _module_available("tokenizers")

    return RuntimeCapabilities(
        python_version=platform.python_version(),
        operating_system=platform.system(),
        machine=platform.machine(),
        torch_available=torch_available,
        transformers_available=transformers_available,
        tokenizers_available=tokenizers_available,
        model_runtime_ready=(
            torch_available
            and transformers_available
            and tokenizers_available
        ),
    )


def capability_status(capabilities: RuntimeCapabilities | None = None) -> str:
    """Return a conservative state suitable for evidence/reporting."""
    caps = capabilities or detect_capabilities()
    return "READY" if caps.model_runtime_ready else "PARTIAL / ENVIRONMENT-BLOCKED"


if __name__ == "__main__":
    import json

    caps = detect_capabilities()
    print(json.dumps({
        "capabilities": caps.to_dict(),
        "status": capability_status(caps),
    }, indent=2))
