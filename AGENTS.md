# AI Working Contract — AMRHZ-AI-13

This repository's role in the AMRHZ ecosystem: **AI runtime and model project**.

## Required reading
1. [Local adoption status](docs/AMRHZ-STANDARDS-ADOPTION.md)
2. [Canonical UI Evolution Contract](https://github.com/amirulhafiz1132002-code/amrhz-architecture-core/blob/main/docs/standards/UI-EVOLUTION-CONTRACT.md)
3. [Canonical Dual-Layer Documentation Standard](https://github.com/amirulhafiz1132002-code/amrhz-architecture-core/blob/main/docs/standards/DUAL-LAYER-DOCUMENTATION-STANDARD.md)
4. [Canonical Evidence and State Contract](https://github.com/amirulhafiz1132002-code/amrhz-architecture-core/blob/main/docs/standards/EVIDENCE-AND-STATE-CONTRACT.md)

Canonical standards proposal: [amrhz-architecture-core PR #1](https://github.com/amirulhafiz1132002-code/amrhz-architecture-core/pull/1). Until that PR is reviewed and merged, treat the standards as **PROPOSED**, not as an approved or enforced policy.

## Repository-specific boundaries
- Do not infer model readiness, deployment, or performance from documentation or dependency installation alone. Do not change runtime/model code, weights, datasets, workflows, or device configuration as part of standards adoption.
- Existing README.md and docs/CROSS_DEVICE_RUNTIME.md provide project-specific context; reconcile claims with current source, tests, and runtime evidence.
- Inspect the current branch, implementation, relevant tests, and configuration before proposing a change.
- Use the smallest change that solves a demonstrated problem. Keep unrelated files and behavior unchanged.
- Do not claim `VERIFIED` without a scoped, observed test result; do not claim `LIVE` without environment-specific deployment/runtime evidence.
- If evidence is missing or contradictory, report `BLOCKED` or `UNKNOWN`; do not fill gaps with assumptions.
- Do not deploy, delete data, change secrets, rewrite architecture, or expand into other repositories unless explicitly approved.
- Report changed files, tests actually run, results, limitations, and remaining unknowns.

These instructions document intended workflow; they do not by themselves prove that automated enforcement exists.
