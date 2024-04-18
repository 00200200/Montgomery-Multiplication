## Montgomery-Multiplication
### OIAK - PROJEKT

#### Cel Projektu:
Zrozumienie, implementacja  i przedstawienie algorytmu Montgomery'ego. Opisanie jego użycia w praktyce (przy jakich warunkach oplaca sie go uzywac). Porównanie szybkości różnych podejść. 

#### Narzędzia i technologie:
- C
- Python

#### Plan Realizacji Projektu
- Ogólne zapozanie się z tematem 
- Zrozumienie matematyczne 
- Wypisanie algorytmu w krokach 
- Implementacja w Pythonie w celu lepszego zrozumienia 
- Implementacja C (zwykła i przyspieszona) 
- Badanie szybkosci bez optymalizacji kompilatora (naiwne podejcie, zywkly, przyspieszony) 
- Stworzenie sprawozdania, analiza wynikow i wnioski 


 krok po kroku na przykladzie:
```
a = 3, b = 5, n = 7

r = 2^Ceiling[Log[2, n]] = 8	
rinv = PowerMod[r, -1, n] = 1	#z rozszerzonego algorytmu euklidesa (odwrotnosc modularna)
k = (r * rinv - 1) / n; = (8 * 1 - 1) / 7 = 1
aa = Mod[a * r, n] = 3*8 mod 7 = 3
bb = Mod[b * r, n] = 5*8 mod 7 = 5
x = aa * bb = 3*5 = 15
s = Mod[x * k, r] = 15 * 1 mod 8 = 7 #w programie zamieniamy na & (operacje logiczna and)
t = x + s * n = 15 + 7 * 8 = 71
u = t / r = 71 / 8 = 8

cc = If[u < n, u, u - n] -> !(8 < 7) -> cc = 8 - 7 = 1

c = Mod[cc * rinv, n] = (1 * 1) mod 7 = 1

3*5 mod 7 = 15 mod 7 = 1 <- POPRAWNE
```
