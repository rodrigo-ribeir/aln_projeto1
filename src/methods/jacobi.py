import numpy as np

def erro_quadrado(u, v):
    return (u-v)@(u-v)

def Jacobi(A, b, e=1e-10, max_iter = 1000):
    m, n = A.shape
    if m != n:
        print("A matriz deve ser quadrada")
        return -1
    x_velho = np.zeros(n)
    x_novo = np.full(n, 10)
    iteracoes = 0
    while(erro_quadrado(x_novo, x_velho < e*e) & iteracoes < max_iter):
        interacoes+=1
        for i in (0, n-1):
            a_linha = A[i]
            somatorio = A[i]@x_velho - A[i][i]*x[i]
            x_novo[i] = (b[i]- somatorio)/A[i][i]
            x_velho = np.copy(x_novo)

    return x_novo, iteracoes


A = np.array([1, 2, -2], [1, 1, 1], [2, 2, 1])
b = np.array([1, 2, 3])

solucao, i = Jacobi(A, b)
print("Solução:", solucao)
print("Iterações:", i)