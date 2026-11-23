import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum

/-! An even periodic cubic SU(2) slice admits central links with every plaquette equal to -I.
The kernel checks the exponent of the central sign. The accompanying note identifies the
two elements of ZMod 2 with the central matrices ±I. -/
namespace Millennium.YangMills.WilsonSlice

abbrev Site (L : ℕ) := Fin 3 → ZMod L

def step {L : ℕ} (x : Site L) (i : Fin 3) : Site L :=
  fun j => x j + if i = j then 1 else 0

def link {L : ℕ} (h : 2 ∣ L) (x : Site L) (i : Fin 3) : ZMod 2 :=
  let parity := ZMod.castHom h (ZMod 2)
  match i with
  -- PCP begin links
  | 0 => 0
  | 1 => parity (x 0)
  | 2 => parity (x 0) + parity (x 1)
  -- PCP end links

def face {L : ℕ} (h : 2 ∣ L) (x : Site L) (i j : Fin 3) : ZMod 2 :=
  link h x i + link h (step x i) j - link h (step x j) i - link h x j

theorem every_face {L : ℕ} (h : 2 ∣ L) (x : Site L) (i j : Fin 3) (hij : i < j) :
    face h x i j = 1 := by
  -- PCP begin proof
  fin_cases i <;> fin_cases j <;>
    norm_num [face, link, step, map_add, ZMod.cast_one h] at *
  -- PCP end proof

#print axioms every_face
end Millennium.YangMills.WilsonSlice
