# https://www.nayuki.io/page/montgomery-reduction-algorithm

def extendGCD(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extendGCD(b % a, a)
        return (gcd, y - (b // a) * x, x)
    

def montgomeryMultiplication(A, B, N):

    R = 1 << (N.bit_length())  
    _, R_inv, _ = extendGCD(R, N)  
    R_inv = R_inv % N # ODwrotnosc R 

    K = (R*(R_inv % N) -1)/N             # // N  ? 
    am  = A*R % N 
    bm  = B*R % N
    X = am * bm
    s = (X*K % R)
    t = X + s*N
    u = t /R             # //N  ?
    cc = u if u < N else u - N;
    c = cc*R_inv % N
    return c




A = int(input("Podaj A: "))
B = int(input("Podaj B: "))
N = int(input("Podaj N(LICZBA PIERWSZA): "))
result = montgomeryMultiplication(A, B, N)
print("WYNIK ALGORYTMU:", result)
print("WYNIK POPRAWNY", A * B % N)