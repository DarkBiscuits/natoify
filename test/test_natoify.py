# Tests for the natoify module

import sys
import os
import pytest

module_path = os.path.abspath(os.path.join('.'))
if module_path not in sys.path:
    sys.path.append(module_path)
# print(module_path)

from natoify.natoify import Natoify

nato = Natoify()

# @pytest.fixture
# def nato_output():
nato_output = "TANGO HOTEL INDIA SIERRA  INDIA SIERRA  ALFA  TANGO ECHO SIERRA TANGO  MIKE ECHO SIERRA SIERRA ALFA GOLF ECHO STOP  ONE TWO THREE FOUR STOP  SIERRA TANGO OSCAR PAPA"
nato_out_lower = "tango hotel india sierra  india sierra  alfa  tango echo sierra tango  mike echo sierra sierra alfa golf echo stop  one two three four stop  sierra tango oscar papa"
nato_out_encrypt = "APAP RACSO OGNAT ARREIS  POTS RUOF EERHT OWT ENO  POTS OHCE FLOG AFLA ARREIS ARREIS OHCE EKIM  OGNAT ARREIS OHCE OGNAT  AFLA  ARREIS AIDNI  ARREIS AIDNI LETOH OGNAT"
symb_output = "EXCLAMARK AT HASHTAG DOLLARSIGN PERCENT CARET AMPERSAND ASTERISK LEFTPAREN RIGHTPAREN UNDERSCORE PLUS EQUAL DASH APOSTROPHE QUOTMARK COLON SEMICOLON QUESTMARK SLASH POINT COMMA GREATERTHAN LESSTHAN BACKSLASH PIPE BACKTICK TILDE LEFTSQUARE RIGHTSQUARE LEFTCURLY RIGHTCURLY"
numb_output = "ONE TWO THREE FOUR FIVE  SIX SEVEN EIGHT NINE ZERO"

def test_nato_encode():
    """Test the encode function
    """
    # Test message
    message = "This is a test message. 1234. STOP"
    nato_message = nato.encode(message)
    assert nato_message == nato_output

def test_nato_decode():
    """Test the decode function
    """
    # Test message
    nato_message = nato_output
    message = nato.decode(nato_message)
    assert message == "THIS IS A TEST MESSAGE. 1234. STOP"

def test_nato_encrypt():
    """Test the encrypt function
    """
    # Test message
    message = "This is a test message. 1234. STOP"
    nato_message = nato.encode(message, encrypt=True)
    assert nato_message == nato_out_encrypt

def test_nato_decrypt():
    """Test the decrypt function
    """
    # Test message
    nato_message = nato_out_encrypt
    message = nato.decode(nato_message, decrypt=True)
    assert message == "THIS IS A TEST MESSAGE. 1234. STOP"

def test_nato_encode_empty():
    """Test the encode function with an empty message
    """
    # Test message
    with pytest.raises(ValueError):
        nato.encode("")

def test_nato_decode_empty():
    """Test the decode function with an empty message
    """
    # Test message
    with pytest.raises(ValueError):
        nato.decode("")

def test_nato_encode_none():
    """Test the encode function with a None message
    """
    # Test message
    with pytest.raises(ValueError):
        nato.encode(None)

def test_nato_decode_none():
    """Test the decode function with a None message
    """
    # Test message
    with pytest.raises(ValueError):
        nato.decode(None)

def test_nato_encode_symbols():
    """Test the encode function with symbols
    """
    # Test message
    message = "!@#$%^&*()_+=-'\":;?/.,><\\|`~[]{}"
    nato_message = nato.encode(message)
    assert nato_message == symb_output

def test_nato_decode_symbols():
    """Test the decode function with symbols
    """
    # Test message
    nato_message = symb_output
    message = nato.decode(nato_message)
    assert message == "!@#$%^&*()_+=-'\":;?/.,><\\|`~[]{}"

def test_nato_encode_numbers():
    """Test the encode function with numbers
    """
    # Test message
    message = "12345 67890"
    nato_message = nato.encode(message)
    assert nato_message == numb_output

def test_nato_decode_numbers():
    """Test the decode function with numbers
    """
    # Test message
    nato_message = numb_output
    message = nato.decode(nato_message)
    assert message == "12345 67890"

def test_nato_encode_uppercase():
    """Test the encode function with uppercase letters
    """
    # Test message
    message = "THIS IS A TEST MESSAGE. 1234. STOP"
    nato_message = nato.encode(message)
    assert nato_message == nato_output

def test_nato_decode_uppercase():
    """Test the decode function with uppercase letters
    """
    # Test message
    nato_message = nato_output
    message = nato.decode(nato_message)
    assert message == "THIS IS A TEST MESSAGE. 1234. STOP"

def test_nato_encode_lowercase():
    """Test the encode function with lowercase letters
    """
    # Test message
    message = "this is a test message. 1234. stop"
    nato_message = nato.encode(message)
    assert nato_message == nato_output

def test_nato_decode_lowercase():
    """Test the decode function with lowercase letters
    """
    # Test message
    nato_message = nato_out_lower
    message = nato.decode(nato_message)
    assert message == "THIS IS A TEST MESSAGE. 1234. STOP"


