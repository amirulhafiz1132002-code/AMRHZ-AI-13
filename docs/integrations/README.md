# AMRHZ AI Integration Context — AI Agent Entry Point

> **Document type:** AI-readable integration context / operational reference  
> **Project:** AMRHZ AI ♾️13  
> **Owner authority:** AMRHZ human owner  
> **Status:** DOCUMENTED / PROPOSED  
> **Last updated:** 2026-10-31  
> **Implementation state:** No live Meta integration or automated context transfer has been verified.

This file is the entry point for AI agents, developers, reviewers, and contributors working on provider integrations and cross-AI context sharing in AMRHZ-AI-13.

It is designed to reduce repeated explanations while preserving accurate project state, source provenance, privacy, and human control.

---

## 0. Agent Start Protocol — READ FIRST

Before proposing or performing integration work:

1. Read this file completely.
2. Read [META-INTEGRATION-AND-CONTEXT-SHARING.md](./META-INTEGRATION-AND-CONTEXT-SHARING.md).
3. Inspect the current repository, branch, relevant source files, tests, configuration, and deployment state.
4. Distinguish documented design from implemented code and verified behavior.
5. Identify the smallest next task and its dependencies.
6. Do not change files, credentials, external accounts, provider settings, or deployments without explicit owner authorization.
7. Report inspected, changed, tested, not tested, and unknown states separately.

**Never infer a live connection from a README, design diagram, provider name, configured-looking UI, or the presence of an API key.**

## 1. Mission

Build an AMRHZ-controlled, provider-neutral integration layer that can exchange explicitly approved context with external AI systems.

The intended outcome is continuity across AI tools without requiring the owner to repeatedly reconstruct project context, while ensuring:

- Human ownership and decision authority.
- Explicit, purpose-bound consent.
- Minimal and classified context transfer.
- Source provenance and verification status.
- Provider-specific authentication and permission scopes.
- Expiry, revocation, disconnect, and auditability.
- Honest reporting of capability and runtime state.

The goal is **controlled context portability**, not unrestricted synchronization of every conversation or account.

## 2. System Identity and Responsibility

AMRHZ AI is the parent intelligence ecosystem. AP1 is the orchestration layer/product family. External AI providers are independent systems that may be used as model providers, reviewers, or approved tool clients.

| Component | Responsibility |
|---|---|
| AMRHZ AI | Owns the architecture, knowledge contracts, and integration policy |
| AMRHZ Knowledge Core | Holds authorized project context and provenance records |
| Context Package Builder | Selects and serializes approved context |
| Classification / Filter | Removes disallowed, unnecessary, or sensitive fields |
| Consent Gate | Requires owner approval for provider, purpose, scope, and duration |
| Provider Adapter | Implements a provider's documented API |
| Connector API | Exposes only explicitly permitted AMRHZ tools/data |
| Evidence Ledger | Records actions, results, verification, and unknowns |
| AP1 Orchestrator | Coordinates proposals, approvals, execution, and verification |
| Human Owner | Approves permissions, external effects, and architectural decisions |

No provider adapter may bypass the Context Package Builder, classification, consent, or evidence controls.

## 3. Integration Vocabulary

Do not conflate these separate concepts:

### 3.1 Model provider integration

AMRHZ sends a request to a provider's documented model API and receives a model response.

Example: an AMRHZ backend calls an available Meta model through an approved API.

This does not automatically connect Meta AI consumer chat, ChatGPT chat history, or any user's private account memory.

### 3.2 AI connector / tool integration

An external AI system calls a documented AMRHZ service endpoint through an approved connector and account-linking flow.

Example: an external AI asks an AMRHZ API for a permitted project summary.

A connector is not unrestricted access to AMRHZ files or memory.

### 3.3 Context package export

AMRHZ prepares a portable, provider-neutral package for the owner to inspect and share manually or through an approved adapter.

This is the recommended first implementation because it can be tested without external credentials or transmission.

### 3.4 Automated context sharing

A verified adapter transfers a specific approved package to a specific destination under a defined schedule or event trigger.

Automation must re-check consent, destination, scope, expiry, and policy on every transfer. A previous approval is not blanket permission for all future data.

## 4. Provider Tracks

### Meta Model API

**Intended role:** optional model provider.

**Possible operation:** AMRHZ server sends approved prompt/context to a supported Meta model endpoint.

**Prerequisites to verify at implementation time:**

- Developer account and API eligibility.
- Current model availability and API version.
- Authentication method and secret storage.
- Rate limits, pricing, regional access, and terms.
- Data retention and provider-side processing policies.
- Successful synthetic-data request and response test.

**Current state:** AVAILABLE FOR REVIEW / NOT CONNECTED.

### Meta AI Connectors

**Intended role:** optional external AI client of AMRHZ tools.

**Possible operation:** Meta AI calls a narrowly scoped AMRHZ service using the provider-supported connector and account-linking flow.

**Prerequisites to verify at implementation time:**

- Current developer-preview eligibility and access.
- API registration and connector requirements.
- OAuth/account-linking requirements and scopes.
- Review, publishing, and regional availability constraints.
- Server-side authorization and access-control tests.
- Revocation and disconnect behavior.

**Current state:** AVAILABLE FOR REVIEW / ACCESS NOT CONFIRMED.

### Other AI providers

The architecture should remain provider-neutral. A provider must be added only through documented, supported interfaces and a reviewed adapter. Do not claim cross-provider support until each adapter is implemented and independently tested.

**Current state:** NOT CONFIGURED unless a repository-backed integration record proves otherwise.

## 5. Context Package Contract

All providers should receive a normalized, versioned package rather than direct unrestricted access to raw memory.

Minimum conceptual fields:

- `schema_version`
- `package_id`
- `created_at`
- `purpose`
- `destination.provider`
- `destination.integration`
- `expires_at`
- `items[]`
- `items[].type`
- `items[].content`
- `items[].source_ref`
- `items[].verification_state`
- `items[].sensitivity`
- `consent.approved`
- `consent.scope`
- `consent.approved_at`
- `consent.revocable`

The normative design and illustrative JSON are maintained in [META-INTEGRATION-AND-CONTEXT-SHARING.md](./META-INTEGRATION-AND-CONTEXT-SHARING.md).

Do not treat the illustrative example as a production-validated JSON Schema. Schema validation, version compatibility, and negative tests are required before runtime adoption.

## 6. Data Classification and Default-Deny Policy

Every candidate context item must be classified before export.

Default-deny categories include:

- Passwords, API keys, OAuth tokens, private keys, recovery codes, and authentication secrets.
- Personal contact details and account identifiers not needed for the approved task.
- Precise location and private device/account metadata.
- Sensitive personal, health, financial, or identity information.
- Private conversations or files that have not been explicitly selected for the task.
- Third-party information without a valid basis and explicit authorization.

Do not include sensitive information merely because it exists in a connected source.

Use the minimum necessary context. Prefer summaries and source references over copying entire records.

Provider-side retention, deletion, training use, and onward sharing must be described only from current authoritative provider documentation and settings. Do not promise deletion from a provider when AMRHZ cannot enforce it.

## 7. Consent Model

Before every external transfer, the owner must be able to inspect:

1. Destination provider and integration.
2. Exact purpose.
3. Context items/categories.
4. One-time or recurring behavior.
5. Expiry and retention implications.
6. Whether the provider may retain or further process the data.

Consent must be explicit, recorded, scoped, and revocable for future transfers.

A consent record does not prove that a transfer occurred. A transfer receipt does not prove that the provider deleted data. Keep these as separate events.

For recurring automation, pause when destination, purpose, data scope, classification, or provider terms change and request renewed approval.

## 8. Identity, Authentication, and Authorization

- Prefer provider-supported OAuth/account linking where appropriate.
- Use the narrowest available scopes.
- Never request or store a provider account password.
- Keep secrets server-side and out of Git, client bundles, logs, test fixtures, screenshots, and generated documentation.
- Encrypt stored tokens and restrict access.
- Validate OAuth state, nonce, redirect URI, and token audience/issuer where applicable.
- Support disconnect and provider token revocation where supported.
- Enforce authorization on every server request; UI state is not an authorization boundary.
- If the provider has no supported API for the intended operation, use manual export or mark it unavailable. Do not scrape private endpoints or automate consumer interfaces as a substitute.

## 9. Evidence and Capability States

Use these exact states where applicable:

| State | Definition |
|---|---|
| UNKNOWN | Evidence is insufficient to determine capability or status |
| NOT_CONFIGURED | No credentials or setup exists |
| AVAILABLE_FOR_REVIEW | Official provider documentation exists; access and eligibility remain unconfirmed |
| DEVELOPMENT | Implementation work exists but is incomplete |
| PARTIAL | Some scoped behavior works; end-to-end acceptance is incomplete |
| CONNECTED | Supported authentication and connection check passed |
| VERIFIED | A defined end-to-end test passed with inspectable evidence |
| LIVE | The verified capability is operating in its intended environment |
| BLOCKED | Policy, eligibility, access, or technical constraints prevent progress |
| ERROR | An attempted operation failed; safe diagnostics are available |

State transitions require evidence. A key being present is not proof of connection. A successful API response is not proof that consent, filtering, expiry, and revocation work.

## 10. Transfer Lifecycle

```text
OWNER INTENT
  -> INSPECT SOURCES
  -> BUILD MINIMAL CONTEXT PACKAGE
  -> CLASSIFY AND FILTER
  -> SHOW DESTINATION / PURPOSE / SCOPE
  -> OWNER APPROVAL
  -> VALIDATE AUTHORIZATION
  -> TRANSFER THROUGH APPROVED ADAPTER
  -> RECORD RECEIPT
  -> VERIFY RESULT
  -> EXPIRE OR REVOKE
```

Each transfer receipt should contain package ID, schema version, destination, purpose, approved scope, timestamp, outcome, safe item identifiers/hashes, provider request ID where safe, and consent reference.

Never log raw secrets or unnecessary sensitive payloads.

## 11. Recommended Implementation Roadmap

### M0 — Context package specification

- Finalize a machine-readable JSON Schema.
- Define classification labels and validation rules.
- Define package preview and redaction behavior.
- Define consent record and transfer receipt schemas.

### M1 — Local/manual export

- Build package generation from explicitly selected AMRHZ sources.
- Preview exact content before export.
- Export JSON/Markdown without external network transfer.
- Record a local export receipt.
- Test default-deny, redaction, expiry metadata, and malformed package rejection.

### M2 — First provider adapter

Choose one provider and one narrow use case only after account eligibility, official API support, terms, and credentials are verified.

- Server-side adapter.
- Synthetic data only for initial testing.
- Timeouts, rate limits, safe errors, and request IDs.
- No broad memory sync.
- End-to-end evidence and cost tracking.

### M3 — Connector/tool access

- Expose only read-only, narrowly scoped tools initially.
- Add provider-supported account linking.
- Test unauthorized, expired, and revoked access.
- Review logs and data minimization.

### M4 — Recurring automation

- Add only for an owner-approved purpose.
- Revalidate consent and scope for every run.
- Add pause, disconnect, revocation, idempotency, and duplicate protection.
- Verify behavior under provider errors and policy changes.

No phase should be marked complete merely because documentation or a UI exists.

## 12. Mandatory Test Matrix

| Test | Expected result |
|---|---|
| No owner consent | Transfer denied |
| Wrong destination | Transfer denied |
| Expired consent | Transfer denied |
| Revoked consent | Future transfer denied |
| Disallowed field in package | Field rejected or redacted |
| Secret-like value detected | Export blocked or value redacted |
| Provider authentication failure | Safe error; no permission expansion |
| Provider rate limit | Bounded retry policy; no duplicate transfer |
| Provider response succeeds | Receipt created and response verified |
| Disconnect | Future requests stop; token revoked where supported |
| Unknown schema version | Package rejected safely |
| Missing source provenance | Item marked unverified or rejected by policy |

Tests must use synthetic, non-sensitive data until security review authorizes another dataset.

## 13. AI Agent Collaboration Protocol

AMRHZ uses a dual-contribution review process:

- **ChatGPT contribution:** primary architecture, repository audit, implementation assistance, and verification.
- **Meta AI contribution:** independent review, provider-specific critique, alternative design, and adversarial challenge.
- **Cross-review:** compare claims, evidence, gaps, and contradictions.
- **Owner decision:** AMRHZ decides scope, permissions, and whether implementation proceeds.

Meta AI must not be represented as having inspected a repository, executed code, or verified a system unless it actually did so and supplies inspectable evidence.

Do not force reviewer agreement. Preserve independent findings.

## 14. Repository and Change Boundaries

Before changing this integration area:

- Inspect current branch and working tree.
- Read the applicable root instructions and architecture standards if present.
- Inspect relevant files and tests.
- Identify whether a proposed file already exists.
- Avoid duplicating canonical standards from the architecture-core repository.
- Keep provider-specific implementation details here only when they are directly relevant to AMRHZ-AI-13.
- Cross-link canonical standards rather than copying them.
- Make minimal, scoped changes.
- Do not commit, push, merge, or deploy without explicit owner authorization.
- After changes, report exact files, commit/branch, checks run, checks not run, and remaining unknowns.

Preferred work sequence:

`AUDIT -> PRIORITIZE -> EXECUTE -> VERIFY`

## 15. Source of Truth and Conflict Resolution

Use the following evidence precedence:

1. Actual source code and runtime configuration for implementation state.
2. Tests and recorded execution output for tested behavior.
3. Provider's current official documentation for external API capabilities and constraints.
4. Deployment and service evidence for live state.
5. Version-controlled architecture documents for intended design and decisions.
6. AI-generated summaries as navigation aids only.

When sources conflict, report the conflict and inspect the higher-precedence source. Do not silently rewrite historical evidence or infer a successful state.

## 16. Current Verified Checkpoint

As of 2026-10-31:

- [x] Initial Meta integration and context-sharing design specification created.
- [x] Specification committed to branch `docs/meta-context-sharing-spec`.
- [x] The new specification was fetched from GitHub after creation.
- [ ] This AI context README has been created and verified.
- [ ] JSON Schema finalized and validated.
- [ ] Meta Model API account eligibility confirmed.
- [ ] Meta AI Connector access confirmed.
- [ ] Manual context package generator implemented.
- [ ] Any provider adapter implemented.
- [ ] External transfer tested.
- [ ] Automated recurring context sharing implemented.

**Current overall integration state: DOCUMENTED / PROPOSED — NOT CONNECTED — NOT VERIFIED — NOT LIVE.**

The completed documentation work must not be reported as a completed integration.

## 17. Canonical Document

Read the full implementation-oriented design here:

[Meta Integration & Automated Context Sharing](./META-INTEGRATION-AND-CONTEXT-SHARING.md)

This file is the AI entry point; the linked specification contains the detailed architecture, phased implementation plan, and acceptance criteria.

---

## Agent Response Format

For every substantial task in this area, report:

- **Intent:** what was requested.
- **Inspected:** files, branch, provider documentation, and runtime state actually checked.
- **Baseline:** what existed before changes.
- **Plan:** smallest proposed change.
- **Authorization:** exact scope approved by the owner.
- **Changed:** exact files and commits.
- **Verified:** commands/tests/API checks actually performed and their outputs.
- **Not verified:** relevant checks not performed.
- **Unknown / blocked:** unresolved questions or dependencies.
- **Next decision:** one clear owner decision, if needed.

> **Core invariant:** REAL STATE > UI SIMULATION · EVIDENCE > CLAIM · HUMAN INTENTION > AI ASSUMPTION · VERIFICATION > BLIND TRUST.
