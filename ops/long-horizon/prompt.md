# ExecPlan Prompt: v0.6-v1.0 Proof-Surface Maturation

You are maintaining `ii-logos-spacetime-derivation`, a public verification and
explainer companion to *A Brief Derivation of Spacetime*.

## Mission

Mature the repository from the current v0.5 proof surface toward a disciplined
v1.0 release. The work must promote only conservative algebraic or arithmetic
bridge packets backed by Lean declarations and deterministic computed artifacts.

The current v0.5 public truth status remains active until later proof work lands
and passes the full validation gate.

## Hard Requirements

- Use Lean as proof authority after `lake build` succeeds.
- Use SymPy as a computed companion, not proof authority.
- Keep the four public tags only: `Lean-proved`, `Computed here`,
  `Imported theorem`, and `Interpretation`.
- Preserve the lightweight `Mat2` / `Vec2` style unless a later milestone
  explicitly justifies migration.
- Do not add Harmonic configuration, secrets, tokens, or CI dependency.
- Do not add an app, chatbot, or GitHub Pages companion during this program.

## Boundary Rule

Physical claims involving light-cone geometry, light rays, horizons, redshift,
arrow orientation, the shared-sign thesis, `t > 0`, `c > 0`, or `PHYS-01` must
stay below proof status until they have separate theorem support and synchronized
truth surfaces.

## Target Proof Packets

- `ST-09-SPLIT-CONE`: algebraic cone predicate around `splitQuadratic`.
- `ST-10-LAMBDA-GENERAL-SIGN`: safe general-dimensional Lambda arithmetic with
  explicit dimension assumptions.
- `ST-11-BRACKET-SURFACE`: strengthened symbolic constant-curvature bracket
  surface without claiming full Lie-algebra exhaustiveness.

## Process Directive

Start by reading `ops/long-horizon/plans.md`. Do not begin proof or artifact
implementation until that file is coherent, current, and specific enough for
another agent to resume the work.
