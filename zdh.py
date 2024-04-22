from Crypto.Util import number

''' Illustrates the Zander-Diffie-Hellman key distribution '''

def keygen(psize):
    n = number.getPrime(psize)
    pk = number.getRandomRange(1, n - 1)
    sk = number.getRandomRange(1, n - 1)
    return pk, sk, n

def _phase1(pkA, pkB, n):
    return pow(pkA, pkB, n)

def _phase2(phase1A, phase1B, n):
    return pow(phase1A, phase1B, n)

def _phase3(phase1, pk, n):
    return pow(phase1, pk, n)

def _phase4(pkB, sk, n):
    return pow(pkB, sk, n)

def _phase5(phase4, sk, n):
    return pow(phase4, sk, n)

pkA, skA, nA = keygen(32)
pkB, skB, nB = keygen(32)

phase1A = _phase1(pkA, skA, nA)
phase1B = _phase1(pkA, skB, nA)
phase2A = _phase2(phase1A, pkA, nA)
phase2B = _phase2(phase1B, pkA, nA)
# First exchange derives the secret modulus
phase3A = _phase3(phase2B, skA, nA)
phase3B = _phase3(phase2A, skB, nA)
phase4A = _phase4(pkB, skA, phase3A)
phase4B = _phase4(pkB, skB, phase3B)
# Second exchange derives the secret key
phase5A = _phase5(phase4B, skA, phase3A)
phase5B = _phase5(phase4A, skB, phase3B)
print(phase5A, phase5B)
