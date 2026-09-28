# Security Policy

Profile Verse cards are **pure static SVG** generated at build time by GitHub Actions. There is no server, no database, and no runtime API call — nothing is executed when someone views your README.

## Reporting a Vulnerability

Even so, SVG is a powerful format. If you find a way to abuse a generated card (e.g., script injection through user input like `name`, `phrases`, or `badges` reaching the SVG), please **do not open a public issue**.

Report it privately to the maintainer via [GitHub's private vulnerability reporting](https://github.com/Morningstar202604/profile-cards/security/advisories) for this repository.

Please include:

- A minimal reproduction (the exact input + the generated SVG)
- Why it is exploitable and its impact
- Suggested fix, if you have one

We aim to acknowledge reports within 3 business days.

## Supported versions

| Version | Supported |
| ------- | --------- |
| main    | ✅        |
| v1      | ✅        |
