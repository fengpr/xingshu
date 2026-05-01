---
name: karpathy-guidelines
description: Follow Andrej Karpathy's coding philosophy and best practices. Use this skill when writing, reviewing, or refactoring code to enforce simple design, deep understanding, minimal changes, and explicit assumptions. Use it to guide implementation decisions, keep code readable, and reduce unnecessary complexity.
license: MIT
---

Use this skill to apply Andrej Karpathy's coding principles to the current task.

# Guidelines

## Keep It Simple

- Write code as simple as possible.
- Prefer explicitness over cleverness.
- Minimize dependencies and moving parts.
- Avoid premature abstraction.

## Understand Existing Code First

- Read nearby code before making changes.
- Match local patterns unless there is a strong reason not to.
- Preserve consistency in style and architecture.
- Avoid introducing a new pattern when an existing one already works.

## Make the Smallest Effective Change

- Solve the task with the least invasive change that fully addresses it.
- Avoid broad refactors unless the task clearly requires them.
- Do not silently fix unrelated issues in the same change.
- Keep diffs easy to review.

## Be Honest About Uncertainty

- State assumptions explicitly.
- If you are unsure, say so and explain what would confirm it.
- Distinguish facts from guesses.
- Prefer verification over confident improvisation.

## Communicate Clearly

- Explain what changed and why in plain language.
- Mention tradeoffs when they matter.
- Keep comments and docs concise and useful.
- Avoid jargon when simpler wording works.

## Prefer Working Code Over Theoretical Perfection

- Optimize for code that is correct, understandable, and maintainable.
- Do not over-engineer for hypothetical future cases.
- When multiple solutions are valid, choose the one that is easiest to reason about.
- Leave the codebase slightly better, but stay focused on the task.

## When Reviewing or Refactoring

- Identify unnecessary complexity and remove it carefully.
- Collapse abstractions that do not pay for themselves.
- Rename only when it improves clarity.
- Preserve behavior unless behavior change is part of the task.

## Output Style

- Keep implementation pragmatic.
- Keep explanations short and direct.
- Prefer concrete recommendations over broad theory.

