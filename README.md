# Michina: Integ test framework for LLMs
This is an example project.

## Setup
`poetry run python -m pytest tests/`

## Github Actions integration
The Michina Github action will run the test to make sure your new prompts pass checks.

1. In your Github repository, under Settings>Security>Secrets and variables, add `OPENAI_API_KEY` as a Repository secret.
2. Profit.
