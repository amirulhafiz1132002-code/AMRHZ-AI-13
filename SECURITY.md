# Security Policy

## Current status

AMRHZ AI is a development-stage project. Security controls, runtime authentication, deployment exposure, and historical secret removal must be verified for each relevant environment; this file does not claim the application is fully secured.

## Reporting a vulnerability

Please do not publish live credentials, personal information, or an unpatched exploitable detail in a public issue. Use GitHub's private vulnerability reporting feature if enabled for this repository. Otherwise, contact the maintainer privately through an available GitHub contact channel with the affected component, impact, reproduction conditions, and redacted evidence.

## Credential handling

- Never commit real API keys, tokens, passwords, or local environment files.
- Use `Final.env.example` as a sanitized template and keep the actual `Final.env` local.
- If a committed value is a real credential, revoke or rotate it with its provider.
- Removing a file from the latest tree does not erase previous commits, forks, caches, clones, or deployment copies.
- Do not claim historical cleanup is complete until the relevant history and copies have been assessed.

## Configuration cleanup record

See [Security and Environment Configuration](docs/SECURITY-CONFIGURATION.md) for the scope and remaining verification boundaries of the environment-file cleanup.

## Build-in-public principle

Keep bugs, failed checks, and engineering lessons visible when useful. Do not expose real credentials or unnecessary personal data as a substitute for transparency. A fix is considered verified only when relevant evidence supports that conclusion.
