# Meta Integration & Automated Context Sharing

> **Status:** PROPOSED / DESIGN SPECIFICATION  
> **Repository:** AMRHZ-AI-13  
> **Owner authority:** AMRHZ human owner  
> **Created:** 2026-10-31  
> **Implementation state:** NOT IMPLEMENTED / NOT VERIFIED

This document defines a safe, provider-aware integration direction for Meta technologies and a user-controlled context-sharing bridge between AMRHZ and approved AI providers.

It is an architecture contract, not proof that Meta AI, ChatGPT, or any other provider is already connected.

---

## 1. Objective

Enable AMRHZ to prepare a portable, structured context package that can be shared with a selected AI provider or service when the owner explicitly authorizes that transfer.

The design must support:

- Meta as a potential model provider through its documented Model API.
- Meta AI Connectors as a potential way for Meta AI to call approved AMRHZ service capabilities.
- A provider-neutral context format that can later support other AI systems.
- Explicit consent, narrow scope, provenance, expiry, revocation, and an auditable transfer record.
- Manual export first; automated transfer only after the target API, authentication, permissions, and data handling are verified.

## 2. What “Meta integration” means

Treat these as separate integration tracks. They are not interchangeable.

### Track A — Meta Model API

Meta's developer documentation describes an HTTP Model API with bearer-token authentication and endpoints including Responses, Chat Completions, Messages, Files, and Models.

Potential AMRHZ use: call a supported Meta model from an AMRHZ-controlled backend through a provider adapter.

Boundaries:

- A Model API key is a server-side secret. Never put it in source code, browser bundles, logs, screenshots, or Git history.
- Use a server-side environment variable or approved secret manager.
- Do not assume that a Meta AI consumer-app account grants Model API access.
- Check current model availability, account eligibility, pricing, rate limits, terms, and data handling before enabling requests.
- Do not upload a user's full memory or conversation archive by default.

### Track B — Meta AI Connectors

Meta describes AI Connectors as a way to expose an existing service API as tools that Meta AI can call. The published onboarding information describes API registration, OAuth account linking, and developer-preview access.

Potential AMRHZ use: expose a small, permissioned AMRHZ API surface so Meta AI can request approved actions or context summaries.

Boundaries:

- Developer-preview availability is not a guarantee of acceptance, production access, or availability in every region/account.
- Connector calls must use scoped authorization and enforce AMRHZ permissions on the server.
- A connector does not automatically grant Meta AI unrestricted access to AMRHZ storage.
- Start with read-only, minimal-scope tools. Any write/action capability requires a separate approval design.
- Confirm current Meta requirements and review status before implementation.

### Track C — Context-sharing bridge

This is an AMRHZ-owned capability, independent of any one provider.

It prepares a context package, asks the owner to approve the destination and fields, then exports or transmits only the approved package through a verified integration.

It does **not** assume that ChatGPT or Meta AI exposes an API for reading the user's private chat history. Context must come from an authorized AMRHZ source or content explicitly supplied by the owner.

## 3. Target architecture

```text
AMRHZ KNOWLEDGE / PROJECT CONTEXT
              |
              v
     CONTEXT PACKAGE BUILDER
              |
              v
     CLASSIFICATION + FILTER
              |
              v
     OWNER CONSENT GATE
   (provider / purpose / fields /
    retention / expiry / revoke)
              |
       +------+------+
       |             |
       v             v
 MANUAL EXPORT   APPROVED API ADAPTERS
       |             |
       |       +-----+----------------+
       |       |                      |
       |       v                      v
       |  META MODEL API       META AI CONNECTOR
       |  (model calls)        (tool access)
       |       |                      |
       +-------+----------------------+
                       |
                       v
              TRANSFER RECEIPT
                       |
                       v
              EVIDENCE / AUDIT LOG
```

The context package builder and consent gate remain under AMRHZ control. Provider adapters must not bypass them.

## 4. Context package contract

Use a versioned, provider-neutral structure. Example:

```json
{
  "schema_version": "1.0",
  "package_id": "generated-unique-id",
  "created_at": "ISO-8601 timestamp",
  "owner_ref": "AMRHZ-controlled pseudonymous identifier",
  "purpose": "specific task approved by the owner",
  "destination": {
    "provider": "meta",
    "integration": "model-api-or-connector"
  },
  "expires_at": "ISO-8601 timestamp",
  "items": [
    {
      "id": "context-item-id",
      "type": "project-summary",
      "content": "minimum necessary approved context",
      "source_ref": "repository path, record ID, or owner-supplied source",
      "verification_state": "verified-or-unverified",
      "sensitivity": "normal"
    }
  ],
  "consent": {
    "approved": true,
    "approved_at": "ISO-8601 timestamp",
    "scope": ["read:project-summary"],
    "revocable": true
  }
}
```

This is an illustrative contract only. The schema must be validated and finalized before production use. Do not put real personal data, tokens, passwords, or private keys in example fixtures.

Required package properties:

- **Purpose-bound:** one stated task, not blanket permission.
- **Destination-bound:** identify the exact provider and integration.
- **Minimal:** include only information needed for that task.
- **Traceable:** every item has a source reference and verification state.
- **Time-limited:** packages expire; persistent provider-side retention must be disclosed separately.
- **Revocable:** stop future transfers and revoke linked authorization where supported.
- **Versioned:** schema changes require compatibility tests.

## 5. Consent and data boundaries

No transfer occurs until the owner has approved all of the following:

1. Destination provider and integration.
2. Purpose of the transfer.
3. Exact context categories or items.
4. Whether the transfer is one-time or recurring.
5. Expiry and retention expectations.
6. Whether the provider may retain the submitted data under its current terms.

Default-deny rules:

- No silent background sharing.
- No blanket sync of all chats, memory, files, or repository contents.
- No contact-list sharing, phone numbers, email addresses, precise location, credentials, authentication tokens, or private keys by default.
- No health, financial, identity, or other sensitive personal data unless a separate lawful, explicit, narrowly scoped process is designed and approved.
- No onward sharing to another provider unless the owner separately approves it.
- No training-use or retention claims unless supported by the provider's current published terms and settings.
- No use of provider output as verified AMRHZ knowledge without provenance and review.

Consent must be recorded as an auditable event. A UI toggle alone is not sufficient evidence of a completed transfer.

## 6. Identity and account linking

Use a provider-supported OAuth or equivalent account-linking flow where available.

- The user authenticates directly with the provider.
- AMRHZ stores only the minimum token material required, encrypted at rest and never exposed to the client.
- Request the narrowest available scopes.
- Validate state/nonce and redirect URI where applicable.
- Support disconnect, token revocation, and local credential deletion.
- Never request or store the user's provider password.
- Never share API keys between unrelated accounts or teams.

If a provider does not offer a supported account-linking or API flow for the intended operation, mark that capability **UNAVAILABLE / MANUAL ONLY**. Do not automate browser scraping or imitate private endpoints.

## 7. Provider capability states

Every provider capability must use an evidence-backed state:

| State | Meaning |
|---|---|
| NOT_CONFIGURED | No credentials or integration setup exists |
| AVAILABLE_FOR_REVIEW | Official API/docs exist; eligibility and access are not yet confirmed |
| CONNECTED | Supported authentication completed and connection check passed |
| ERROR | A connection attempt failed; retain a safe diagnostic |
| UNKNOWN | Evidence is insufficient |
| BLOCKED | Provider access, policy, eligibility, or technical constraint prevents use |
| VERIFIED | A scoped end-to-end test passed with a recorded receipt |

A configured key alone does not prove that a provider is connected. A successful health check alone does not prove context transfer works.

## 8. Transfer lifecycle

```text
OWNER REQUEST
    -> BUILD MINIMAL PACKAGE
    -> CLASSIFY / FILTER
    -> SHOW DESTINATION + SCOPE
    -> OWNER APPROVAL
    -> VALIDATE CONSENT + AUTH
    -> TRANSFER
    -> RECORD RECEIPT
    -> VERIFY RESULT
    -> EXPIRE / REVOKE
```

For recurring automation, repeat the consent check at every scheduled transfer. If scope, destination, data classification, or provider terms change, pause and request approval again.

A transfer receipt should record:

- Package ID and schema version.
- Provider and integration identifier.
- Purpose and approved scope.
- Timestamp and outcome.
- Item IDs or safe hashes, not unnecessary raw content.
- Provider request/response identifiers where safe.
- Error category if unsuccessful.
- Consent reference and expiry.

Never log secrets or full sensitive payloads.

## 9. Initial implementation sequence

### Phase 0 — Documentation and capability verification

- [x] Record the integration tracks and security boundaries.
- [ ] Confirm Meta Model API account eligibility and current model availability.
- [ ] Confirm Meta AI Connector developer-preview access and onboarding requirements.
- [ ] Decide which track is the first useful AMRHZ use case.
- [ ] Review provider terms, privacy, retention, and regional availability.

### Phase 1 — Manual context package

- [ ] Define and validate the JSON schema.
- [ ] Build a local package preview and redaction step.
- [ ] Export a user-approved package as a file or copyable text.
- [ ] Record a local export receipt.
- [ ] Test expiry and revocation semantics.

This phase must not require Meta credentials or transmit data externally.

### Phase 2 — Meta Model API adapter

- [ ] Implement server-side adapter only after eligibility and terms are checked.
- [ ] Store credentials outside Git and client-side code.
- [ ] Add minimal request/response handling, timeouts, rate-limit handling, and safe errors.
- [ ] Test with synthetic, non-sensitive context.
- [ ] Verify provider response and transfer receipt.

### Phase 3 — Meta AI Connector

- [ ] Apply for / confirm developer-preview access.
- [ ] Define a minimal read-only AMRHZ API.
- [ ] Add OAuth account linking and scoped authorization.
- [ ] Test only approved tools and context categories.
- [ ] Review access logs, revoke access, and test denied requests.

### Phase 4 — Controlled automation

- [ ] Enable recurring transfers only for a specifically approved use case.
- [ ] Re-check consent, scope, expiry, and destination on every run.
- [ ] Add pause, disconnect, and revocation controls.
- [ ] Verify idempotency and duplicate-transfer handling.
- [ ] Publish an evidence-backed capability state.

No later phase is implied to be complete by this document.

## 10. Acceptance criteria

The integration is not VERIFIED until all applicable checks pass:

- An unapproved transfer is denied.
- A package contains only selected, permitted fields.
- The destination and purpose are visible before approval.
- Expired or revoked consent blocks subsequent transfers.
- A provider error does not silently retry with broader permissions.
- Secrets do not appear in Git, client bundles, logs, or receipts.
- Every successful transfer has a traceable receipt.
- Provider-side retention and deletion limits are accurately disclosed.
- A disconnect stops future requests and revokes tokens where supported.
- Tests use synthetic data until the security review approves real data.

## 11. Known limitations and open decisions

- Meta AI Connectors are documented as developer preview; access and production readiness must be confirmed.
- Meta Model API availability and model list can change; check current documentation and account access before implementation.
- A general-purpose API for exporting private ChatGPT or Meta AI consumer-chat histories has not been established by this specification.
- Provider APIs do not imply shared memory between assistants. AMRHZ must remain the source of truth for any context it owns.
- No actual Meta account is linked, no credentials are configured, and no external transfer has been tested as part of this documentation change.

Open owner decisions:

1. First target: Meta Model API, Meta AI Connector, or manual context-package export.
2. First permitted context category: project summary, architecture decisions, or another narrowly defined category.
3. Whether the first version is one-time export only (recommended) or later recurring automation.

## 12. Official references

- [Meta AI Connectors](https://dev.meta.ai/products/connectors) — connector concept, API onboarding, OAuth account linking, developer-preview access.
- [Meta for Developers — Wearables FAQ](https://developers.meta.com/wearables/faq/) — describes Meta AI Connector availability across Meta AI surfaces.
- [Meta Model API Reference](https://dev.meta.ai/docs/api-reference) — API base, authentication, and resource endpoints.
- [Meta Model API Responses](https://dev.meta.ai/docs/protocols/responses) — request/context handling options.

Provider documentation and terms must be rechecked at implementation time.

---

## Change record

| Date | Change | Evidence | State |
|---|---|---|---|
| 2026-10-31 | Added initial Meta integration and context-sharing design specification | Official Meta developer documentation reviewed; no live integration test performed | DOCUMENTED / PROPOSED |
