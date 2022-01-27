import math
import random 
print("RSA ENCRYPTOR/DECRYPTOR")
print("*****************************************************")
 
#Input Prime Numbers
print("PLEASE ENTER THE 'p' AND 'q' VALUES BELOW:")
p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))
print("*****************************************************")
 
#Check if Input's are Prime
'''THIS FUNCTION AND THE CODE IMMEDIATELY BELOW THE FUNCTION CHECKS WHETHER THE INPUTS ARE PRIME OR NOT.'''
def prime_check(a):
    if(a==2):
        return True
    elif((a<2) or ((a%2)==0)):
        return False
    elif(a>2):
        for i in range(2,a):
            if not(a%i):
                return false
    return True

check_p = prime_check(p)
check_q = prime_check(q)
while(((check_p==False) or (check_q==False))):
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
    check_p = prime_check(p)
    check_q = prime_check(q)

# recursive function for euclid's algorithm
def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)

def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)



             #rsa module


    #calculating n=p*q
n=p*q
r=(p-1)*(q-1)
ne=math.ceil(math.log2(n))
print(n, ':value n' , ne , ':bit encryption')

bitn=2*ne+3
print(bitn, 'val of qubit numb')

    #Carmichael's totient function lcm(p-1,q-1) 
_lambda = int(abs((p-1)*(q-1)) / gcd(p-1,q-1))
print("Carmichael's totient function lcm(p-1,q-1) :", _lambda)
print("*****************************************************")

    #e Value Calculation
    # RANDOM POSSIBLE VALUE OF 'e' BETWEEN 1 and _lambda THAT MAKES (e,_lambda)) COPRIME.'''
err=[]
for i in range(1,r):
    if(gcd(i,r)==1):
        err.append(i)
# random.seed(37)
print(err)
e=int(input("e in array:"))
# e=random.choice(err)

print("The value of e is:",e)


    #find value d
gdc,einv,__=eea(((e) % _lambda),_lambda)    
    # d == e^(-1) mod (_lambda) 
# print(einv,_lambda, 'einv, _lambda')
d=((einv) % _lambda)

print(d, 'value d')
########## KEYS ###############

pub_key=(e,n)
priv_key=(d,n)

######### Encrypting and Dycripting #########

    #ASCII conversion
def to_ascii(text):
    ascii_values = [ord(character) for character in text]
    print(ascii_values, 'ascii values')
    return ascii_values

def from_ascii(asciiarr):
    string = ''.join(map(chr, asciiarr))
    print ("String:", str(string))
    return string


    #encrypting  
def encrypt(pub_key,message):
    e,n = pub_key
    asciiarr = to_ascii(message)
    crypted_m=[]
    for i in asciiarr:
        cm=((int(i)**e) % (n))
        crypted_m.append(cm)
    return crypted_m

def decrypt(priv_key,message):
    d,n = priv_key
    txt=message.split(',')
    asciiarr=[]
    print(txt)
    for i in txt:
        dm=((int(i)**d) % (n))
        asciiarr.append(dm)
    print(asciiarr)
    return from_ascii(asciiarr)


#Choose Encrypt or Decrypt and Print
#Message
message = input("What would you like encrypted or decrypted?(Separate numbers with ',' for decryption):")
print("Your message is:",message)
choose = input("Type '1' for encryption and '2' for decrytion.")
if(choose=='1'):
    enc_msg=encrypt(pub_key,message)
    print("Your encrypted message is:",enc_msg)
elif(choose=='2'):
    print("Your decrypted message is:",decrypt(priv_key,message))
else:
    print("You entered the wrong option.")



