# RSA Algorithm for Simple Stenograph - Optimized Version
 
# EXTERNAL MODULES
from PIL import Image
import stepic
from os.path import isfile as isExist
import time

# ALGORITHM - MAIN PROGRAM
print("Welcome to RSA Stenography - Basic Version!")
print("\nDecide your choice")
print("1. Encrypting Image")
print("2. Decrypting Image\n")
check = int(input("Your input: "))

# Input processing
valid = False
while (not valid):
    if check == 1:
        image_path = input("\033[93mInsert image path to encode \n >> \033[37m")
        if isExist(image_path):
            s = input("\033[93mInsert words to encrypt \n >> \033[37m")
            # a. Request image file to save
            image_save = input("\033[93mInsert image path to save the encoded images \n >> \033[37m")
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
            print("========================  RESULT  ========================")
            print('\033[92m' + "Result messages has succesfully encrypted and written on",image_save)
            print(f"Encryption time: \033[37m{timefinish-timestart} \033[92msecond(s).\n")
            valid = True
        else :
            print('\033[31m' + "Image file is not exist")
            valid = False
    elif check == 2 :
        image_path = input("\033[93mInsert image path to decode \n >> \033[37m")
        if isExist(image_path):
            # xx. Outputting
            print("")
            print("========================  RESULT  ========================")
            print("Get a result....")
            # xx. Starting time
            timestart = time.time()
            # a. Image path to analyze stenography after validating
            image = Image.open(image_path)
            # b. Getting words from picture of steganophy
            kata = stepic.decode(image)
            # xx. Finish time
            timefinish = time.time()
            # c. Outputting
            print('\033[92m' + "\nMessages has succesfully decrypted")
            print(f"Decryption time: \033[37m{timefinish-timestart} \033[92msecond(s).")
            print("Result of Decryption:")
            print('\033[37m' + kata)
            print("")
            with open('Decrypted.txt', 'w') as file:
                file.write(f'{kata}')
            print("The decyypted text is also written on Decrypted.txt\n")
            valid = True
        else :
            print('\033[31m' + "Image file is not exist")
            valid = False
    else :
        valid = False
        print('\033[31m' + "Your input is Invalid!\n")
        check = int(input('\033[37m' + "Your input : "))