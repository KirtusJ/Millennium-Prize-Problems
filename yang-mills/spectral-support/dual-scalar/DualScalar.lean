import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp

namespace Millennium.YangMills.D4.DualScalar

open Matrix

/-- In orthogonal coordinates adapted to the primal and dual curvature spaces,
    the complementary block of the inverse gives the reciprocal determinant. -/
theorem schurReciprocity {m n : Type*} [Fintype m] [Fintype n] [DecidableEq m] [DecidableEq n]
    (A : Matrix m m ℝ) (B : Matrix m n ℝ) (C : Matrix n m ℝ) (D : Matrix n n ℝ)
    [Invertible A] [Invertible (D-C*⅟A*B)] [Invertible (fromBlocks A B C D)] :
    (fromBlocks A B C D).det * (⅟(fromBlocks A B C D)).toBlocks₂₂.det=A.det := by
  rw [Matrix.invOf_fromBlocks₁₁_eq, Matrix.toBlocks_fromBlocks₂₂, Matrix.det_fromBlocks₁₁,
    mul_assoc, ← Matrix.det_mul, mul_invOf_self, Matrix.det_one, mul_one]

theorem sourceComplement {R : Type*} [Ring R] (w z k u : R) (hw : w*z=1) (hu : k*u=0) :
    (w-w*k*w)*z*u=u := by
  simp [sub_mul,mul_assoc,hw,hu]

/-- An operator supported on the complementary columns is fixed by its weighted action there. -/
theorem complementaryKernel {m n : Type*} [Fintype m] [Fintype n] [DecidableEq n]
    (G : Matrix m n ℝ) (J Z : Matrix m m ℝ) (H : Matrix n n ℝ)
    (hl : G*G.transpose*J=J) (hr : J*G*G.transpose=J)
    (hs : J*Z*G=G) (ho : G.transpose*G=1)
    (hi : (G.transpose*Z*G)*H=1) : J=G*H*G.transpose := by
  have hc : (G.transpose*J*G)*(G.transpose*Z*G)=1 := by
    calc
      _ = G.transpose*(J*G*G.transpose)*Z*G := by simp only [Matrix.mul_assoc]
      _ = G.transpose*(J*Z*G) := by rw [hr]; simp only [Matrix.mul_assoc]
      _ = 1 := by rw [hs,ho]
  have hm : G.transpose*J*G=H := by
    calc
      _ = (G.transpose*J*G)*((G.transpose*Z*G)*H) := by rw [hi,Matrix.mul_one]
      _ = H := by rw [← Matrix.mul_assoc,hc,Matrix.one_mul]
  calc
    J = G*G.transpose*(J*G*G.transpose) := by rw [hr,hl]
    _ = G*(G.transpose*J*G)*G.transpose := by simp only [Matrix.mul_assoc]
    _ = _ := by rw [hm]

theorem oddCycle {R : Type*} [Ring R] (x y z : R) : (-x)*(-y)*(-z)=-(x*y*z) := by simp

theorem centeredEven (p d p' d' a : ℝ) (h : p=d'-3*a/2) (k : p'=d+3*a/2) :
    (p+d)/2+3*a/4=(p'+d')/2-3*a/4 := by linarith

theorem radialDifference (w v : ℝ) :
    w*v^2-w*(1-w*v)^2=2*w*v-w+w*(w-1)*(2*v-(w+1)*v^2) := by ring

theorem localMixed (v g h gh : ℝ) :
    2*gh-2*(2*v*gh+2*g*h)=2*(1-2*v)*gh-4*g*h := by ring

theorem halfDiagonal (g h gh : ℝ) :
    -(3/16)*(2*(1-2*(1/2:ℝ))*gh-4*g*h)=3/4*g*h := by ring

theorem actionDependence (k x : ℝ) : -(15/4)*k*x=(-10*k)*(3/8*x) := by ring

theorem generalAction (d q v : ℝ) (hd : d≠0) :
    -(8*q/d)*(d/8*v^2) = -q*v^2 := by field_simp; ring

theorem squaredDeficit (d k : ℝ) :
    8*(k*d*(d+2)/4)=2*k*(d+2)*d := by ring

theorem asymptoticRatio (p x y z : ℝ) (hp : p≠0) (hx : x≠0) (hy : y≠0) (hz : z≠0) :
    (288/p^8*(1/(x^8*y^8)+1/(x^8*z^8)+1/(y^8*z^8))) /
     (1728/p^6/(x*y*z)^4) =
    1/(6*p^2)*(z^4/(x*y)^4+y^4/(x*z)^4+x^4/(y*z)^4) := by
  field_simp
  ring

theorem uniqueNumerator (M b x y k : ℤ) (h : 2*b<M) (b₀ : 0≤b)
    (hx : -b≤x ∧ x≤b) (hy : -b≤y ∧ y≤b) (hk : x-y=M*k) : x=y := by
  have pos : 0≤M := by omega
  rcases lt_trichotomy k 0 with neg | zero | plus
  · have bound : 0≤ -1-k := by omega
    nlinarith [mul_nonneg pos bound, hx.1, hy.2]
  · simpa [zero] using sub_eq_zero.mp (show x-y=0 by simpa [zero] using hk)
  · have bound : 0≤k-1 := by omega
    nlinarith [mul_nonneg pos bound, hx.2, hy.1]

def agrees (p : Nat) (fraction : Int × Nat) (r : Nat) : Bool :=
  (fraction.2 % p != 0) && ((fraction.1-(r:Int)*fraction.2) % p == 0)

def validInteger (n : Int) (den bound : Nat) (rs : List (Nat × Nat)) : Prop :=
  let ps := rs.map Prod.fst
  ps.Pairwise Nat.Coprime ∧ 2*bound < ps.prod ∧ n.natAbs ≤ bound ∧
  (rs.all (fun (p,r) => (den%p != 0) && ((n-(den:Int)*r)%p == 0)))=true

theorem certifiedCube : validInteger (5358791580308898413877169054252204032) 2452100204171991946071508971945984000000 114115251950344253313782691219050432437369700352
    [(999983, 768003), (999979, 898808), (999961, 418789), (999959, 148612), (999953, 801638), (999931, 910712), (999917, 119876), (999907, 336186)] := by
  unfold validInteger
  decide

theorem certifiedStar : validInteger (-3469713910289433432490180232968077312) 2452100204171991946071508971945984000000 123872086691261318786234103009838817585446846464
    [(999983, 484891), (999979, 671260), (999961, 293877), (999959, 508594), (999953, 960007), (999931, 582447), (999917, 394116), (999907, 310631)] := by
  unfold validInteger
  decide

def boundaryFractions : List (Int × Nat) := [
  (16962491267, 125903545000695),
  (-16962491267, 125903545000695),
  (18743362972614416149495387, 25198931177334574748217360000),
  (-3698361655138868693387, 22499045694048727453765500),
  (-4024682034546488110997, 19999151728043313292236000),
  (1387771036187991908423, 19999151728043313292236000)]

def twistFractions : List (Int × Nat) := [
  (26128480291, 292183491600),
  (26128480291, 292183491600),
  (13420141639117, 21058248606595200),
  (-13420141639117, 21058248606595200),
  (1932371081494058279, 12647584113121077120000)]

theorem twistedSignal :
    ((336160425392856154089090109/153821815121395508095008000000:ℚ)+(-507867206387987309649227261/358917568616589518888352000000))/2=41476067929301557483797449/107675270584976855666505600000 ∧
    (0:ℚ)<(1932371081494058279/12647584113121077120000) ∧ (1932371081494058279/12647584113121077120000:ℚ)<(41476067929301557483797449/107675270584976855666505600000) ∧
    (1440/100000:ℚ)^2<(41476067929301557483797449/107675270584976855666505600000:ℚ)^2/(26128480291/292183491600)^3 ∧
    (41476067929301557483797449/107675270584976855666505600000:ℚ)^2/(26128480291/292183491600)^3<(1441/100000:ℚ)^2 := by norm_num

theorem certifiedSkewCube : validInteger (-508038751613375745825329566542397440) 2452100204171991946071508971945984000000 105754759233303842333188230987301066260244070400
    [(999983, 726783), (999979, 927413), (999961, 6779), (999959, 995073), (999953, 701596), (999931, 347334), (999917, 615700), (999907, 50241)] := by
  unfold validInteger
  decide

theorem certifiedSkewStar : validInteger (924718918952371930198497712663363584) 2452100204171991946071508971945984000000 116935611882782118675323183656293757838550368256
    [(999983, 20293), (999979, 646407), (999961, 416008), (999959, 485476), (999953, 525112), (999931, 657568), (999917, 260358), (999907, 489949)] := by
  unfold validInteger
  decide

theorem skewSignal :
    ((-12168391210385646769328591/58731965773623739454457600000:ℚ)+(406057467161566570748650331/1076752705849768556665056000000))/2=68613860614186142491609811/807564529387326417498792000000 ∧
    (0:ℚ)<(202946807006718881/28457064254522423520000) ∧ (202946807006718881/28457064254522423520000:ℚ)<(68613860614186142491609811/807564529387326417498792000000) ∧
    (4105/100000:ℚ)^2<(68613860614186142491609811/807564529387326417498792000000:ℚ)^2/(181679364144682978830181843/42421859155979146911058992000000) ∧
    (68613860614186142491609811/807564529387326417498792000000:ℚ)^2/(181679364144682978830181843/42421859155979146911058992000000)<(4106/100000:ℚ)^2 := by norm_num

def skewFractions : List (Int × Nat) := [
  (1645494547, 97394497200),
  (1645494547, 97394497200),
  (-13711313008171, 315873729098928000),
  (13711313008171, 315873729098928000),
  (202946807006718881, 28457064254522423520000)]

-- BEGIN PCP OS generated dual response checks
def boundaryResidues : List Nat := [24, 77, 84, 18, 70, 37]

def twistResidues : List Nat := [90, 90, 123, 70, 97]

def skewResidues : List Nat := [192, 192, 175, 18, 188]

theorem measuredBoundary : boundaryFractions.length=boundaryResidues.length ∧
    (boundaryFractions.zipWith (agrees 101) boundaryResidues).all id=true := by decide

theorem measuredTwist : twistFractions.length=twistResidues.length ∧
    (twistFractions.zipWith (agrees 193) twistResidues).all id=true := by decide

theorem measuredSkew : skewFractions.length=skewResidues.length ∧
    (skewFractions.zipWith (agrees 193) skewResidues).all id=true := by decide

#print axioms schurReciprocity
#print axioms sourceComplement
#print axioms oddCycle
#print axioms complementaryKernel
#print axioms generalAction
#print axioms squaredDeficit
#print axioms centeredEven
#print axioms radialDifference
#print axioms localMixed
#print axioms halfDiagonal
#print axioms actionDependence
#print axioms asymptoticRatio
#print axioms uniqueNumerator
#print axioms certifiedCube
#print axioms certifiedStar
#print axioms twistedSignal
#print axioms measuredBoundary
#print axioms measuredTwist
#print axioms certifiedSkewCube
#print axioms certifiedSkewStar
#print axioms skewSignal
#print axioms measuredSkew
end Millennium.YangMills.D4.DualScalar
