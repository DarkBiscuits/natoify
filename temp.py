from natoify.natoify import Natoify

with open("data/ChatGPT-4 Story Telling.txt", "r") as f:
    msg = f.read()

nato = Natoify()

# Unencrypted version
# nato_msg = nato.encode(msg)
# print(nato_msg[0:100])

# with open("data/ChatGPT-4_Story_Telling_NATO.txt", "w") as f:
#     f.write(nato_msg)

# Encrypted version
nato_msg = nato.encrypt(msg)
print(nato_msg[0:100])

with open("data/ChatGPT-4_Story_NATO_ENCRYP.txt", "w") as f:
    f.write(nato_msg)

# eng_msg = nato.decode(nato_msg)
# print(eng_msg)
