import Std

/-! The four rotation classes represented by the signed Hamilton basis.
All coefficient arithmetic takes place in the integers. -/
namespace YangMills.CentralQuotient

inductive Axis where
  | e | i | j | k
  deriving Repr, BEq, DecidableEq

structure QuaternionZ where
  r : Int
  x : Int
  y : Int
  z : Int
  deriving Repr, DecidableEq

def mul (p q : QuaternionZ) : QuaternionZ :=
  ⟨p.r*q.r - p.x*q.x - p.y*q.y - p.z*q.z,
   p.r*q.x + p.x*q.r + p.y*q.z - p.z*q.y,
   p.r*q.y - p.x*q.z + p.y*q.r + p.z*q.x,
   p.r*q.z + p.x*q.y - p.y*q.x + p.z*q.r⟩

def neg (p : QuaternionZ) : QuaternionZ := ⟨-p.r, -p.x, -p.y, -p.z⟩

def basis : Axis → QuaternionZ
  | .e => ⟨1, 0, 0, 0⟩
  | .i => ⟨0, 1, 0, 0⟩
  | .j => ⟨0, 0, 1, 0⟩
  | .k => ⟨0, 0, 0, 1⟩

def lift (a : Axis) (minus : Bool) : QuaternionZ :=
  if minus then neg (basis a) else basis a

def twisted (a b : Axis) : Bool :=
  !(a == .e || b == .e || a == b)

def HasFlatLift {ι : Type} (hol : ι → Axis) : Prop :=
  ∃ sign : ι → Bool, ∀ s t,
    mul (lift (hol s) (sign s)) (lift (hol t) (sign t)) =
    mul (lift (hol t) (sign t)) (lift (hol s) (sign s))

/-- Six bits in the order 12, 13, 14, 23, 24, 34. -/
def flux (a b c d : Axis) : Nat :=
  (twisted a b).toNat + 2*(twisted a c).toNat + 4*(twisted a d).toNat +
  8*(twisted b c).toNat + 16*(twisted b d).toNat + 32*(twisted c d).toNat

def axes : List Axis := [.e, .i, .j, .k]

def fluxes : List Nat :=
  axes.flatMap fun a => axes.flatMap fun b =>
  axes.flatMap fun c => axes.map fun d => flux a b c d

/-- Faces 0,1 are opposite, as are 2,3 and 4,5. Each adjacent pair
names their unique common edge. The ordering also labels the twelve edge bits. -/
def cubeEdges : List (Nat × Nat) :=
  [(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),(2,4),(2,5),(3,4),(3,5)]

def closedFaceMasks : List Nat :=
  (List.range 64).filter fun m =>
    cubeEdges.all fun (u,v) => m.testBit u == m.testBit v

/-- Count edge sign assignments with each face-sign pattern by adding one
independent edge at a time. At one edge the two incident face signs both flip. -/
def faceMultiplicities : List Nat :=
  cubeEdges.foldl (fun previous (u,v) =>
    let flip := 2^u + 2^v
    (List.range 64).map fun m => previous[m]! + previous[m ^^^ flip]!)
    (1 :: List.replicate 63 0)

def negativeFaces (mask : Nat) : Nat :=
  ((List.range 6).filter fun i => mask.testBit i).length

/-- When exp β = 2 and every initial plaquette is the identity,
64 times the Boltzmann weight of a configuration with k negative faces is 2^(12−2k). -/
def scaledCubeSum : Nat :=
  ((List.range 64).map fun m => faceMultiplicities[m]! * 2^(12 - 2 * negativeFaces m)).sum

end YangMills.CentralQuotient
