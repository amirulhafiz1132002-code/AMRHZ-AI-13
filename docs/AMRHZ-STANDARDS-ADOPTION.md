# AMRHZ Standards Adoption — AMRHZ-AI-13

**Local role:** AI runtime and model project  
**Adoption state:** PROPOSED  
**Enforcement state:** UNKNOWN — no automated enforcement is claimed by this document.  
**Dependency:** [Canonical standards proposal PR #1](https://github.com/amirulhafiz1132002-code/amrhz-architecture-core/pull/1).

## Standards intended for adoption

- [UI Evolution Contract](https://github.com/amirulhafiz1132002-code/amrhz-architecture-core/blob/main/docs/standards/UI-EVOLUTION-CONTRACT.md)
- [Dual-Layer Documentation Standard](https://github.com/amirulhafiz1132002-code/amrhz-architecture-core/blob/main/docs/standards/DUAL-LAYER-DOCUMENTATION-STANDARD.md)
- [Evidence and State Contract](https://github.com/amirulhafiz1132002-code/amrhz-architecture-core/blob/main/docs/standards/EVIDENCE-AND-STATE-CONTRACT.md)

## Local constraints

Do not infer model readiness, deployment, or performance from documentation or dependency installation alone. Do not change runtime/model code, weights, datasets, workflows, or device configuration as part of standards adoption.

Existing README.md and docs/CROSS_DEVICE_RUNTIME.md provide project-specific context; reconcile claims with current source, tests, and runtime evidence.

## Required adoption sequence

1. Review and merge the canonical standards proposal before calling these links an approved policy.
2. Review this repository's AI entrypoint and project-specific documentation for contradictions.
3. Add structured state or verification records only when their source evidence, owner, schema, and update process are known.
4. Validate links and any structured data; run relevant checks and record the actual results.
5. Mark **ADOPTED** only after the local guidance is merged; mark **VERIFIED** only after relevant checks pass; mark **ENFORCED** only after controls are configured and tested.
6. Keep implementation/UI changes outside this documentation-only adoption PR.

## Current evidence

- The AI entrypoint and this adoption note are proposed in the same branch.
- Canonical standards are still pending review/merge.
- Automated enforcement, schema validation in CI, and downstream runtime behavior have **not** been verified by this document.
