from termcolor import colored
import os

hashrate = input(colored("Set a Hashrate: ", "white", attrs=["bold"]))
os.system('cls' if os.name == 'nt' else 'clear')
confirmation = input(colored("Set a Hex Confirmation Time: ", "white", attrs=["bold"]))
os.system('cls' if os.name == 'nt' else 'clear')
difficulty = 2**80 / (int(hashrate) * int(confirmation))
target = round(2**224 * 2**80 / difficulty)
hexed = target.to_bytes((target.bit_length() + 7) // 8, "big").hex()
print(colored(f"Numerical: {str(target)}\nHex: {hexed}", "white", attrs=["bold"]))
