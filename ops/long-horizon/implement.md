# ExecPlan Implementation Contract

This file defines how Codex should execute the v0.6-v1.0 program.

## Operating Rule

Work milestone by milestone from `ops/long-horizon/plans.md`. Do not stop after
each milestone for confirmation unless there is a real blocker, a truth-boundary
ambiguity, or a user instruction conflict.

## Required Workflow

1. Re-read `prompt.md`, `plans.md`, `implement.md`, and `documentation.md`
   before resuming a long-running session.
2. Start each milestone by checking `git status --short --branch`.
3. Keep edits scoped to the milestone.
4. Prefer targeted Lean or Python checks while developing.
5. Run the full validation gate before commit.
6. Update documentation and truth surfaces before staging.
7. Commit only when the worktree reflects a coherent milestone.

## Validation Discipline

- For proof work, `lake build` and the proof-hole scan are mandatory.
- For artifact work, regenerate artifacts and require no drift after generation.
- For bug fixes, add or identify a failing targeted check first when practical.
- For documentation-only work, run `git diff --check`, the truth-boundary scan,
  and the full local gate unless the user explicitly requests a lighter pass.

## Completion Criteria

A milestone is complete only when:

- intended files are updated;
- public truth surfaces agree;
- no physical-boundary claim is promoted accidentally;
- local validation passes;
- GitHub Actions are green after push when publishing is part of the task.

## Merge Discipline

- Use `codex/` branch names for scoped work.
- Prefer feature branches for proof-surface changes.
- Move `main` only after validation is green.
- Create release tags only from a green `main`.
