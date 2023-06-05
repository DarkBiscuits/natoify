"""
Utilities to encode and decode text messages into NATO phonetic alphabet code words.
"""

import html
import json
import glob
import os


class Natoify:
    """
    Contains the encoders and decoders for NATO phonetic alphabet text messages.

    Attributes:
        codes_by_letter (dict): Dictionary of NATO phonetic code words keyed by letter
        codes_by_word (dict): Dictionary of NATO phonetic code words keyed by word
        CODE_LIBRARY (dict): Dictionary of valid code options
        CODE_LIB_DIR (str): Directory containing code.json files

    Methods:
        encode(message: str) -> str: Encode a message string to NATO phonetic words
        decode(message: str) -> str: Decode a NATO message string into plain English
        encrypt(message: str) -> str: Encrypt after encoding a message to NATO phonetic words
        decrypt(message: str) -> str: Decrypt an encrypted NATO message
        set_code(code: str) -> None: Set the code to use for encoding and decoding
        list_codes() -> list: Generate list of available code libraries
        load_codes(directory: str) -> None: Loads json code libraries from a directory (default: ../code_lib)

    Examples:
        >>> nato = Natoify()
        >>> nato.encode("Hello World!")
        'HOTEL ECHO LIMA LIMA OSCAR  WHISKEY OSCAR ROMEO LIMA DELTA EXCLAMARK'

        >>> nato.decode("HOTEL ECHO LIMA LIMA OSCAR  WHISKEY OSCAR ROMEO LIMA DELTA EXCLAMARK")
        'HELLO WORLD!'

        >>> nato.encode("Hello World!", encrypt=True)
        'KRAMA'

        >>> nato.set_code("GHETTO")
        >>> nato.encode("Hello World!")
        'HOTEL ECHO LIMA LIMA OSCAR  WHISKEY OSCAR ROMEO LIMA DELTA EXCLAMARK'
    """

    # Get current director and path to code_lib directory
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    CODE_LIB_DIR = os.path.join(CURRENT_DIR, "../code_lib")

    CODE_LIBRARY = {}

    def __init__(self):
        """Load the default codes (also sets current code to prevent errors - Default is NATO)."""

        self.codes_by_letter = {}
        self.current_code = ""
        # Load the default codes (also sets current code to prevent errors - Default is NATO)
        self.load_codes(self.CODE_LIB_DIR)
        # Generate dictionary of phonetic code words keyed by word (reverse of codes_by_letter)
        self.codes_by_word = self._codes_by_word(self.codes_by_letter)

    def _codes_by_word(self, codes_by_letter: dict) -> dict:
        """
        Returns the reverse of the key, value pairs in codes_by_letter for 
        simplified decode lookup.

        Args:
            codes_by_letter (dict): Dictionary of NATO phonetic code words keyed by letter

        Returns:
            codes_by_word (dict): Dictionary of NATO phonetic code words keyed by word
    
        """

        by_words = {value: key for (key, value) in codes_by_letter.items()}
        by_words["STOP"] = "."
        return by_words

    def _ultimately_unescape(self, s: str) -> str:
        """A relentless loop for cleaning out web encoding from a string.
        
        Args:
            s (str): The string to clean up

        Returns:
            s (str): The cleaned up string
        
        """

        unescaped = ""
        while unescaped != s:
            s = html.unescape(s)
            unescaped = html.unescape(s)
        return s

    def _clean_message(self, message: str) -> str:
        """
        Cleans up a message string before encoding or decoding.
        Attempts to remove any web encoding and non-ascii characters.

        Args:
            message (str): The message to clean up

        Returns:
            cleaned (str): The cleaned up message
        
        """

        cleaned = message.strip()
        # Try removing web encoding
        message = self._ultimately_unescape(message)
        if not message.isascii():
            cleaned = "".join(char for char in message if char.isascii())
        return cleaned

    def load_codes(self, directory: str = "") -> None:
        """
        Loads custom code libraries from a directory containing code.json files.
        The code.json file contains a json object of letter:word pairs.

        Expected JSON: {"NATO": {"A": "ALPHA", "B": "BRAVO", ...}}

        Args:
            directory (str): The directory containing the code.json files. Defaults to "../code_lib"

        Examples:
            >>> nato = Natoify()
            >>> nato.load_codes("../code_lib")
            >>> nato.list_codes()
            ['NATO', 'GHETTO', 'REDNECK', 'HARRYPOTTER', 'STARWARS']
        """

        # Check if directory is empty
        if directory == "":
            directory = self.CODE_LIB_DIR

        # Get a list of all the json files in the directory
        json_files = glob.glob(f"{directory}/*.json")

        # If there is a problem with the directory, raise an error
        if len(json_files) == 0:
            raise FileNotFoundError(f"No code.json files found in: {directory}")

        # Iterate through each file and load the codes
        for json_file in json_files:
            with open(json_file, "r") as f:
                codes = json.load(f)
                # Check if the file contains a valid code library
                # TODO: Add more validation

                # Check for duplicate code names
                if not codes.keys() <= self.CODE_LIBRARY.keys():
                    # Add the code to the CODE_LIBRARY dictionary
                    self.CODE_LIBRARY.update(codes)
        
        # Set the code library to NATO or the first code in the library
        self.reset_current_code()

    def reset_current_code(self) -> None:
        """Set the code to the first code in the library 
        if NATO is not available (user set custom directory)
        """

        if "NATO" not in self.CODE_LIBRARY.keys():
            self.set_code(self.list_codes()[0])
        else:
            self.set_code("NATO")

    def list_codes(self) -> list:
        """Generate list of available code library names
        
        Returns:
            c_list (list): List of available code library names
        
        """

        c_list = [code for code in self.CODE_LIBRARY.keys()]
        c_list.sort()
        return c_list

    def set_code(self, code: str = "NATO") -> None:
        """
        Sets the code to use for encoding and decoding.
        Valid options are "NATO"(default), "GHETTO", etc..

        Args:
            code (str): The code type to use for encoding and decoding

        Raises:
            ValueError: If code type is not a valid option

        Examples:
            >>> nato = Natoify()
            >>> nato.set_code("NATO")
            >>> nato.encode("Hello World!")
            'HOTEL ECHO LIMA LIMA OSCAR  WHISKEY OSCAR ROMEO LIMA DELTA EXCLAMARK'
        """

        code = code.upper()
        if code not in self.CODE_LIBRARY.keys():
            self.reset_current_code()
            print("Invalid code library name. Library does not exist.")
        else:
            self.codes_by_letter = self.CODE_LIBRARY[code]
            self.codes_by_word = self._codes_by_word(self.codes_by_letter)
            self.current_code = code

    def encode(self, message: str, encrypt: bool = False) -> str:
        """Encode a message string to NATO phonetic words. Code used
        is stored in self.current_code.
        
        Args:
            message (str): The message to encode
            encrypt (bool): Encrypt the message after encoding. Defaults to False

        Raises:
            ValueError: If message is empty or None

        Examples:
            >>> nato = Natoify()
            >>> nato.encode("Hello World!")
            'HOTEL ECHO LIMA LIMA OSCAR  WHISKEY OSCAR ROMEO LIMA DELTA EXCLAMARK'
        """

        # Catch empty message
        if message == "" or message == None:
            raise ValueError("Message cannot be empty")

        # Clean up message, remove non-ascii characters, and convert to uppercase
        message = self._clean_message(message)
        message = message.upper()
        message += " "  # Add a space to prevent out of index errors

        # Initialize the NATO message variable
        nato_message = ""

        # Iterate through each character in the message and translate to NATO word
        for i, char in enumerate(message):
            # Check if character is a period
            if char == ".":
                # Check if period is at end of sentence
                if message[i + 1] == " " or message[i + 1] == "\n":
                    nato_message += "STOP "
                else:
                    # Period is part of a number or abbreviation
                    nato_message += self.codes_by_letter[char] + " "

            # Only add a single space if character is a space
            elif char == " ":
                nato_message += " "
            else:
                # Translate character into NATO word
                nato_message += self.codes_by_letter[char] + " "

        # Remove trailing space
        nato_message = nato_message.strip()

        # Encrypt message if encrypt is True
        if encrypt:
            nato_message = self.encrypt(nato_message)

        return nato_message

    def decode(self, message: str, decrypt: bool = False) -> str:
        """Decode a NATO message string into plain English. Code used
        is stored in self.current_code.

        If message was not encoded or incorrect code library is set,
        it will return a error string or a few random words that matched.

        Args:
            message (str): The message to decode
            decrypt (bool, optional): Decrypt the message before decoding. Defaults to False.

        Raises: 
            ValueError: If message is empty or None

        Returns:
            str: The decoded message

        Examples:
            >>> nato = Natoify()
            >>> nato.set_code("NATO")
            >>> nato.decode("HOTEL ECHO LIMA LIMA OSCAR  WHISKEY OSCAR ROMEO LIMA DELTA EXCLAMARK")
            'HELLO WORLD!'
        """

        # Catch empty message
        if message == "" or message == None:
            raise ValueError("Message cannot be empty")

        # Decrypt message if decrypt is True
        if decrypt:
            message = self.decrypt(message)

        # Ensure message is uppercase
        message = message.upper()

        # Initialize the decoded message variable
        decoded_msg = ""

        # Split message into a list of lines (list containing a string)
        lines = message.split("\n")

        # Split each line's string into a list of code word
        # groups that represent a single word
        lines = [line.split("  ") for line in lines]

        # Decode each line (list containing lists of code word groups)
        for line in lines:
            # Strip whitespace from each word group(of symbols (code words))
            line = [word.strip() for word in line]
            decoded_line = ""  # Collects a decoded line of words

            # Decode each group of symbols (that form a word)
            for word in line:
                symbols = word.split(" ")
                word = [
                    self.codes_by_word.get(symbol) for symbol in symbols if symbol != ""
                ]
                word = [w for w in word if w != None]
                
                # Check if word is not empty before joining
                if len(word) != 0:
                    word = "".join(word) + " "
                    # Append decoded word to decoded line
                    decoded_line += word

            # Append decoded line to decoded message
            if decoded_line != "":
                decoded_msg += decoded_line.strip() + "\n"

        # Remove trailing newline
        if decoded_msg != "":
            decoded_msg = decoded_msg.strip()

        # Check for empty message
        if decoded_msg == "":
            decoded_msg = "ERROR: Message was either not NATOIFY encoded or code library was not set correctly"

        return decoded_msg

    def encrypt(self, message: str) -> str:
        """Encrypt a message by reversing the message string
        TODO - Add a real encryption method
        """
        msg = message[::-1]
        return msg

    def decrypt(self, message: str) -> str:
        """Decrypt a message by reversing the message string
        TODO - Add a real decryption method
        """
        msg = message[::-1]
        return msg
