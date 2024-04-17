#        https://eduinf.waw.pl/inf/alg/001_search/0009.php Mozna samemu napisac wyzwanie XD ale dla testow i analizy pozyczam  
def extendGCD(a,b):
    u,w,x,z = 1,a,0,b
    while w:
        if w < z:
            q = u
            u = x
            x = q
            q = w
            w = z
            z = q
        q = w // z
        u -= q * x
        w -= q * z
    if z == 1:
        if x < 0: x += b
        return x
    else:
        print("BRAK")

 
def montgomery():
    A = int(input("Podaj A:"))
    B = int(input("Podaj B:"))
    N = int(input("Podaj N:"))
    r = 2
    while(r<N):
        r *=2 
    
    am =  (A * r) % 17  # A W PRZESTRZENI MONTGOMERYEGO  WZOR A * R MOD N 
    bm = (B * r) % 17  # B W PRZESTRZENI MONTGOMERYEGO WZOR B * R MOD N 
    c = (am * bm)   # MNOZENIE W PRZESTRZENI MONTGOMERYEGO  WZOR : (WZOR A * R MOD N  ) * (WZOR B * R MOD N  ) ( NA WHITEBOARD ZMIENNA T )
    a = N # POMOCNICZNA 
    b = r  # POMOCNICZA 
    rXD = extendGCD(a,b) # OBLICZANIE Z EUKLIDESA 
    rXD = r - rXD # ODWROTNOSC R^-1 MOD N
    nXD = extendGCD(b,a)
    m = (c * rXD) % r
    u = (c + m * N) // r
    


    result = (u * nXD) % N
    print("WYNIK ALGORYTMU: ", result)
    print(f"{A} MOD {B}  =  ", (A*B %N))

  
montgomery()




# https://www.nayuki.io/page/montgomery-reduction-algorithm

# https://en.wikipedia.org/wiki/Montgomery_modular_multiplication

# https://cp-algorithms.com/algebra/montgomery_multiplication.html
# https://en.algorithmica.org/hpc/number-theory/montgomery/

# NOTATKI POLECAM SOBIE PRZYKLAD ZROBIC 
# https://whiteboard.office.com/me/whiteboards/p/c3BvOmh0dHBzOi8vcG9saXRlY2huaWthd3JvY2xhd3NrYS1teS5zaGFyZXBvaW50LmNvbS9wZXJzb25hbC8yNzYyMDRfc3R1ZGVudF9wd3JfZWR1X3Bs/b!j45tsbHQMk-4ckJnX4ZgE-AtSja5THtLqfgCb8OmHq4Uh771Y3xuTZylmRIDSbim/01J73P2KTBGBJFNFS4CRCJQUUZG46PIIIC 