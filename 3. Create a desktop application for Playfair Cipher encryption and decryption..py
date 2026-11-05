k = input("Key: ").upper().replace("J","I")
g = ''.join(dict.fromkeys(''.join(c for c in k if c.isalpha()) + "ABCDEFGHIKLMNOPQRSTUVWXYZ"))
t = ''.join(c for c in input("Text: ").upper().replace("J","I") if c.isalpha())

p, i = "", 0
while i < len(t):
    a, b = t[i], (t[i+1:i+2] or "X")
    i += 2
    if a == b: b = "X"; i -= 1
    p += a + b

def f(s, d):
    o = ""
    for a, b in zip(s[::2], s[1::2]):
        r, c = divmod(g.index(a), 5); R, C = divmod(g.index(b), 5)
        if r == R: c, C = (c+d)%5, (C+d)%5
        elif c == C: r, R = (r+d)%5, (R+d)%5
        else: c, C = C, c
        o += g[r*5+c] + g[R*5+C]
    return o

e = f(p, 1)
print("Encrypted:", e)
print("Decrypted:", f(e, -1))