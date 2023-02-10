def isPrime(x):
    if x < 2:                       # numbers < 2 are not prime
        return False
    if x == 2:                      # 2 is prime
        return True
    for n in range(2,x):            # divide x by all numbers from 2 to x
        if x % n == 0:              # if mod = 0, number not prime
            return False
    return True                     # if number gets there => its prime

def primeGenerator(a,b):
    for i in range(a,b+1):          # b+1 => final number inclued in a list
        if isPrime(i):
            yield i                 # python generator (yield) aka lazy iterator

s = int(input("[INPUT] Enter start number: "))
f = int(input("[INPUT] Enter final number: "))

print("[INFO] List of prime numbers from:",s,"to:",f)
print(list(primeGenerator(s,f)))    # lazy iterator used to print prime number from s to f range in a list
