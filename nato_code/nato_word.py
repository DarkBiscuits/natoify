"""
This module contains a function that generates the NATO phonetic code words for each letter
in a word. If run as a script, the user can enter a word to get a list of the NATO phonetic 
code words for each of its letters in the console.

Attributes:
    nato_dict (dict): A dictionary containing the NATO phonetic code words for each letter
        and number.

Methods:
    str_to_nato(word: str) -> str: Generate the NATO phonetic code words for a words letters.
    main(): Commandline version of str_to_nato(). 

Example:
    >>> str_to_nato("Hello")
    "Hotel Echo Lima Lima Oscar"
"""

from nato_lib import nato_codes

def char_to_nato(char: str) -> str:
    """Generate the NATO phonetic code word for a character.

    Args:
        char (str): The character to generate the NATO phonetic code word for.

    Returns:
        str: The NATO phonetic code word for the character.

    Examples:
        >>> char_to_nato("H")
        "Hotel"
    """
    return nato_codes[char.upper()]

def word_to_nato(word: str) -> str:
    """Generate the NATO phonetic code words for the letters in a word.

    Args:
        word (str): The word to generate the NATO phonetic code words for.

    Returns:
        str: The NATO phonetic code words for the letters in the word.

    Examples:
        >>> word_to_nato("Hello")
        "Hotel Echo Lima Lima Oscar"
    """
    nato_words = [nato_codes[letter] for letter in word.upper()]
    return " ".join(nato_words)


def main():
    """Generate the NATO phonetic code words for a word entered by the user (CLI Version)."""
    print("\nWelcome to the NATO Phonetic Alphabet Converter")
    print(
        "Enter a word to get a list of the NATO phonetic code words for each of its letters."
    )
    print("")
    word = input("Enter a word: ")

    # Generate the NATO phonetic code words for the word and print the result
    print(word_to_nato(word))
    print("")


if __name__ == "__main__":
    main()
