"""
A utility to encode and decode text messages into NATO phonetic alphabet code words.
"""

import html

class Natoify:
    """
    Contains the encoders and decoders for text messages.
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

    def _clean_message(self, message: str) -> str:
        """
        Cleans up a message string before encoding or decoding.
        Attempts to remove any web encoding and non-ascii characters.
        """
        cleaned = message
        # Try removing web encoding
        message = html.unescape(message)
        if not message.isascii():
            cleaned = ''.join(char for char in message if char.isascii())
        return cleaned
    
    def encode(self, message: str) -> str:
        """Convert a message string to NATO words
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
        pass

    def encrypt(self, message: str) -> str:
        pass

    def decrypt(self, message: str) -> str:
        pass
