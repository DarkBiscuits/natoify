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
     - method to reload/update LIBRARY if code txt is added after program start
