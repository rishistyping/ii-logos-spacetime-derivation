import Lake
open Lake DSL

package «spacetime-skeletal» where
  leanOptions := #[
    ⟨`pp.unicode.fun, true⟩,
    ⟨`autoImplicit, false⟩
  ]

require mathlib from git
  "https://github.com/leanprover-community/mathlib4" @ "v4.7.0"

@[default_target]
lean_lib Spacetime
