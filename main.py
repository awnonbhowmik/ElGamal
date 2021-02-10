from random import getrandbits, randint, choice
from sympy.ntheory import isprime

"""cyclic group generator <zp*,x>"""


def cyc_group_gen(g, p):
    E = []
    """create empty set"""
    my_set = set(E)

    for i in range(1, p):
        num = pow(g, i, p)
        my_set.add(num)
    return len(my_set)


def modInverse(a, m):
    x, y, m0 = 1, 0, m

    if m == 1:
        return 0

    while a > 1:
        q = a//m
        t = m
        m = a % m
        a = t
        t = y
        y = x-q*y
        x = t

    if x < 0:
        x += m0

    return x

if __name__=="__main__":
    bits=16
    #NIST_STANDARD=[512,1024,2048]
    while True:
        #p=choice(NIST_STANDARD)
        p=getrandbits(bits)
        if isprime(p):
            print("Bits: {}\np: {}".format(bits,p))
            break
    
    for x in range(1,p):
        if cyc_group_gen(x,p)==p-1:
            E1=x
            break
    
    d=randint(1,p-2)

    E2=pow(E1,d,p)
    print("public key: ({},{},{})\nprivate key: {}\n".format(E1,E2,p,d))

    r=randint(2,p-3)

    msg=input("Enter message: ")
    ascii_lst=[ord(c) for c in msg]

    C1=pow(E1,r,p)

    cipher=[]
    for i in range(len(ascii_lst)):
        C2=pow((pow(E2,r)*ascii_lst[i]),1,p)
        cipher.append(C2)
    
    print("Encrypted message:\n{}\n".format(cipher))

    decipher=[]
    for i in range(len(cipher)):
        dec=pow((modInverse(pow(C1,d),p)*cipher[i]),1,p)
        decipher.append(chr(dec))
    

    print("Decrypted message:\n")
    print(''.join(map(lambda x:str(x),decipher)))