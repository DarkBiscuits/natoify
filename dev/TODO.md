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
   - entry/filebrowser to set saveing dir path and filename
   - buttons for encoding and decoding
   - can test encoding/decoding without saving to file
   - checkbox to toggle encryption/decryption off/on
   - dropdown to set code type

 - Create a code language loader
   - Load code dictionaries from text files in package folder - /codes
   - NATO and VULGAR remain embeded in .codes as defaults
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