"""
A utility to encode and decode text messages into NATO phonetic alphabet code words.
"""

import html

class Natoify:
    """
    Contains the encoders and decoders for NATO phonetic alphabet text messages.

    Attributes:
        codes_by_letter (dict): Dictionary of NATO phonetic code words keyed by letter
        codes_by_word (dict): Dictionary of NATO phonetic code words keyed by word

    Methods:
        encode(message: str) -> str: Encode a message string to NATO phonetic words
        decode(message: str) -> str: Decode a NATO message string into plain English
        encrpyt(message: str) -> str: Encrypt a message after NATO encoding
        decrypt(message: str) -> str: Decrypt an encrypted NATO message

    Examples:
        >>> nato = Natoify()
        >>> nato.encode("Hello World!")
        'HOTEL ECHO LIMA LIMA OSCAR  WHISKEY OSCAR ROMEO LIMA DELTA EXCLAMARK'
    """

    CODES_BY_LETTER = {
        "A": "ALFA",
        "B": "BRAVO",
        "C": "CHARLIE",
        "D": "DELTA",
        "E": "ECHO",
        "F": "FOXTROT",
        "G": "GOLF",
        "H": "HOTEL",
        "I": "INDIA",
        "J": "JULIET",
        "K": "KILO",
        "L": "LIMA",
        "M": "MIKE",
        "N": "NOVEMBER",
        "O": "OSCAR",
        "P": "PAPA",
        "Q": "QUEBEC",
        "R": "ROMEO",
        "S": "SIERRA",
        "T": "TANGO",
        "U": "UNIFORM",
        "V": "VICTOR",
        "W": "WHISKEY",
        "X": "X-RAY",
        "Y": "YANKEE",
        "Z": "ZULU",
        "0": "ZERO",
        "1": "ONE",
        "2": "TWO",
        "3": "THREE",
        "4": "FOUR",
        "5": "FIVE",
        "6": "SIX",
        "7": "SEVEN",
        "8": "EIGHT",
        "9": "NINE",
        "-": "DASH",
        ",": "COMMA",
        ".": "POINT",
        "@": "AT",
        "?": "QUESTMARK",
        "!": "EXCLAMARK",
        "'": "APOSTROPHE",
        '"': "QUOTMARK",
        "(": "LEFTPAREN",
        ")": "RIGHTPAREN",
        "&": "AMPERSAND",
        ":": "COLON",
        ";": "SEMICOLON",
        "/": "SLASH",
        "\\": "BACKSLASH",
        "+": "PLUS",
        "=": "EQUAL",
        "_": "UNDERSCORE",
        "$": "DOLLARSIGN",
        "%": "PERCENT",
        "#": "HASHTAG",
        "*": "ASTERISK",
        "<": "LESSTHAN",
        ">": "GREATERTHAN",
        "^": "CARET",
        "~": "TILDE",
        "`": "BACKTICK",
        "{": "LEFTCURLY",
        "}": "RIGHTCURLY",
        "[": "LEFTSQUARE",
        "]": "RIGHTSQUARE",
        "|": "PIPE",
        " ": " ",
        "\n": "\n",
        "\t": "\t",
    }


    def __init__(self):
        # Dictionary of NATO phonetic code words keyed by letter
        self.codes_by_letter = self.CODES_BY_LETTER
        # Dictionary of NATO phonetic code words keyed by word
        self.codes_by_word = self._codes_by_word(self.codes_by_letter)

    def _codes_by_word(self, codes_by_letter: dict) -> dict:
        """
        Returns the reverse of the key, value pairs in codes_by_letter for decode lookup.
        """
        by_words = {value: key for (key, value) in codes_by_letter.items()}
        by_words["STOP"] = "."
        return by_words

    def _ultimately_unescape(self, s: str) -> str:
        """A relentless loop for cleaning out web encoding from a string."""
        unescaped = ""
        while unescaped != s:
            s = html.unescape(s)
            unescaped = html.unescape(s)

        return s
    
    def _clean_message(self, message: str) -> str:
        """
        Cleans up a message string before encoding or decoding.
        Attempts to remove any web encoding and non-ascii characters.
        """
        cleaned = message
        # Try removing web encoding
        message = self._ultimately_unescape(message)
        if not message.isascii():
            cleaned = ''.join(char for char in message if char.isascii())
        return cleaned
    

    def encode(self, message: str) -> str:
        """Encode a message string to NATO phonetic words
        """

        # Catch empty message
        if message == '' or message == None:
            raise ValueError('Message cannot be empty')
        
        # Clean up message, remove non-ascii characters, and convert to uppercase
        message = self._clean_message(message)
        message = message.upper()
        message += ' '  # Add a space to prevent out of index errors
        
        # Initialize the NATO message variable
        nato_message = ''

        # Iterate through each character in the message and translate to NATO word
        for i, char in enumerate(message):
            
            # Check if character is a period
            if char == '.': 
                # Check if period is at end of sentence
                if message[i+1] == ' ' or message[i+1] == '\n':
                    nato_message += 'STOP '
                else:
                    # Period is part of a number or abbreviation
                    nato_message += self.codes_by_letter[char] + ' '
            
            # Only add a single space if character is a space
            elif char == ' ':
                nato_message += ' '
            else:
                # Translate character to NATO word
                nato_message += self.codes_by_letter[char] + ' '
        
        return nato_message.strip()  # Remove trailing space


    def decode(self, message: str) -> str:
        """Decode a NATO message string into plain English
        """

        # Catch empty message
        if message == '' or message == None:
            raise ValueError('Message cannot be empty')
        
        # Clean up message, remove non-ascii characters, and convert to uppercase
        message = self._clean_message(message)
        message = message.upper()
        
        # Initialize the decoded message variable
        decoded_msg = ""

        # Split message into a list of lines (list containing a string)
        lines = message.split('\n')
        
        # Split each line's string into a list of code word
        # groups that represent a single word
        lines = [line.split('  ') for line in lines]

        # Decode each line (list containing lists of code word groups)
        for line in lines:
            # Strip whitespace from each word group(of symbols (code words))
            line = [word.strip() for word in line]
            decoded_line = ""  # Collects a decoded line of words
            
            # Decode each group of symbols (that form a word)
            for word in line:
                symbols = word.split(' ')
                word = [self.codes_by_word.get(symbol) for symbol in symbols if symbol != '']
                word = ''.join(word) + ' '
                # Append decoded word to decoded line
                decoded_line += word
            
            # Append decoded line to decoded message
            decoded_msg += decoded_line.strip() + '\n'

        return decoded_msg.strip()  # Remove trailing newline


    def encrypt(self, message: str) -> str:
        """Encrypt a message after NATO encoding by reversing the message string"""
        msg = self.encode(message)
        rev = msg[::-1]
        return rev

    def decrypt(self, message: str) -> str:
        """Decrypt an encoded NATO message by reversing and decoding the message string"""
        rev = message[::-1]
        msg = self.decode(rev)
        return msg
