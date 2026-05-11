import Spacetime.Basic

/-!
# Spacetime.TimeEvolutionMatrix

The core v0 theorem target: the exact 2x2 matrix on each `(Kᵢ,Pᵢ)` plane.

`A(lam) = [[0, -lam], [-1, 0]]`.
-/

namespace Spacetime

/-- The time-evolution matrix `A(lam)` on a `(Kᵢ,Pᵢ)` plane. -/
def timeEvolutionMatrix (lam : CurvatureSign) : Mat2 :=
  ⟨0, -lam, -1, 0⟩

/-- `trace(A(lam)) = 0`. -/
theorem trace_zero (lam : CurvatureSign) :
    (timeEvolutionMatrix lam).trace = 0 := by
  simp [timeEvolutionMatrix, Mat2.trace]

/-- `det(A(lam)) = -lam`. -/
theorem det_eq_neg_lambda (lam : CurvatureSign) :
    (timeEvolutionMatrix lam).det = -lam := by
  simp [timeEvolutionMatrix, Mat2.det]

/-- The characteristic polynomial is `x² - lam`. -/
theorem char_poly (lam x : CurvatureSign) :
    (timeEvolutionMatrix lam).charpoly x = x ^ 2 - lam := by
  simp [Mat2.charpoly, timeEvolutionMatrix, Mat2.trace, Mat2.det]
  ring

/-- `A(lam)^2 = lamI`. -/
theorem square_eq_lambda_identity (lam : CurvatureSign) :
    Mat2.mul (timeEvolutionMatrix lam) (timeEvolutionMatrix lam) = Mat2.scalar lam := by
  simp [Mat2.mul, Mat2.scalar, timeEvolutionMatrix]

/-- At `lam = 0`, the square vanishes. -/
theorem zero_branch_square_zero {lam : CurvatureSign} (h : lam = 0) :
    Mat2.mul (timeEvolutionMatrix lam) (timeEvolutionMatrix lam) = Mat2.zero := by
  rw [square_eq_lambda_identity, h]
  rfl

/-- For positive `lam`, `det(A(lam)) < 0`. -/
theorem positive_branch_det_negative {lam : CurvatureSign} (h : lam > 0) :
    (timeEvolutionMatrix lam).det < 0 := by
  rw [det_eq_neg_lambda]
  linarith

/-- For negative `lam`, `det(A(lam)) > 0`. -/
theorem negative_branch_det_positive {lam : CurvatureSign} (h : lam < 0) :
    (timeEvolutionMatrix lam).det > 0 := by
  rw [det_eq_neg_lambda]
  linarith

end Spacetime
