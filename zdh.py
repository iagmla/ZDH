from Crypto.Util import number

''' Illustrates the Zander-Diffie-Hellman key distribution '''

def keygen(psize):
    n = number.getPrime(psize)
    g = 2
    sk = number.getRandomRange(1, n - 1)
    return g, sk, n

def _phase1(g, sk, n):
    return pow(g, sk, n)

def _phase2(phase1A, phase1B, n):
    return pow(phase1A, phase1B, n)

def _phase3(phase1, g, n):
    return pow(phase1, g, n)

def _phase4(pkB, sk, n):
    return pow(pkB, sk, n)

def _phase5(phase4, sk, n):
    return pow(phase4, sk, n)

g, skA, nA = keygen(32)
g, skB, nB = keygen(32)

phase1A = _phase1(g, skA, nA)
phase1B = _phase1(g, skB, nA)
# Exchange
phase2A = _phase2(phase1A, g, nA)
phase2B = _phase2(phase1B, g, nA)
# Arrive at the secret modulus
phase3A = _phase3(phase2B, skA, nA)
phase3B = _phase3(phase2A, skB, nA)
# Exchange
phase4A = _phase4(g, skA, phase3A)
phase4B = _phase4(g, skB, phase3B)
# Arrive at the secret key
phase5A = _phase5(phase4B, skA, phase3A)
phase5B = _phase5(phase4A, skB, phase3B)
print(phase5A, phase5B)
