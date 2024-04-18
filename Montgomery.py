#        https://eduinf.waw.pl/inf/alg/001_search/0009.php Mozna samemu napisac wyzwanie XD ale dla testow i analizy pozyczam  
# def extendGCD(a,b):
#     u,w,x,z = 1,a,0,b
#     while w:
#         if w < z:
#             q = u
#             u = x
#             x = q
#             q = w
#             w = z
#             z = q
#         q = w // z
#         u -= q * x
#         w -= q * z
#     if z == 1:
#         if x < 0: x += b
#         return x
#     else:
#         print("BRAK")

# GCD REKRURENCYJNIE 
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

    # Montgomery Transformacja
    AR = (A * R) % N
    BR = (B * R) % N
    T = (AR * BR) % N  # Mnozenie w przestrzeni Montgomery'ego

    _, N_inv, _ = extendGCD(N, R)
    N_inv = (-N_inv) % R    # Odwrotnosc N 

    # Montgomery reudkcja
    m = (T * N_inv) % R
    U = (T + m * N) // R
    # Upewaniamy się  czy U [0,N-1] znalazłem na wikipedii bez tego w niektórych przypadkach był błąd 
    if U >= N:
        U -= N
    #MOntgomery transdformacja 
    result = (U * R_inv) % N

    return result

# Example usage
A = int(input("Podaj A: "))
B = int(input("Podaj B: "))
N = int(input("Podaj N(LICZBA PIERWSZA): "))
result = montgomeryMultiplication(A, B, N)
print("WYNIK ALGORYTMU:", result)
print("WYNIK POPRAWNY", A * B % N)


# https://www.nayuki.io/page/montgomery-reduction-algorithm

# https://en.wikipedia.org/wiki/Montgomery_modular_multiplication

# https://cp-algorithms.com/algebra/montgomery_multiplication.html
# https://en.algorithmica.org/hpc/number-theory/montgomery/

# NOTATKI POLECAM SOBIE PRZYKLAD ZROBIC 
# https://whiteboard.office.com/me/whiteboards/p/c3BvOmh0dHBzOi8vcG9saXRlY2huaWthd3JvY2xhd3NrYS1teS5zaGFyZXBvaW50LmNvbS9wZXJzb25hbC8yNzYyMDRfc3R1ZGVudF9wd3JfZWR1X3Bs/b!j45tsbHQMk-4ckJnX4ZgE-AtSja5THtLqfgCb8OmHq4Uh771Y3xuTZylmRIDSbim/01J73P2KTBGBJFNFS4CRCJQUUZG46PIIIC 