from termcolor import colored
import os

elapsed = input(colored("Elapsed Time: ", "white", attrs=["bold"]))
os.system('cls' if os.name == 'nt' else 'clear')
old = input(colored("Old Target: ", "white", attrs=["bold"]))
os.system('cls' if os.name == 'nt' else 'clear')
target = round(int(old)) * (int(elapsed) / 22))
print(colored(f"Numeric: {str(target)}\nHex: {target.to_bytes((target.bit_length() + 7) // 8, 'big').hex()}"))
