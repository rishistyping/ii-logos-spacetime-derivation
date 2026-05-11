import Spacetime.Basic

/-!
# Spacetime.SignatureBridge

Symbolic bridge surfaces for the relation between curvature and the
cosmological constant.  Geometric compactness and Wick-rotation readings stay
outside the v0 proof authority.
-/

namespace Spacetime

/-- Descriptive signature models used by the explainer surfaces. -/
inductive SignatureModel where
  | euclideanSphere
  | lorentzianHyperboloid
  deriving Repr, DecidableEq

/-- Symbolic relation `Λ = 1/2 (d-1)(d-2) lam`. -/
noncomputable def cosmologicalFromCurvature (d : Dim) (lam : CurvatureSign) : ℝ :=
  (((d : ℝ) - 1) * ((d : ℝ) - 2) * lam) / 2

/-- In four spacetime dimensions, the symbolic relation becomes `Λ = 3lam`. -/
theorem cosmologicalFromCurvature_four (lam : CurvatureSign) :
    cosmologicalFromCurvature 4 lam = 3 * lam := by
  norm_num [cosmologicalFromCurvature]
  ring

/-- In four spacetime dimensions, positive curvature gives positive symbolic Lambda. -/
theorem cosmologicalFromCurvature_four_positive {lam : CurvatureSign} (h : 0 < lam) :
    0 < cosmologicalFromCurvature 4 lam := by
  rw [cosmologicalFromCurvature_four]
  nlinarith

end Spacetime
