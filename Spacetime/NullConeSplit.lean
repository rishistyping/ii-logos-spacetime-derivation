import Spacetime.NullBridge

/-!
# Spacetime.NullConeSplit

Planned algebraic split-cone packet for v0.6+ execution.
This file records cone-closure facts and keeps physical interpretations out of scope.
-/

namespace Spacetime

/-- Cone-null predicate induced by the split quadratic form. -/
def splitCone (lam : CurvatureSign) (v : Vec2) : Prop :=
  splitQuadratic lam v = 0

/-- Cone null condition is preserved by scalar scaling in the split form. -/
theorem splitCone_scale (lam r : CurvatureSign) {v : Vec2} (h : splitCone lam v) :
    splitCone lam (Vec2.scale r v) := by
  unfold splitCone at *
  rw [splitQuadratic_scale, h]
  ring

/-- `ellPlus` lies on the split cone in the nonnegative branch. -/
theorem splitCone_ellPlus_zero {lam : CurvatureSign} (h : 0 ≤ lam) :
    splitCone lam (ellPlus lam) := by
  unfold splitCone
  exact ellPlus_splitQuadratic_zero h

/-- `ellMinus` lies on the split cone in the nonnegative branch. -/
theorem splitCone_ellMinus_zero {lam : CurvatureSign} (h : 0 ≤ lam) :
    splitCone lam (ellMinus lam) := by
  unfold splitCone
  exact ellMinus_splitQuadratic_zero h

end Spacetime
