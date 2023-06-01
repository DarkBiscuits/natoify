"""
Command line interface for natoify

Usage:
    natoify [OPTIONS]

Options:    
    -m, --message FILENAME   Message filename (or '-' to read from stdin)
    -o, --output FILENAME    Output filename (or '-' to write to stdout)
    -d, --decode             Decode the input message
    -e, --encrypted          Message is to be encrypted (or decrypted if decoding))
    -c, --code CODE          Code library to use for encryption/decryption
    -l, --list-codes         List available code libraries
    -r, --repl               Run in interactive mode. Type input -> get output
    --help                   Show this message and exit.

Examples:   
    >>>natoify -m message.txt -o output.txt
        encode message.txt using NATO code without encryption (default)

    >>>natoify -m message.txt -o output.txt -e -c VULGAR
        encode message.txt using VULGAR code and encryption

    >>>natoify -m message.txt -o output.txt -d -c VULGAR
        decode message.txt using VULGAR code without decryption

    >>>natoify -m message.txt -o -
        encode message.txt using NATO code and write to stdout

    >>>natoify -m - -o -
        encode stdin using NATO code and write to stdout

    >>>natoify -m - -o output.txt
        encode stdin using NATO code and write to output.txt

    >>>natoify -r
        run in interactive mode. Type input -> get output

    >>>natoify -l
        list available code libraries


"""

import click

from natoify.engine import Natoify


def show_codes(nato: Natoify) -> None:
    """Send list of available codes to stdout"""
    click.echo("Available code libraries:")
    for code in nato.list_codes():
        click.echo(f"\t{code}")


def try_set_code(code: str, nato: Natoify) -> bool:
    """Set code library for natoify engine
    Fail gracefully if code is not available
    """
    code = code.upper()
    if code not in nato.list_codes():
        success = False
    else:
        nato.set_code(code)
        success = True
    return success


def interactive_mode(code: str = "NATO") -> None:
    """Run natoify in interactive mode

    Interactive mode allows the user to enter a message and receive the encoded message.
    The user can also change the code library or toggle encryption.

    Args:
        code (str): Code library to use for encoding

    Returns:
        None
    """
    # Welcome to interactive mode showing commands
    click.echo(f"\nWelcome to interactive mode. (using '{code}' code)\n")
    click.echo("Type '>??' to enter options mode.")
    click.echo("Use options mode to change code library or toggle encryption.\n")
    click.echo("Enter message to encode. (or press Enter to quit)")

    # Initialize natoify engine
    nato = Natoify()
    encrypt = False

    # Main loop for interactive mode
    while True:
        # Get input from user
        msg = input("Enter message: ")
        if msg == "":
            # Exit main loop
            click.echo("Exiting...")
            exit(1)
        elif msg == ">??":
            # Options mode loop
            click.echo("Options mode:")
            click.echo("\t'c' to change code library")
            click.echo("\t'e' to toggle encryption")
            click.echo("\t'ENTER' to resume encoding")
            while True:
                opt = input("Enter option: ")
                if opt == "c":
                    # Change code library
                    show_codes(nato)
                    code = input("Enter code: ")
                    if try_set_code(code, nato):
                        click.echo(f"Code set to '{code}'")
                    else:
                        click.echo(
                            f"Error: '{code}' is not a valid code. See codes options above."
                        )
                elif opt == "e":
                    # Toggle encryption
                    encrypt = not encrypt
                    click.echo(f"Encryption set to {encrypt}")
                elif opt == "":
                    # Resume encoding, exit options mode loop
                    click.echo("Resuming encoding...")
                    break
                else:
                    click.echo(
                        "Invalid option. 'c' for code, 'e' for encryption, or 'ENTER' to resume."
                    )
        else:
            # Interactive message encoding
            nato_msg = nato.encode(msg, encrypt)
            click.echo(nato_msg)


@click.command()
@click.option(
    "-m",
    "--message",
    type=click.File("rb"),
    default="-",
    help="Message filename (or '-' to read from stdin)",
)
@click.option(
    "-o",
    "--output",
    type=click.File("wb"),
    default="-",
    help="Output filename (or '-' to write to stdout)",
)
@click.option(
    "-d", "--decode", is_flag=True, default=False, help="Decode the input message"
)
@click.option(
    "-e",
    "--encrypted",
    is_flag=True,
    default=False,
    help="Message is to be encrypted (or decrypted if decoding))",
)
@click.option(
    "-c", "--code", default="NATO", help="Code library to use for encryption/decryption"
)
@click.option(
    "-l", "--list-codes", is_flag=True, default=False, help="List available codes"
)
@click.option(
    "-r",
    "--repl",
    is_flag=True,
    default=False,
    help="Run in interactive mode. Type input -> get output",
)
def run(message, output, decode, encrypted, code, list_codes, repl):
    """
    Welcome to the NATOify command line interface!
    This program will encode or decode a message using the NATO phonetic alphabet.
    Alternate codes are available. Use --list-codes to see available options.

    Examples:

        >>>natoify -m message.txt -o output.txt

            encode message.txt using NATO code without encryption (default)

        >>>natoify -m message.txt -o output.txt -e -c VULGAR

            encode message.txt using VULGAR code and encryption

        >>>natoify -m message.txt -o output.txt -d -c VULGAR

            decode message.txt using VULGAR code without decryption

        >>>natoify -m message.txt -o -

            encode message.txt using NATO code and write to stdout

        >>>natoify -m - -o -

            encode stdin using NATO code and write to stdout

        >>>natoify -m - -o output.txt

            encode stdin using NATO code and write to output.txt

        >>>natoify -r

            run in interactive mode. Type input -> get output

        >>>natoify -l

            list available code libraries

        >>>natoify -h

            show this help message

        >>>natoify
        
            encode stdin using NATO code and write to stdout (default without options)
            = same as using '-m - -o -' : Can hang if stdin is empty (use ctrl+d to exit)
    """

    # Determine mode of operation
    if list_codes:
        # List available codes and exit
        nato = Natoify()
        show_codes(nato)
        exit(0)
    elif repl:
        # Run in interactive mode and exit
        interactive_mode(code)
        exit(0)
    else:
        # Run in normal mode. Read from file or stdin, write to file or stdout
        # Initialize natoify engine
        nato = Natoify()

        # Set code for encoding/decoding
        if not try_set_code(code, nato):
            click.echo(
                f"Error: '{code}' is not a valid code. Use --list-codes to see available options."
            )
            exit(1)

        # Read message from file or stdin
        msg = message.read()
        if msg == "" or msg == None:
            click.echo("Error reading input. Input cannot be empty.")
            exit(1)

        # Convert message to string (if coming from stdin)
        msg = msg.decode("utf-8")

        # Encode or decode message using natoify engine
        if decode:
            nato_msg = nato.decode(msg, encrypted)
        else:
            nato_msg = nato.encode(msg, encrypted)

        # Write message to file or stdout
        nato_msg = nato_msg.encode("utf-8")  # Convert to bytes for writing
        output.write(nato_msg)
        output.flush()


# *** Main Program ***
if __name__ == "__main__":
    run()
