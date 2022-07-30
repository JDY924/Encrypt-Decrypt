import loading
from time import sleep
import os
print("Welcome!")
print("Rules:")
print("You can't paste into the console, but you can copy.")
alphabet = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ "
message = ''
def encrypt():
  global message
  message = input("Enter the message to encrypt:")
  key = input("Enter the key (It needs to be at least 8 numbers & only numbers.) :")
  os.system('clear')
  if int(key)%94 == 0:
    key = 87654321
    print("The key was invalid and was replaced. Your new key is 87654321.")
  encrypt = ""
  for i in message:
    position = alphabet.find(i)
    new_position = (position + int(key))%94
    encrypt = encrypt + alphabet[new_position]
  loader = loading.Loader("Encrypting...").start()
  for i in range(10):
    sleep(0.25)
  loader.stop()
  print(encrypt)
  return encrypt






def decrypt():


  e = open("encrypted_message.txt", "r")
  message = e.read()
  

  
  key = input("Enter the encryption key:")
  encrypt = ""
  for i in message:
    position = alphabet.find(i)
    new_position = (position - int(key))%94
    encrypt = encrypt + alphabet[new_position]
  loader = loading.Loader("Decrypting...").start()
  for i in range(10):
    sleep(0.25)
  loader.stop()
  print(encrypt)





  
while True:
  choice = input("Press e to encrypt or press d to decrypt:")
  if choice == "e":
    e = open("encrypted_message.txt", "w")
    e.writelines(encrypt())
    e.close()
  elif choice == "d":
    decrypt()
  else:
    print("That is not an option. Please type e or d.")
  choice = input("If you want to use this again, press y. Otherwise, the program will end:")
  if choice != "y":
    print("Thank you for using this program.")
    break
# if remainder == 0 then the message is not encrypted
# decrypt 
# error handling 
# place into function

#create text file using user input as the name
#read files to decrypt
