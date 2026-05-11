import Spacetime.EigenDirections

/-!
# Spacetime.NullBridge

Algebraic split-null bridge for the v0.5 theorem surface.
This file proves only that the two v0.3 eigendirections vanish against the
split quadratic form `k^2 - lambda p^2`. Physical readings remain outside this
Lean surface.
-/

namespace Spacetime

/-- The split quadratic form on `(K_i, P_i)` coordinates. -/
noncomputable def splitQuadratic (lam : CurvatureSign) (v : Vec2) : ℝ :=
  v.k ^ 2 - lam * v.p ^ 2

/-- Predicate wrapper for vectors annihilated by the split quadratic form. -/
def IsSplitNull (lam : CurvatureSign) (v : Vec2) : Prop :=
  splitQuadratic lam v = 0

/-- The split quadratic form is homogeneous of degree two. -/
theorem splitQuadratic_scale (lam r : CurvatureSign) (v : Vec2) :
    splitQuadratic lam (Vec2.scale r v) = r ^ 2 * splitQuadratic lam v := by
  simp [splitQuadratic, Vec2.scale]
  ring

/-- `ellPlus` vanishes against the split quadratic form for nonnegative lambda. -/
theorem ellPlus_splitQuadratic_zero {lam : CurvatureSign} (h : 0 ≤ lam) :
    splitQuadratic lam (ellPlus lam) = 0 := by
  simp [splitQuadratic, ellPlus]
  nlinarith [Real.sq_sqrt h]

/-- `ellMinus` vanishes against the split quadratic form for nonnegative lambda. -/
theorem ellMinus_splitQuadratic_zero {lam : CurvatureSign} (h : 0 ≤ lam) :
    splitQuadratic lam (ellMinus lam) = 0 := by
  simp [splitQuadratic, ellMinus]
  nlinarith [Real.sq_sqrt h]

/-- Predicate form for `ellPlus_splitQuadratic_zero`. -/
theorem ellPlus_isSplitNull {lam : CurvatureSign} (h : 0 ≤ lam) :
    IsSplitNull lam (ellPlus lam) := by
  exact ellPlus_splitQuadratic_zero h

/-- Predicate form for `ellMinus_splitQuadratic_zero`. -/
theorem ellMinus_isSplitNull {lam : CurvatureSign} (h : 0 ≤ lam) :
    IsSplitNull lam (ellMinus lam) := by
  exact ellMinus_splitQuadratic_zero h

end Spacetime
