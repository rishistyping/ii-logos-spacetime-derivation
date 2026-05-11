(* v0 placeholder builder for the Spacetime explainer notebook. *)

ClearAll[lambda, x, A];
A[lambda_] := {{0, -lambda}, {-1, 0}};

Print["A(lambda) = ", MatrixForm[A[lambda]]];
Print["trace = ", Tr[A[lambda]]];
Print["det = ", Det[A[lambda]]];
Print["charpoly = ", CharacteristicPolynomial[A[lambda], x]];
Print["A^2 = ", MatrixForm[Simplify[A[lambda].A[lambda]]]];

If[!DirectoryQ["wolfram/notebooks"], CreateDirectory["wolfram/notebooks", CreateIntermediateDirectories -> True]];
Export["wolfram/notebooks/spacetime_explainer.nb", Notebook[{Cell["A Brief Derivation of Spacetime — v0 Notebook Stub", "Title"], Cell["The deterministic builder currently records the exact A(lambda) matrix spine. Extend this file for the full public notebook.", "Text"]}]];
