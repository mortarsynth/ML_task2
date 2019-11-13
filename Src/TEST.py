import numpy as np
import scipy.sparse as sp



a = sp.dok_matrix((2, 2), dtype=np.float)
a[0, 1] = 1.0
a[1, 0] = 1.0
a_csr = a.tocsr()
a_dense = a_csr.todense()

b = a
b[0, 0] = 0.5
b[1, 1] = 0.5
b_csr = b.tocsr()
b_dense = b_csr.todense()

print(b2_csr)
