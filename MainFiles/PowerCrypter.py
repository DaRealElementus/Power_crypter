import random
import os
from colorama import Fore, init
import atexit
import subprocess
import sys
import time
os.system("CLS")

debug = False
DoKey = True
quit = False
init(autoreset=True)

'''Dont steal this, I worked really hard on it - @ItsmeElementus'''

def stop_pressed():
  try:
    if quit == False:
      print("Executing quit.py")
      subprocess.call([sys.executable, "quitting.py"])
      time.sleep(1)
  except Exception as e:
    print(f"Error executing quitting.py: {e}")

def Decrypt(phrase, key, debug):
  key = str(key)
  curkey = list(key) * 20000
  count = 0
  newphrase = ""
  for character in phrase:
    letter = ord(character)
    if letter == 53384:
      character = 127
    else:
      pass
    letter -= int(curkey[count])
    new = chr(letter)
    newphrase += new
    if debug == True:
      print(f"{character}({ord(character)}) - {curkey[count]} = {new} : total phrase = {newphrase} : count = {count}")
    count += 1

  return newphrase

def Encrypt(phrase, key, debug):
  key = str(key)
  curkey = list(key) * 20000
  count = 0
  newphrase = ""
  for character in phrase:
    letter = ord(character) + int(curkey[count])
    if letter == 127:
      letter = 53384
    else:
      pass
    new = chr(letter)
    newphrase += new
    if debug == True:
      print(f"{character}({ord(character)}) + {curkey[count]} = {new} : total phrase = {newphrase} : count = {count}")
    count += 1
    
  return newphrase
def main():
  global quit
  global debug
  print(f"Hello {Fore.GREEN}{os.getlogin()}{Fore.RESET}, Welcome!")
  print(
    f"This is the {Fore.BLUE}POWERCRYPTER{Fore.RESET} encryption system that happens to be my brainchild."
  )
  print(
    "Note: Ascii is dumb and PowerCrypter does not have an ascii range limit (thats why its so safe),\nthis can cause some data loss, use at your own risk"
    )
  print(
    f"Try these commands:{Fore.YELLOW} E, D, quit, help, explain, reset"
    )
  print(
    f"Ver: {Fore.CYAN}1.8"
    )
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
          print(f"{Fore.YELLOW}I   g   o   p   t")
          print("and that is how this system works, enjoy!")
          print("Data loss is caused when UTF-8 Characters are shuffled into key presses, eg 127 = DEL key. I hate this and wish it to dissapear but it is nessecary for I.T. to work")
        elif EorD == "RESET":
          os.system("CLS")
        elif EorD == "DEBUG.UNPACK":
          debug = True
          print(f"toggled debug: {str(debug).upper()}")
        elif EorD == "DEBUG.ERROR":
          raise SystemExit
        elif EorD == "SECRET":
          print(f"Wanna Know a secret? This is a vigenere cypher, it wasn't meant to be one, dont tell anyone, I will know because I know your name, {os.getlogin()}. ")
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
      if DoKey == True:
        key = input("Input Key: ")
        if key == "":
          key = str(random.randint(9999,99999))
          print(f"{Fore.MAGENTA}No key detected, your new key is: {Fore.RESET}{key}")
      else:
        print(f"{Fore.RED}Error: No phase inputed from User: Key skipped!")
      newkey = ""
      try:
        key = int(key)
        newkey = key
      except:
        for character in key:
          newkey += str(ord(character))
        key = newkey
      if phrase == "":
        print(Fore.RED + "Error: Invalid input try again")
      else:
        if EorD == "E":
          print(f"Your Encrypted message is: {Encrypt(phrase, int(key), debug)}")
        elif EorD == "D":
          print(f"Your Decrypted message is: {Decrypt(phrase, int(key), debug)}")
        else:
          print("How did you even get here?")
    except KeyboardInterrupt:
      print("")
      print(Fore.RED + "Saved from a Error, Try Ctrl+Shift+C next time \nIf you want to quit, type 'quit'")
    except SystemExit:
        stop_pressed()
        exit()
    except:
      print(Fore.RED + "Woah, something funky happened, lets try that again")
if __name__ == "__main__":
    main()

atexit.register(stop_pressed)