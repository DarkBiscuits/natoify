# TODO Items

 - Test decode to seel what happens when it tries to decode a non-nato message
 - Make decode fail gracefully and notify the user when a message is not nato
  - return an error string? "Decoding failed, seems that message was not NATO"
 - wait until desktop app or cli? Easier to see what's happening and error msgs.

 - Create a CLI script using Click
   - needs input file (message) as default
   - default output is to screen (can be piped > to file on cli)
     - find out if that is done by shell or '> filename' becomes argument passed to program
     - if > filename is given, no output to cli screen
   - option to save to same directory as message with _nato added to filename (-s --save)
     - will save to output dir and filename if given
   - option to specify decoding (-d --decode) encoding is default
   - option to specify code type (NATO or VULGAR, -n --nato -v --vulgar)
   - option to encrypt with encoding (-e --encrypt)
   - option to decrypt with decoding (-u -unencrypt)
   - option to show cli help (-h --help)
 
 - Create desktop app using customtkinter
   - can open a text file, cut/paste into text area, or type in place
   - button to select file with filebrowser
   - entry/filebrowser to set saving dir path and filename
   - buttons for encoding and decoding
   - can test encoding/decoding without saving to file
   - checkbox to toggle encryption/decryption off/on
   - dropdown to set code type

 - Create a code language loader
   - Load code dictionaries from text files in package folder - /codes
   - NATO and GHETTO remain embedded in .codes as defaults
   - method to load, verify, and store additional codes from /codes
   - adds code types to existing CODE_OPTIONS attribute for use
   - codes are loaded as python dictionaries into a main dictionary
     - keys will be the names used in CODE_OPTIONS for selection
     - add all codes to LIBRARY dictionary at class creation (__init__)
     - set_code() uses LIBRARY to set working code variables
     - all methods created in codes.py - codes class?
     - method to reload/update LIBRARY if code txt is added after program start`

- Theme ideas
  - pirates of the caribbean movies
  - stinky jobs
  - dracula
  - zombie movies
  - nasa
  - native american 
  - pets
  - dating
  - mountain men
  - presidents
  - africa
  - europe
  - america
  - australia
  - england
  - eddie murphy
  - caveman
  - pokemon
  - ninjas
  - heavy metal music artists
  - pop music artists
  - country music artists
  - unusual towns
  - chemistry
  - dog breeds
  - famous explorers
  - nicknames
  - narnia
  - gatsby
  - davinci code
  - asimov
  - bladerunner
  - madmax

1. CARLIN (George Carlin)
2. CHAPPELLE (Dave Chappelle)
3. ROCK (Chris Rock)
4. SEINFELD (Jerry Seinfeld)
5. BURR (Bill Burr)
6. GAD (Gad Elmaleh)
7. C.K. (Louis C.K.)
8. MULANEY (John Mulaney)
9. SILVERMAN (Sarah Silverman)
10. KLEIN (Robert Klein)

1. Friends
2. Game of Thrones
3. The Office (US)
4. Breaking Bad
5. Stranger Things
6. The Big Bang Theory
7. The Crown
8. Grey's Anatomy
9. Narcos
10. The Walking Dead

1. MONSTER MADNESS - Words inspired by classic movie monsters like Dracula, Frankenstein, and the Wolfman.
2. PIZZA PARTY - Words inspired by everyone's favorite food, pizza, such as pepperoni, cheesy, and crusty.
3. UNICORN UNIVERSE - Words inspired by magical and mythical creatures like unicorns, dragons, and fairies.
4. SPAGHETTI WESTERN - Words inspired by classic western films, but with a twist - they're all spaghetti westerns! Think Clint Eastwood and Ennio Morricone.
5. CANDY CRAZE - Words inspired by every sugary treat you can imagine, from lollipops to chocolate bars to gummy worms.
6. 80s ACTION - Words inspired by the over-the-top action movies of the 1980s, like Rambo, Robocop, and Die Hard.
7. ALIEN ABDUCTION - Words inspired by aliens, spaceships, and otherworldly phenomena, like Roswell, abduction, and UFO.
8. RAINBOW RENAISSANCE - Words inspired by every color of the rainbow, including indigo, violet, magenta, and chartreuse.
9. PIRATE PARADISE - Words inspired by pirates, their ships, and their treasure, like Captain Hook, Jolly Roger, and pieces of eight.
10. PENGUIN PALOOZA - Words inspired by our tuxedoed friends, including waddling, flippers, and rookeries.

- scarface
- fastandfurious
- riddick
- pulpfiction
- terminator
- facebook
- twitter
- instagram
- killbill
- jackreacher
- johnwick

## Old Readme Text

What started as a simple coding challenge while taking a basic Python course has 
gone horribly wrong...thanks to Github Copilot and chatGPT. AI tools
made it easy to continue building out a simple script into a full blown program, 
complete with cli interface and windowed desktop app. What does it do?

Natoify encodes/decodes plain text messages using a NATO-style phonetic alphabet as a key.
In standard NATO speak: A=ALFA, B=BRAVO, C=CHARLIE, D=DELTA, etc. 
Each letter in the message is matched to its corresponding word from the selected
code library and it then outputs an encoded message in plain text. Decoding a message, the
text is searched for matching code words and they are replaced with the proper letter
(or number/punctuation). Encoding results in a message with no special characters or
numbers, only uppercase letters in the form of groups of words. Decoding reveals the
original message, complete with numbers and special characters.

This python package includes the basic encoder and decoder (engine.py) along
with a cli program (natocli.py) and a desktop app (natoapp.py) based on the
customtkinter library (cross-platform).

The cli program allows you to specify an input text file and an output text file for
the resulting encoded or decoded message. It has some utility options to list 
available code libraries, set a specific code library for encoding/decoding, 
encrypt/decrypt in addition to encoding/decoding, and a repl loop allowing you
to experiment by typing text to input and seeing the resulting output immediately, along with
the ability to switch code libraries and toggle encryption as you go. Great for playing with
options before passing files through. Running it as a chain in your favorite shell
also lets you to omit the input, output, or both, allowing it to be used to pipe (|) 
cli output to/from other programs through it for conversion.

The desktop app allows you to load a text message, choose a code library, toggle 
encoding/decoding/encryption/decryption options, and view the result. You can load and 
install additional code libraries as well. The playground tab gives you a place to play 
with typing input text and immediately viewing the output, encode a word or sentence using 
all available code libraries at once for comparison (and as a way to see the results of all libraries), and even includes a GPT mode where you can chat with chatGPT (3.5 turbo). GPT was used to generate almost all the included libraries (113 at last count) and is great for creating a code library based on your own custom theme. There is also a code editor tab where code
library files can be loaded, edited, copies saved, etc. The desktop app is built using
customtkinter, a modern styled gui framework based on tkinter, and should work on any
platform.