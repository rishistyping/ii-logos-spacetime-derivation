import Mathlib

/-!
# Spacetime.Basic

Conservative basic data for the v0 skeleton.

This file intentionally avoids advanced matrix APIs.  The core 2x2 matrix is
encoded as a small structure so the first theorem ladder can be kept exact,
readable, and low-risk.
-/

namespace Spacetime

/-- Curvature/sign parameter used throughout the paper. -/
abbrev CurvatureSign : Type := ℝ

/-- Dimension parameter for symbolic bridge statements. -/
abbrev Dim : Type := Nat

/-- The three sign branches of the scalar curvature parameter. -/
inductive Branch where
  | positive
  | zero
  | negative
  deriving Repr, DecidableEq

/-- Branch classification as algebraic data. -/
noncomputable def classifyBranch (lam : CurvatureSign) : Branch := by
  classical
  exact if lam > 0 then Branch.positive else if lam = 0 then Branch.zero else Branch.negative

/-- A minimal 2x2 real matrix representation. -/
structure Mat2 where
  a00 : ℝ
  a01 : ℝ
  a10 : ℝ
  a11 : ℝ

namespace Mat2

/-- Trace of a 2x2 matrix. -/
def trace (A : Mat2) : ℝ :=
  A.a00 + A.a11

/-- Determinant of a 2x2 matrix. -/
def det (A : Mat2) : ℝ :=
  A.a00 * A.a11 - A.a01 * A.a10

/-- Characteristic polynomial evaluated at `x`. -/
def charpoly (A : Mat2) (x : ℝ) : ℝ :=
  x ^ 2 - A.trace * x + A.det

/-- Zero 2x2 matrix. -/
def zero : Mat2 :=
  ⟨0, 0, 0, 0⟩

/-- Scalar matrix `rI`. -/
def scalar (r : ℝ) : Mat2 :=
  ⟨r, 0, 0, r⟩

/-- Matrix multiplication for the minimal 2x2 representation. -/
def mul (A B : Mat2) : Mat2 :=
  ⟨A.a00 * B.a00 + A.a01 * B.a10,
   A.a00 * B.a01 + A.a01 * B.a11,
   A.a10 * B.a00 + A.a11 * B.a10,
   A.a10 * B.a01 + A.a11 * B.a11⟩

end Mat2

end Spacetime
