import Spacetime.TimeEvolutionMatrix

/-!
# Spacetime.EigenDirections

The v0.3 algebraic eigendirection bridge for the already-promoted matrix spine.
This file proves only the matrix/eigenvector facts.  Null-vector, light-cone,
redshift, horizon, and arrow-of-time readings remain outside proof authority.
-/

namespace Spacetime

/-- A minimal two-vector representation in `(K_i, P_i)` coordinates. -/
structure Vec2 where
  k : ℝ
  p : ℝ

namespace Vec2

/-- The zero two-vector. -/
def zero : Vec2 :=
  ⟨0, 0⟩

/-- Scalar multiplication for the minimal two-vector representation. -/
def scale (r : ℝ) (v : Vec2) : Vec2 :=
  ⟨r * v.k, r * v.p⟩

/-- Fieldwise extensionality for the minimal two-vector representation. -/
theorem ext {u v : Vec2} (hk : u.k = v.k) (hp : u.p = v.p) : u = v := by
  cases u
  cases v
  simp at hk hp
  cases hk
  cases hp
  rfl

end Vec2

namespace Mat2

/-- Matrix-vector multiplication for the minimal 2x2 representation. -/
def mulVec (A : Mat2) (v : Vec2) : Vec2 :=
  ⟨A.a00 * v.k + A.a01 * v.p,
   A.a10 * v.k + A.a11 * v.p⟩

end Mat2

/-- The `+sqrt(lambda)` algebraic eigendirection: `P_i - sqrt(lambda) K_i`. -/
noncomputable def ellPlus (lam : CurvatureSign) : Vec2 :=
  ⟨-Real.sqrt lam, 1⟩

/-- The `-sqrt(lambda)` algebraic eigendirection: `P_i + sqrt(lambda) K_i`. -/
noncomputable def ellMinus (lam : CurvatureSign) : Vec2 :=
  ⟨Real.sqrt lam, 1⟩

/-- `ellPlus` is nonzero. -/
theorem ellPlus_nonzero (lam : CurvatureSign) : ellPlus lam ≠ Vec2.zero := by
  intro h
  have hp := congrArg Vec2.p h
  simp [ellPlus, Vec2.zero] at hp

/-- `ellMinus` is nonzero. -/
theorem ellMinus_nonzero (lam : CurvatureSign) : ellMinus lam ≠ Vec2.zero := by
  intro h
  have hp := congrArg Vec2.p h
  simp [ellMinus, Vec2.zero] at hp

/-- `ellPlus` is an eigenvector of `A(lambda)` with eigenvalue `sqrt(lambda)`. -/
theorem ellPlus_eigen {lam : CurvatureSign} (h : 0 ≤ lam) :
    Mat2.mulVec (timeEvolutionMatrix lam) (ellPlus lam) =
      Vec2.scale (Real.sqrt lam) (ellPlus lam) := by
  apply Vec2.ext <;> simp [Mat2.mulVec, Vec2.scale, ellPlus, timeEvolutionMatrix]
  nlinarith [Real.sq_sqrt h]

/-- `ellMinus` is an eigenvector of `A(lambda)` with eigenvalue `-sqrt(lambda)`. -/
theorem ellMinus_eigen {lam : CurvatureSign} (h : 0 ≤ lam) :
    Mat2.mulVec (timeEvolutionMatrix lam) (ellMinus lam) =
      Vec2.scale (-Real.sqrt lam) (ellMinus lam) := by
  apply Vec2.ext <;> simp [Mat2.mulVec, Vec2.scale, ellMinus, timeEvolutionMatrix]
  nlinarith [Real.sq_sqrt h]

/-- On the positive branch the two algebraic eigendirections are distinct. -/
theorem ellPlus_ne_ellMinus {lam : CurvatureSign} (h : 0 < lam) :
    ellPlus lam ≠ ellMinus lam := by
  intro heq
  have hk := congrArg Vec2.k heq
  have hs : 0 < Real.sqrt lam := Real.sqrt_pos.2 h
  simp [ellPlus, ellMinus] at hk
  linarith

end Spacetime
