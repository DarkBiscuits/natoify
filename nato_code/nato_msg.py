"""
Module to convert a message to the NATO phonetic alphabet by character.
"""

from nato_lib import nato_codes, nato_code_words


def msg_to_nato(message: str) -> str:
    """Convert a message string to NATO words
    """
    nato_message = ''

    # Catch empty message
    if message == '' or message == None:
        return ''

    # Add a space to the end of the message to catch out of index errors
    message += ' '

    # Iterate through each character in the message and translate to NATO word
    for i, char in enumerate(message):
        char = char.upper()
        if char == '.': 
            # Check if period is at end of sentence
            if message[i+1] == ' ' or message[i+1] == '\n':
                nato_message += 'STOP '
            else:
                # Period is part of a number or abbreviation
                nato_message += nato_codes[char] + ' '
        # Only add a single space if character is a space
        elif char == ' ':
            nato_message += ' '
        else:
            # Translate character to NATO word
            nato_message += nato_codes[char] + ' '
            nato_message[:-1]  # Remove trailing space
    
    return nato_message

def nato_to_msg(nato_message: str) -> str:
    """Decode a NATO message string into English
    """

    # Catch empty message
    if nato_message == '' or nato_message == None:
        return ''
    
    # Get the reversed code dictionary for decode lookup
    nato_words = nato_code_words(nato_codes)
    decoded_msg = ""

    # Split message into a list of lines (list containing a string)
    lines = nato_message.split('\n')
    
    # Split each line's string into a list of words
    lines = [line.split('  ') for line in lines]

    # Decode each line (list containing lists of strings)
    for line in lines:
        # Strip whitespace from each word (group of symbols)
        line = [word.strip() for word in line]
        decoded_line = ""
        
        # Decode each group of symbols (that form a word)
        for word in line:
            symbols = word.split(' ')
            word = [nato_words.get(symbol.upper()) for symbol in symbols if symbol != '']
            word = ''.join(word) + ' '
            # Append decoded word to decoded line
            decoded_line += word
        
        # Append decoded line to decoded message
        decoded_msg += decoded_line + '\n'

    return decoded_msg.strip()


# Test output
# Load test message
# with open('../data/message.txt', 'r') as f:
#     message = f.read()

# n_msg = msg_to_nato(message)
# if n_msg:
#     print(n_msg, '\n')
#     with open('../data/nato_message.txt', 'w') as f:
#         f.write(n_msg)
#     eng_msg = nato_to_msg(n_msg)
#     print(eng_msg)


