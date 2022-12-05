# RSA Algorithm for Simple Stenograph - Optimized Version
 
# EXTERNAL MODULES
from PIL import Image
import stepic
from os.path import isfile as isExist
import time

# ALGORITHM - MAIN PROGRAM
print("Welcome to RSA Stenography - Basic Version!")
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
            # a. Request image file to save
            image_save = input("Insert image path to save the encoded images: ")
            # xx. Starting time
            timestart = time.time()
            # b. Insert image paths after validating scheme
            img = Image.open(image_path)
            # j. Convert the message into UTF-8 format:
            message = s.encode()
            # c. Adding messages encrypted on images
            encoded_img = stepic.encode(img, message)
            encoded_img.save(image_save)
            # xx. Finish time
            timefinish = time.time()
            # d. Outputting
            print("")
            print("Result image was written on",image_save)
            print("")
            print("Encryption time:",timefinish-timestart,"second(s).")
            valid = True
        else :
            print("Image file is not exist")
            valid = False
    elif check == 2 :
        image_path = input("Insert image path to decode: ")
        if isExist(image_path):
            # xx. Starting time
            timestart = time.time()
            # a. Image path to analyze stenography after validating
            image = Image.open(image_path)
            # b. Getting words from picture of steganophy
            kata = stepic.decode(image)
            # xx. Finish time
            timefinish = time.time()
            # c. Outputting
            print("")
            print("Result of Decryption:")
            print(kata)
            print("")
            print("Decryption time:",timefinish-timestart,"second(s).")
            valid = True
        else :
            print("Image file is not exist")
            valid = False
    else :
        valid = False
        print("Your input is Invalid!\n")
        check = int(input("Your input : "))