import Spacetime.TimeEvolutionMatrix

/-!
# Spacetime.SignVerdict

Narrow algebraic sign-regime boundary.  These definitions deliberately stop
short of the full physical sign thesis.
-/

namespace Spacetime

/-- Algebraic marker for the hyperbolic branch: negative determinant. -/
def HyperbolicAlgebraic (lam : CurvatureSign) : Prop :=
  (timeEvolutionMatrix lam).det < 0

/-- Algebraic marker for the parabolic branch: square-zero at `lam = 0`. -/
def ParabolicAlgebraic (lam : CurvatureSign) : Prop :=
  Mat2.mul (timeEvolutionMatrix lam) (timeEvolutionMatrix lam) = Mat2.zero

/-- Algebraic marker for the elliptic explainer branch: positive determinant and zero trace. -/
def EllipticAlgebraic (lam : CurvatureSign) : Prop :=
  (timeEvolutionMatrix lam).det > 0 ∧ (timeEvolutionMatrix lam).trace = 0

/-- Positive branch satisfies the algebraic hyperbolic marker. -/
theorem positiveBranch_hyperbolicAlgebraic {lam : CurvatureSign} (h : lam > 0) :
    HyperbolicAlgebraic lam := by
  exact positive_branch_det_negative h

/-- Zero branch satisfies the algebraic parabolic marker. -/
theorem zeroBranch_parabolicAlgebraic {lam : CurvatureSign} (h : lam = 0) :
    ParabolicAlgebraic lam := by
  exact zero_branch_square_zero h

/-- Negative branch satisfies the algebraic elliptic marker. -/
theorem negativeBranch_ellipticAlgebraic {lam : CurvatureSign} (h : lam < 0) :
    EllipticAlgebraic lam := by
  constructor
  · exact negative_branch_det_positive h
  · exact trace_zero lam

end Spacetime
