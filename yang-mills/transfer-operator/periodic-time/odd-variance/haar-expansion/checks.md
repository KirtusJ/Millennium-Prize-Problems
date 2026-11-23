# Checks of the Haar coefficient and its support

The checker fixes the first figure-eight at the origin and examines the 48 possible words at each candidate second root. Two action insertions cover at most eight odd edges, so the two eight-edge words must share at least four edges. Any intersecting pair has root displacement in $[-2,2]^4$. To find a pair of distinct inserted plaquettes the checker picks one odd edge, enumerates the six squares touching it, and tests whether the remaining odd edges bound one elementary square. It compares the entire resulting pair with the two unmatched faces. [Exact support enumeration](check.py)

There were 48 identical word pairs, 1,440 ordered overlapping word pairs with an admissible insertion pair, and 96 further ordered pairs sharing at least four edges that admitted no insertion pair. Every admissible overlapping pair shared exactly one plaquette. Each unmatched face had a private edge. Its mixed real-imaginary Haar moment therefore vanished.

An independent one-dimensional integration tilted each of the two defining Haar face holonomies by its real trace. It tests the diagrams retained in the contact calculation. The table gives the change of this two-face reading divided by $\beta^2$, including the 48 word weights; the exact target is $-3/1024=-0.0029296875$.

| $\beta$ | Two-face coefficient estimate |
|---:|---:|
| 0.1 | −0.0029272481 |
| 0.05 | −0.0029290773 |
| 0.025 | −0.0029295349 |
| 0.0125 | −0.0029296494 |

The parent native PCP OS worker evaluated the contact contractions on the 24 unit Hurwitz quaternions and checked the required spherical moments of degrees two and four. Its child counted the conditional action neighborhood directly, and its grandchild checked the path distance and row-mass bounds on a finite periodic graph. The relay matched each child request and all three expected records. Each guest exited 0 and its register contained 47 events. These are finite checks; the uniform infinite-volume remainder uses the comparison proof. A4’s original checker also reproduced 30,000 distinct edge supports on a side-five torus, mixed norm $3/4096$ and contact $9/256$. [Guest source](worker.c) · [Expected output](checks.txt) · [Host relay](../../../../observable-normalization/transfer-increments/replay-guests.py) · [A4 checker](../../../../observable-normalization/transfer-increments/local-action/odd-clover/haar-dual/check.py)

| Guest | Executable SHA-256 | Register head in the recorded deployment |
|---|---|---|
| Parent | 0432a3eaed993050cf947ac384ac9a57619ed048c3566c07c32b49259e0ab0d8 | f7763b41ed0d56bef36123822f0738610b46363ad292e0c0a408a68030a8098f |
| Child | 78d5b7700a6ec949961dadeda552c072ffe5172d05eb1beffb15372e62b8e2fe | 3ef42aa4db20bb7bf7bbc9573ed97a3ce90537bc2fc9f10f51ce5053c69064f2 |
| Grandchild | c856b27e826910cf89b0e935856d6cd18eae175148c5e16eb842e31abd9001c4 | 94b89fca073083dee077c6e950d26445b28e5d5bbed157b7ade3428f18ef0c63 |

Kernel SHA-256 was d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f. The generated record SHA-256 was 19fe1615e93695bb484ec48d76a0ae4b552f4907542a2a42d8b9aba5a18cee52. From this directory, with NumPy, gcc, QEMU and the kernel available, run the following commands.

```sh
python check.py
python ../../../../observable-normalization/transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof checks.txt
```
