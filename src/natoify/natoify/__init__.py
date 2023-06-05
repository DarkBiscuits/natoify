"""
The Natoify package contains modules for converting plain text messages into their
NATO phonetic code word equivalents. Each character of the message is converted into
its NATO phonetic code word, ex- "A" becomes "Alpha", "B" becomes "Bravo", etc.
Natoify also supports converting numbers and ascii symbols into their NATO phonetic 
code word equivalents. Includes methods for encoding, decoding, encrypting, and 
decrypting messages. A command line interface and tkinter desktop app is also 
included for easy use. 
"""


from .engine import Natoify
from .natogpt import NatoGPT
