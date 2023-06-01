import os
import sys

module_path = os.path.abspath(os.path.join('../natoify/'))
if module_path not in sys.path:
    sys.path.append(module_path)
print(sys.path)
print(os.getcwd())

from natoify.engine import Natoify

with open("../../data/message.txt", "r") as f:
    msg = f.read()

nato = Natoify()

# Encrypted version
nato.set_code("vulgar")
nato_msg = nato.encode(msg)
print(nato_msg)

# with open("data/message_vulgar.txt", "w") as f:
#     f.write(nato_msg)
# print("Wrote to data/message_vulgar.txt")


