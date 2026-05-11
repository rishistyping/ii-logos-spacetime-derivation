import Spacetime.Basic

/-!
# Spacetime.ConstantCurvature

A narrow scaffold for the paper's constant-curvature translation bracket
surface.  This is a model of the algebraic form `[P_a,P_b] = lamJ_ab`, not a
full Lie-algebra exhaustiveness theorem.
-/

namespace Spacetime

/-- Symbolic generators used by the skeletal bracket surface. -/
inductive Generator where
  | J (a b : Nat)
  | P (a : Nat)
  deriving Repr, DecidableEq

/-- A single symbolic bracket term: coefficient times generator. -/
structure BracketTerm where
  coeff : ℝ
  gen : Generator

/-- Skeletal constant-curvature translation bracket `[P_a,P_b] = lamJ_ab`. -/
def translationBracket (a b : Nat) (lam : CurvatureSign) : BracketTerm :=
  ⟨lam, Generator.J a b⟩

/-- The bracket coefficient is exactly the curvature parameter. -/
theorem translationBracket_coeff (a b : Nat) (lam : CurvatureSign) :
    (translationBracket a b lam).coeff = lam := by
  rfl

/-- The bracket lands in the symbolic rotation generator indexed by `(a,b)`. -/
theorem translationBracket_generator (a b : Nat) (lam : CurvatureSign) :
    (translationBracket a b lam).gen = Generator.J a b := by
  rfl

/-- Bracket coefficient scales linearly in the curvature parameter. -/
theorem translationBracket_scale (a b : Nat) (lam₁ lam₂ : CurvatureSign) :
    translationBracket a b (lam₁ + lam₂) =
      ⟨(translationBracket a b lam₁).coeff + (translationBracket a b lam₂).coeff,
        (translationBracket a b (lam₁ + lam₂)).gen⟩ := by
  rfl

/-- Zero-curvature translation bracket still stays in the symbolic `J_ab` family. -/
theorem translationBracket_zero (a b : Nat) :
    translationBracket a b 0 = ⟨0, Generator.J a b⟩ := by
  simp [translationBracket]

/-- Generator type and branch are fixed once indices are fixed. -/
theorem translationBracket_stable_structure (a b : Nat) (lam : CurvatureSign) :
    (translationBracket a b lam).gen = Generator.J a b ∧
      (translationBracket a b lam).coeff = lam := by
  constructor <;> simp [translationBracket]

end Spacetime
