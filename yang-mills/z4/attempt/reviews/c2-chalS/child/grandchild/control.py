import numpy as np
with open("control.txt","x") as f: f.write(str(np.linalg.matrix_rank(np.eye(3)))+"\n")
