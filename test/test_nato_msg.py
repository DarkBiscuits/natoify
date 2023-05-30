# Tests for the nato_msg module

import sys
import os
import pytest

module_path = os.path.abspath(os.path.join('nato_code'))
if module_path not in sys.path:
    sys.path.append(module_path)
print(module_path)

from nato_msg import msg_to_nato, nato_to_msg

# @pytest.fixture
# def nato_output():
nato_output = "TANGO HOTEL INDIA SIERRA  INDIA SIERRA  ALFA  TANGO ECHO SIERRA TANGO  MIKE ECHO SIERRA SIERRA ALFA GOLF ECHO STOP  ONE TWO THREE FOUR STOP  SIERRA TANGO OSCAR PAPA "
nato_out_lower = "tango hotel india sierra  india sierra  alfa  tango echo sierra tango  mike echo sierra sierra alfa golf echo stop  one two three four stop  sierra tango oscar papa "
symb_output = "EXCLAMARK AT HASHTAG DOLLARSIGN PERCENT CARET AMPERSAND ASTERISK LEFTPAREN RIGHTPAREN UNDERSCORE PLUS EQUAL DASH APOSTROPHE QUOTMARK COLON SEMICOLON QUESTMARK SLASH POINT COMMA GREATERTHAN LESSTHAN BACKSLASH PIPE BACKTICK TILDE LEFTSQUARE RIGHTSQUARE LEFTCURLY RIGHTCURLY "
numb_output = "ONE TWO THREE FOUR FIVE  SIX SEVEN EIGHT NINE ZERO "

def test_msg_to_nato():
    """Test the msg_to_nato function
    """
    # Test message
    message = "This is a test message. 1234. STOP"
    nato_message = msg_to_nato(message)
    assert nato_message == nato_output

def test_nato_to_msg():
    """Test the nato_to_msg function
    """
    # Test message
    nato_message = nato_output
    message = nato_to_msg(nato_message)
    assert message == "THIS IS A TEST MESSAGE. 1234. STOP"

def test_msg_to_nato_empty():
    """Test the msg_to_nato function with an empty message
    """
    # Test message
    message = ""
    nato_message = msg_to_nato(message)
    assert nato_message == ""

def test_nato_to_msg_empty():
    """Test the nato_to_msg function with an empty message
    """
    # Test message
    nato_message = ""
    message = nato_to_msg(nato_message)
    assert message == ""

def test_msg_to_nato_none():
    """Test the msg_to_nato function with a None message
    """
    # Test message
    message = None
    nato_message = msg_to_nato(message)
    assert nato_message == ""

def test_nato_to_msg_none():
    """Test the nato_to_msg function with a None message
    """
    # Test message
    nato_message = None
    message = nato_to_msg(nato_message)
    assert message == ""

def test_msg_to_nato_symbols():
    """Test the msg_to_nato function with symbols
    """
    # Test message
    message = "!@#$%^&*()_+=-'\":;?/.,><\\|`~[]{}"
    nato_message = msg_to_nato(message)
    assert nato_message == symb_output

def test_nato_to_msg_symbols():
    """Test the nato_to_msg function with symbols
    """
    # Test message
    nato_message = symb_output
    message = nato_to_msg(nato_message)
    assert message == "!@#$%^&*()_+=-'\":;?/.,><\\|`~[]{}"

def test_msg_to_nato_numbers():
    """Test the msg_to_nato function with numbers
    """
    # Test message
    message = "12345 67890"
    nato_message = msg_to_nato(message)
    assert nato_message == numb_output

def test_nato_to_msg_numbers():
    """Test the nato_to_msg function with numbers
    """
    # Test message
    nato_message = numb_output
    message = nato_to_msg(nato_message)
    assert message == "12345 67890"

def test_msg_to_nato_uppercase():
    """Test the msg_to_nato function with uppercase letters
    """
    # Test message
    message = "THIS IS A TEST MESSAGE. 1234. STOP"
    nato_message = msg_to_nato(message)
    assert nato_message == nato_output

def test_nato_to_msg_uppercase():
    """Test the nato_to_msg function with uppercase letters
    """
    # Test message
    nato_message = nato_output
    message = nato_to_msg(nato_message)
    assert message == "THIS IS A TEST MESSAGE. 1234. STOP"

def test_msg_to_nato_lowercase():
    """Test the msg_to_nato function with lowercase letters
    """
    # Test message
    message = "this is a test message. 1234. stop"
    nato_message = msg_to_nato(message)
    assert nato_message == nato_output

def test_nato_to_msg_lowercase():
    """Test the nato_to_msg function with lowercase letters
    """
    # Test message
    nato_message = nato_out_lower
    message = nato_to_msg(nato_message)
    assert message == "THIS IS A TEST MESSAGE. 1234. STOP"


