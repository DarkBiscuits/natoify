import os
import sys

module_path = os.path.abspath(os.path.join('../natoify/'))
if module_path not in sys.path:
    sys.path.append(module_path)
print(sys.path)
print(os.getcwd())

from natoify.engine import Natoify
# executed from the natoify/src/natoify directory in terminal

# Encode hello world with every code in the library
nato_msg = ""
nato = Natoify()
codes = nato.list_codes()
codes.sort()
maximum = max(codes, key=len)
chars = len(maximum) + 2
for code in codes:
    nato.set_code(code)
    nato_msg += f"{code:<{chars}}>  "
    nato_msg += nato.encode("hello world!") + "\n"

with open("../../data/hello_nato.txt", "w") as f:
    f.write(nato_msg)
print("Wrote to data/hello_nato.txt")


