import numpy as np

def SVD(A):
    #V
    ATransA = np.dot(A.T, A)

    eig_V, V = np.linalg.eig(ATransA)  
    eig_V_sorted_indices = np.argsort(eig_V)[::-1]

    V1 = V[:, eig_V_sorted_indices]
    eig_V1 = eig_V[eig_V_sorted_indices]

    #U
    AATrans = np.dot(A, A.T)

    eig_U, U = np.linalg.eig(AATrans)
    eig_U_sorted_indices = np.argsort(eig_U)[::-1]

    U1 = U[:, eig_U_sorted_indices]
    eig_U1 = eig_U[eig_U_sorted_indices]

    #Sigma
    Sigma = np.zeros_like(A, dtype=float)
    for i in np.arange(min(A.shape)):
        Sigma[i, i] = np.sqrt(eig_V1[i])    
    
    return U1, Sigma, V1.T