# RSA Algorithm for Simple Stenograph - Optimized Version
 
# EXTERNAL MODULES
import random
from PIL import Image
import stepic
from os.path import isfile as isExist
import time

# FUNCTIONS
# 1. Random prime number generator
def primeNumberGenerator():
    num = random.randint(2, 1000)
    # Checking whether the random integer is prime or not
    for i in range(2,num):
        if (num % i) == 0:
            return primeNumberGenerator()
    return num

# 2. GCD of two numbers
def gcd(p,q):
    while q != 0:
        p, q = q, p % q
    return p

# 3. Co-prime to a number generator
def coprimeGenerator(num):
    m = random.randint(2, 1000)
    if gcd(num, m) != 1:
        return coprimeGenerator(num)
    else :
        return m

# 4. EGCD of 2 numbers
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
    
# 5. Modulo Inverse
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m
    
# 6. Encrypting Code
def Encrypt(image_path, s):
    # xx. Starting time
    timestart = time.time()
    
    # a. Defining 2 number, relatively prime
    p = primeNumberGenerator()
    q = primeNumberGenerator()

    # b. Validating is 2 number is same and setup for p and q value
    sama = (p == q)
    while (sama):
        q = primeNumberGenerator()
        sama = (p == q)
        
    if (p < q):
        # Swap procedure
        temp = q
        q = p
        p = temp

    # c. Setup value of m and n
    n = p * q
    m = (p -1) * (q - 1)

    # d. Choosing e
    e = coprimeGenerator(m)

    # e. Insert image paths after validating scheme
    img = Image.open(image_path)
    
    # f. Convert every single alphabet in string to ASCII
    list = [ord(c) for c in s]
    
    # g. Encrypt the code
    plt = [0 for i in range (len(list))]
    for i in range (len(list)):
        plt[i] = int((list[i] ** e) % n)

    # h. Encrypted words
    res1 = ""
    for i in plt:
        res1 = res1 + chr(i)
        
    # i. Encrypted codes
    res = ""
    for i in plt:
        res = res + str('{:06}'.format(i))
        
    # j. Convert the message into UTF-8 format:
    message = res.encode()
    
    # k. Adding messages encrypted on images
    encoded_img = stepic.encode(img, message)
    
    # xx. Finish time
    timefinish = time.time()
    
    # l. Request image file to save
    image_save = input("Insert image path to save the encoded images: ")
    encoded_img.save(image_save)
    
    # m. Outputting
    print("")
    print("Here is your private key")
    print("n =",n,"e =",e)
    print("")
    print("Save this key whenever you want to decrypt the words!")
    with open('Encrypted.txt', 'w') as file:
        file.write(f'{res}')
    print("Result image was written on",image_save)
    print("The text result is also written on Encrypted.txt\n")
    print("Encryption time:",timefinish-timestart,"second(s).")

# 7. Decrypting Code   
def Decrypt(image_path, n, e):
    # xx. Starting time
    timestart = time.time()
    
    # a. Image path to analyze stenography after validating
    image = Image.open(image_path)
    
    # b. Getting words from picture of steganophy
    kata = stepic.decode(image)
    
    # c. Splitting the input to array
    array = ['' for i in range (int(len(kata)/6))]

    # d. Parsing the input into few segments
    i = 0
    while i < int(len(kata)):
        array[int(i/6)] = kata[i:i+6]
        i += 6
        
    # e. Converting to integer, Raising error management
    arrayint = [0 for i in range (len(array))]

    for i in range (len(array)):
        try:
            arrayint[i] = int(array[i])
        except ValueError:
            raise ValueError("There\'s no secret found here")
    
    # f. Setup value of m using n input
    for i in range(2,n):
        if (n % i == 0):
            p = i
            
    q = n // p
    m = (p - 1) * (q - 1)
    
    # g. Choosing decription key, fulfilled ed = 1 (mod m)
    d = modinv(e, m)
    
    # h. Decrypting process
    fin = [0 for i in range (len(arrayint))]
    
    for i in range (len(arrayint)):
        fin[i] = int((arrayint[i] ** d) % n)
    
    # i. Resulting the decryption process
    res = ""
    for i in fin :
        res = res + chr(i)
        
    # xx. Finish time
    timefinish = time.time()
    
    # j. Outputting
    print("")
    print("Result of Decryption:")
    print(res)
    print("")
    print("Decryption time:",timefinish-timestart,"second(s).")
    
# ALGORITHM - MAIN PROGRAM
print("Welcome to RSA Stenography - Optimized Version!")
print("Decide your choice")
print("1. Encrypting Image")
print("2. Decrypting Image\n")
check = int(input("Your input: "))

# Input processing
valid = False
while (not valid):
    if check == 1:
        image_path = input("Insert image path to encode: ")
        if isExist(image_path):
            s = input("Insert words to encrypt: \n")
            Encrypt(image_path,s)
            valid = True
        else :
            print("Image file is not exist")
            valid = False
    elif check == 2 :
        image_path = input("Insert image path to decode: ")
        if isExist(image_path):
            n = int(input("Insert the n value: "))
            e = int(input("Insert the public key: "))
            Decrypt(image_path,n,e)
            valid = True
        else :
            print("Image file is not exist")
            valid = False
    else :
        valid = False
        print("Your input is Invalid!\n")
        check = int(input("Your input : "))