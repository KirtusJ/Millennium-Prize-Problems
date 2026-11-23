import Model

namespace YangMills.CentralQuotient

theorem product_up_to_sign (a b : Axis) (s t : Bool) :
    let p := mul (lift a s) (lift b t)
    let q := mul (lift b t) (lift a s)
    p = if twisted a b then neg q else q := by
  cases a <;> cases b <;> cases s <;> cases t <;> decide

theorem commute_iff (a b : Axis) (s t : Bool) :
    mul (lift a s) (lift b t) = mul (lift b t) (lift a s) ↔
    twisted a b = false := by
  cases a <;> cases b <;> cases s <;> cases t <;> decide

theorem witness (s t : Bool) :
    mul (lift .i s) (lift .j t) ≠ mul (lift .j t) (lift .i s) := by
  cases s <;> cases t <;> decide

theorem flatLift_iff {ι : Type} (hol : ι → Axis) :
    HasFlatLift hol ↔ ∀ s t, twisted (hol s) (hol t) = false := by
  constructor
  · rintro ⟨sign, h⟩ s t
    exact (commute_iff _ _ (sign s) (sign t)).mp (h s t)
  · intro h
    exact ⟨fun _ => false, fun s t => (commute_iff _ _ false false).mpr (h s t)⟩

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem four_cycle_census :
    fluxes.length = 256 ∧ fluxes.count 0 = 46 ∧
    (fluxes.eraseDups.erase 0).length = 35 ∧
    ((fluxes.eraseDups.erase 0).all (fun m => fluxes.count m == 6)) = true := by decide +kernel

theorem pfaffian_zero (a b c d : Axis) :
    ((twisted a b && twisted c d) ^^ (twisted a c && twisted b d)) =
      (twisted a d && twisted b c) := by
  cases a <;> cases b <;> cases c <;> cases d <;> decide

theorem closed_cube_surfaces : closedFaceMasks = [0, 63] := by decide +kernel

set_option maxRecDepth 20000 in
set_option maxHeartbeats 0 in
theorem cube_face_fibres :
    ((List.range 64).all fun m => faceMultiplicities[m]! ==
      (if negativeFaces m % 2 == 0 then 128 else 0)) = true := by decide +kernel

set_option maxRecDepth 20000 in
set_option maxHeartbeats 0 in
theorem cube_weight_at_identity : scaledCubeSum = 1046656 := by decide +kernel

end YangMills.CentralQuotient

#print axioms YangMills.CentralQuotient.product_up_to_sign
#print axioms YangMills.CentralQuotient.commute_iff
#print axioms YangMills.CentralQuotient.witness
#print axioms YangMills.CentralQuotient.flatLift_iff
#print axioms YangMills.CentralQuotient.four_cycle_census
#print axioms YangMills.CentralQuotient.pfaffian_zero
#print axioms YangMills.CentralQuotient.closed_cube_surfaces
#print axioms YangMills.CentralQuotient.cube_face_fibres
#print axioms YangMills.CentralQuotient.cube_weight_at_identity
