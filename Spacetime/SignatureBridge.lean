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

/-- Safe general-dimensional symbolic relation with explicit dimension and sign assumptions. -/
theorem cosmologicalFromCurvature_general (d : Dim) (lam : CurvatureSign) :
    cosmologicalFromCurvature d lam = (((d : ℝ) - 1) * ((d : ℝ) - 2) * lam) / 2 := by
  rfl

/-- For explicit positive dimensions, nonnegative curvature implies nonnegative symbolic Lambda. -/
theorem cosmologicalFromCurvature_nonneg_of_nonneg {d : Dim} (hd : 3 ≤ d) {lam : CurvatureSign}
    (h : 0 ≤ lam) :
    0 ≤ cosmologicalFromCurvature d lam := by
  rw [cosmologicalFromCurvature_general]
  have hd' : (3 : ℝ) ≤ d := by exact_mod_cast hd
  have h1 : 0 ≤ (d : ℝ) - 1 := by nlinarith
  have h2 : 0 ≤ (d : ℝ) - 2 := by nlinarith
  have hprod : 0 ≤ ((d : ℝ) - 1) * ((d : ℝ) - 2) := mul_nonneg h1 h2
  have hden : 0 < (2 : ℝ) := by norm_num
  have hmul : 0 ≤ (((d : ℝ) - 1) * ((d : ℝ) - 2) * lam) := mul_nonneg hprod h
  exact div_nonneg hmul (le_of_lt hden)

/-- For explicit positive dimensions, positive symbolic Lambda follows from positive curvature. -/
theorem cosmologicalFromCurvature_positive_of_positive {d : Dim} (hd : 3 ≤ d) {lam : CurvatureSign}
    (h : 0 < lam) :
    0 < cosmologicalFromCurvature d lam := by
  rw [cosmologicalFromCurvature_general]
  have hd' : (3 : ℝ) ≤ d := by exact_mod_cast hd
  have h1 : 0 < (d : ℝ) - 1 := by nlinarith
  have h2 : 0 < (d : ℝ) - 2 := by nlinarith
  have hprod : 0 < ((d : ℝ) - 1) * ((d : ℝ) - 2) := mul_pos h1 h2
  have hden : (0 : ℝ) < 2 := by norm_num
  have hmul : 0 < ((d : ℝ) - 1) * ((d : ℝ) - 2) * lam := mul_pos hprod h
  exact (div_pos hmul hden)

end Spacetime
