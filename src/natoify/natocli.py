"""
Command line interface for natoify
"""

import click

from natoify.engine import Natoify


@click.command()
@click.option("--input",  type=click.File("rb"), help="Message text file (or '-' for stdin)")
@click.option("--output", type=click.File("wb"), default='-', help="Filename for output (or '-' for stdout))")
@click.option("--decode", is_flag=True, default=False, help="Decode the input message")
@click.option("--encrypted", is_flag=True, default=False, help="Message is to be encrypted (or decrypted if decoding))")
@click.option("--code", default="NATO", help="Code to use for encryption/decryption")
@click.option("--list-codes", is_flag=True, default=False, help="List available codes")
@click.option("--repl", is_flag=True, default=False, help="Run in interactive mode. Type input -> get output")
def run(input, output, decode, encrypted, code, list_codes, repl): 
    """Run the natoify command line interface"""

    # Initialize natoify engine
    nato = Natoify()

    # Set code for encoding/decoding
    code = code.upper()
    if code not in nato.CODE_OPTIONS.keys():
        click.echo("Invalid code option. Use --list-codes to see available options")
        exit(1)
    else:
        nato.set_code(code)
    
    # Determine mode of operation
    if list_codes:
        # List available codes and exit
        click.echo("Available codes:")
        for code in nato.CODE_OPTIONS.keys():
            click.echo(f"\t{code}")
        exit(0)
    elif repl:
        # Run in interactive mode and exit
        click.echo("Welcome to interactive mode. (using 'NATO' code)")
        click.echo("To see encrypted output, use '--repl --encrypted' at startup")
        click.echo("To run with a different code, use '--repl --code <code>' at startup\n")
        click.echo("Enter message to encode. Enter blank line to quit")
        message = "Hello!"
        while True:
            if message == "":
                exit(0) 
            message = input("Enter message: ")
            nato_msg = nato.encode(message, encrypted)
            click.echo(nato_msg)
    else:
        # Run in normal mode. Read from file or stdin, write to file or stdout
        message = input.read()
        if message == "" or message == None:
            click.echo("Error reading input. Input cannot be empty.")
            exit(1)

        # Encode or decode message
        if decode:
            nato_msg = nato.decode(message, encrypted)
        else:
            nato_msg = nato.encode(message, encrypted)

        # Write message to file
        output.write(nato_msg)
        output.flush()

# *** Main Program ***
if __name__ == "__main__":
    run()