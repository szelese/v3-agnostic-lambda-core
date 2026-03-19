# v3-agnostic-lambda-core

> ⚠️ This project is currently under active development. Documentation will be expanded over time.

## Core Contract

The core logic is fully decoupled from the Lambda handler.
Any function that satisfies this contract can be used as the core:

- **Input:** `dict` (parsed from the Lambda event body)
- **Output:** JSON-serializable `dict`
- **Exceptions:** do not handle in core — the handler catches all exceptions and returns HTTP 500

AWS Lambda boilerplate in Python with an environment-agnostic core architecture.