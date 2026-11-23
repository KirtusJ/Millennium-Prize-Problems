# Reproducing the shell reconstruction

The Python check generates independent Haar SU(2) link matrices with a fixed seed, fixes the indicated tree by an independent graph traversal, builds the rooted faces, then discards the links. It solves all squares with one unknown repeatedly until every edge is recovered. The last column checks a separate diagonal connection with face angle $1/(2L^2)$. Run with Python and NumPy. [Checker](check.py)

| Side | Shell links | Shell squares | Maximum Frobenius error | Seam / face angle |
|---:|---:|---:|---:|---:|
| 2 | 208 | 192 | 1.45e−14 | 4 |
| 3 | 672 | 648 | 5.15e−14 | 9 |
| 4 | 1568 | 1536 | 9.46e−14 | 16 |
| 6 | 5232 | 5184 | 1.66e−13 | 36 |

The PCP OS parent checks the shell vertex and tree edge counts, the child checks both oriented square inverses on all 4,096 assignments in the quaternion group of order eight, and the grandchild checks the word-budget arithmetic and the Cartan seam coefficient. Each child boot is launched by the shared host relay after the preceding guest requests it. All three reported exit zero and 47 register events on the pinned kernel with SHA-256 `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`. [Guest source](worker.c) · [Expected output](checks.txt) · [Relay](../../../../observable-normalization/transfer-increments/replay-guests.py)

| Guest | Executable SHA-256 | Register head |
|---|---|---|
| Parent | 3cb227e365887a7ce6d95b1fe2246df82857c38992695ccfa07b34b349428ef9 | 2527c544726d514ba0bedcad49f867e1c6ba4e594797e613ceac91a339749901 |
| Child | 577c6545950f897e973514449d7f758ccca04d73ba4090d8f94b8183f59817a7 | 442adc06a741bd20d0e857191245c568eda24d203e4b9fb1a552f470ffb5f253 |
| Grandchild | bf9f9d8daa72b0a271a56abb519293bf6eabf641253de9354e85befc60df4e12 | 82ad85c7e9b9d7cc4c1bfa7fc674d9fd5a56547ff63a3e5a6acbe5c4a7e92255 |

```sh
python check.py
python ../../../../observable-normalization/transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof checks.txt
```
