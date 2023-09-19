import random
import os
from colorama import Fore, init
import atexit
os.system("CLS")

DoKey = True
quit = False
init(autoreset=True)

'''Dont steal this, I worked really hard on it - @ItsmeElementus'''

@atexit.register
def stop_pressed():
  if quit == False:
    exec(open('quit.py').read())
  else:
    pass

def Decrypt(phrase, key):
  key = str(key)
  curkey = list(key) * 20000
  count = 0
  newphrase = ""
  for character in phrase:
    letter = ord(character) - int(curkey[count])
    new = chr(letter)
    newphrase += new
    count += 1
  return newphrase

def Encrypt(phrase, key):
  key = str(key)
  curkey = list(key) * 20000
  count = 0
  newphrase = ""
  for character in phrase:
    letter = ord(character) + int(curkey[count])
    new = chr(letter)
    newphrase += new
    count += 1
  return newphrase

print(f"Hello {Fore.GREEN}{os.getlogin()}{Fore.RESET}, Welcome!")
print(
  f"This is the {Fore.BLUE}POWERCRYPTER{Fore.RESET} encryption system that happens to be my brainchild."
)
print(f"Try these commands:{Fore.YELLOW} E, D, quit, help, explain, reset")
print(f"Ver: {Fore.CYAN}1.2")
while True:
  try:
    DoKey = True
    while True:
      EorD = input("Encrpyt or Decrypt: ").upper()
      
      if EorD == "E" or EorD == "D":
        break
      elif EorD == "QUIT":
        quit = True
        break
      elif EorD == "HELP":
        print("This is a encryption system with the goal to be uncrackable")
        print("the 'E' command means encrypt or hide information, it will ask for a key and spit out a seemingly random phrase.")
        print("That random phrase is your phrase but hidden, it can only be found or decyrpted by using the 'D' command")
        print("the 'D' command will ask for the jumbled up phrase, and then a key,")
        print("if you use a different key than the one you inputed, you wont get the original message")
        print("if you have any more problems, fell free to contact me at Elementusgaming@gmail.com")
        print("Have Fun!")
      elif EorD == "EXPLAIN":
        print("This progarm takes your key (12345) and turns it into [1], [2], [3], [4], [5]")
        print("It then takes your phrase (Hello) and turns it into [H], [e], [l], [l], [o]")
        print("It then rotates your phrase by what number coresponds to the character")
        print(f"{Fore.YELLOW}H   e   l   l   o")
        print(f"{Fore.YELLOW}1   2   3   4   5")
        print(f"{Fore.YELLOW}^   ^   ^   ^   ^")
        print(f"{Fore.YELLOW}|   |   |   |   |")
        print(f"{Fore.YELLOW}L   n   q   l   t")
        print("and that is how this system works, enjoy!")
      elif EorD == "RESET":
        os.system("CLS")
      else:
        print(f"{Fore.RED}Error: Not a recognized command")
    if quit:
      os.system('CLS')
      break
    phrase = input("Input Phrase (Limited to 100000 characters): ")
    if phrase == "":
      if EorD == "E":
        phrase = "Hello World"
        print(f"{Fore.RED}Error: Resetting phrase to default (Hello world)")
      if EorD == "D":
        DoKey = False
        print(f"{Fore.RED}Error: Resetting phrase to default")
        key = "12345"
        phrase = "Lnqlt!\qwoh"
    
    else:
      pass
    if DoKey == True:
      key = input("Input Key: ")
      if key == "":
        key = str(random.randint(9999,99999))
        print(f"{Fore.MAGENTA}No key detected, your new key is: {Fore.RESET}{key}")
      
    else:
      print(f"{Fore.RED}Error: No phase inputed from User: Key skipped!")
      
    newkey = ""
    if type(key) == int:
      pass
    else:
      for character in key:
        newkey += str(ord(character))
      key = newkey
  
    if phrase == "":
      print(Fore.RED + "Error: Invalid input try again")
    else:
      if EorD == "E":
        print(f"Your Encrypted message is: {Encrypt(phrase, int(key))}")
      elif EorD == "D":
         print(f"Your Decrypted message is: {Decrypt(phrase, int(key))}")
  except KeyboardInterrupt:
    print("")
    print(Fore.RED + "Saved from a Error, Try Ctrl+Shift+C next time")
  except:
    print(Fore.RED + "Woah, something funky happened, lets try that again")
