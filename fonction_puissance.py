def puissance(a, n):
    r = 1
    for _ in range(n):
        r *= a
    return r

print(puissance(2, 5))  # Exemple : 2⁵ = 32
