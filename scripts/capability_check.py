"""Print observed AMRHZ-AI-13 runtime capabilities as JSON."""

import json

from runtime.capabilities import capability_status, detect_capabilities


if __name__ == "__main__":
    capabilities = detect_capabilities()
    print(json.dumps({
        "status": capability_status(capabilities),
        "capabilities": capabilities.to_dict(),
    }, indent=2))
