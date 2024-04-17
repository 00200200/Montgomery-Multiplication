P = 10**9 + 7
r = 2**32
r2 = r * r % P
Pinv = pow(-P, -1, r) # (-P^-1) % r

def m_reduce(ab):
  m = ab * Pinv % r
  return (ab + m * P) // r

def m_transform(a):
  return m_reduce(a * r2)

# Example of how to use it
a = 123456789
b = 35
a_prim = m_transform(a) # mult a by 2^32
b_prim = m_transform(b) # mult b by 2^32
prod_prim = m_reduce(a_prim * b_prim) # divide a' * b' by 2^32
prod = m_reduce(prod_prim) # divide prod' by 2^32
print('%d * %d %% %d = %d' % (a, b, P, prod)) # prints 123456789 * 35 % 1000000007 = 320987587

#POBEIRZ WARTOSC A B ORAZ STALE r 
# Transformuj wartosc A i B na Wartosci montgomeryego  ( )
# Redukuj Ztransformatowane wartosci Montgomeryetgo a,b  < - --- -- - Wynik 

# CODE ==>  https://codeforces.com/blog/entry/103374