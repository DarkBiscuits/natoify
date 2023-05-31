from natoify.natoify import Natoify

with open("data/message.txt", "r") as f:
    msg = f.read()

nato = Natoify()

# Encrypted version
nato.set_code("vulgar")
nato_msg = nato.encode(msg)
print(nato_msg)

with open("data/message_vulgar.txt", "w") as f:
    f.write(nato_msg)


