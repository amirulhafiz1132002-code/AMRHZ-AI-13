# AMRHZ Cross-Device Runtime Strategy v0.1

**State:** LOCKED  
**Checkpoint:** 2026-10-06

## Principle

> **Build portable infrastructure on Android, but reserve heavyweight model execution for environments that genuinely support it.**

AMRHZ development must not become dependent on one physical device.

## Architecture

```
AMRHZ CORE
    ↓
Environment Detection
    ↓
Capability Verification
    ↓
Select Supported Runtime
    ↓
Execute
    ↓
Verify
    ↓
Report REAL STATE
```

## Runtime roles

### Android / Termux

Android is a valid AMRHZ runtime node for:

- environment detection
- repository inspection
- capability reporting
- lightweight tests
- portable tooling
- documentation and protocol verification
- any runtime component that the environment genuinely supports

Android is **not** required to execute the heavyweight model stack when its dependency/runtime constraints prevent that.

### PC / full development environment

The PC is the intended environment for:

- full Transformers runtime
- model loading
- inference smoke tests
- heavier model development
- later AMRHZ transformation work

This boundary can change only through new evidence and an explicit architecture decision.

### Repository

The repository is the common source of truth for:

- code
- tests
- protocols
- architecture
- documented state
- provenance

## Current Android evidence

Tested environment:

- OS: Android / Termux
- Architecture: ARM64 / aarch64
- Python: 3.14.6
- PyTorch: 2.14.1

Observed:

| Capability | State |
|---|---|
| PyTorch import | VERIFIED |
| CPU device | VERIFIED |
| Transformers | NOT AVAILABLE |
| Compatible `tokenizers` PyPI binary | NOT AVAILABLE |
| Native Termux `tokenizers` package | NOT FOUND |
| Source build | BLOCKED |
| Model inference | NOT VERIFIED |

### Interpretation

The Android result establishes a **runtime/dependency compatibility boundary**.

It does not establish that the working-model implementation is broken.

No dependency, model architecture, or requirements change should be introduced solely to manufacture a green result on this environment.

## Cross-device contract

The same verification protocol should run wherever practical:

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

A device reports what it can actually do.

It does not inherit another device's status.

## State rule

```
ANDROID
  ↓
PARTIAL / ENVIRONMENT-BLOCKED

PC
  ↓
READY only after dependencies are verified

MODEL
  ↓
VERIFIED only after real inference evidence exists

SYSTEM
  ↓
LIVE only after integrated runtime evidence exists
```

## Next implementation

**AMRHZ Portable Runtime Layer v0.1**

Acceptance should remain evidence-based and incremental:

1. detect runtime environment
2. report capabilities
3. identify supported execution path
4. run the applicable lightweight verification
5. report explicit state
6. preserve the same protocol for PC verification

---

**Locked:** 2026-10-06  
**Strategy:** Portable infrastructure + environment-honest execution  
**Core rule:** Evidence > claim
