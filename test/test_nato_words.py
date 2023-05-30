# Generate a series of tests for the str_to_nato function.
#
# The tests should cover the following cases:
#     - The word "Hello" should return "Hotel Echo Lima Lima Oscar"
#     - The word "Goodbye" should return "Golf Oscar Oscar Delta Bravo Yankee Echo"
#     - The word "Yes" should return "Yankee Echo Sierra"
#     - The word "No" should return "November Oscar"
#     - The word "Mike35" should return "Mike India Kilo Echo Three Five"
#     - The word "123" should return "One Two Three"
#     - The word "hi.74" should return "Hotel India Point Seven Four"
#     - The word "3,2-1" should return "Three Comma Two Dash One"


# Path: tests.py
# Compare this snippet from nato_words.py:
#     >>> str_to_nato("Hello")
#     "Hotel Echo Lima Lima Oscar"
# """

import sys
import os
import pytest

module_path = os.path.abspath(os.path.join('nato_code'))
if module_path not in sys.path:
    sys.path.append(module_path)
print(module_path)

import nato_word



@pytest.mark.parametrize(
    "word, expected",
    [
        ("Hello", "HOTEL ECHO LIMA LIMA OSCAR"),
        ("Goodbye", "GOLF OSCAR OSCAR DELTA BRAVO YANKEE ECHO"),
        ("Yes", "YANKEE ECHO SIERRA"),
        ("No", "NOVEMBER OSCAR"),
        ("Mike35", "MIKE INDIA KILO ECHO THREE FIVE"),
        ("123", "ONE TWO THREE"),
        ("hi.74", "HOTEL INDIA POINT SEVEN FOUR"),
        ("3,2-1", "THREE COMMA TWO DASH ONE"),
    ],
)
def test_word_to_nato(word, expected):
    """Generate the NATO phonetic code words for the letters in a word.

    Args:
        word (str): The word to generate the NATO phonetic code words for.

    Returns:
        str: The NATO phonetic code words for the letters in the word.

    Examples:
        >>> word_to_nato("Hello")
        "Hotel Echo Lima Lima Oscar"
    """
    assert nato_word.word_to_nato(word) == expected

