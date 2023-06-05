<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/darkbiscuits/natoify">
    <img src="_static/DarkBiscuit.jpg" alt="Logo" width="80" height="80">
  </a>

<h1 align="center">Natoify</h1>

  <p align="center">
    Encode and decode plain text messages using the NATO phonetic alphabet (or variants)
    <br />
    <a href="https://github.com/darkbiscuits/natoify"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/darkbiscuits/natoify">View Demo</a>
    ·
    <a href="https://github.com/darkbiscuits/natoify/issues">Report Bug</a>
    ·
    <a href="https://github.com/darkbiscuits/natoify/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
# About The Project

[![Natoify: natocli Screen Shot][natocli-screenshot]](_static/natocli-screenshot.png)
[![Natoify: natoapp Screen Shot][natoapp-screenshot]](_static/natoapp-screenshot.png)

What started as a simple coding challenge while taking a basic Python course has 
gone horribly wrong...thanks to Github Copilot and chatGPT. AI tools
made it easy to continue building out a simple script into a full blown program, 
complete with cli interface and windowed desktop app. What does it do?

Natoify encodes/decodes plain text messages using a NATO-style phonetic alphabet as a key.
In standard NATO speak: A=ALFA, B=BRAVO, C=CHARLIE, D=DELTA, etc. 
Each letter in the message is matched to its corresponding word from the selected
code library and it then outputs an encoded message in plain text. Decoding a message, the
text is searched for matching code words and they are replaced with the proper letter
(or number/punctuation). Encoding results in a message with no special characters or
numbers, only uppercase letters in the form of groups of words. Decoding reveals the
original message, complete with numbers and special characters.

This python package includes the basic encoder and decoder (engine.py) along
with a cli program (natocli.py) and a desktop app (natoapp.py) based on the
customtkinter library (cross-platform).

The cli program allows you to specify an input text file and an output text file for
the resulting encoded or decoded message. It has some utility options to list 
available code libraries, set a specific code library for encoding/decoding, 
encrypt/decrypt in addition to encoding/decoding, and a repl loop allowing you
to experiment by typing text to input and seeing the resulting output immediately, along with
the ability to switch code libraries and toggle encryption as you go. Great for playing with
options before passing files through. Running it as a chain in your favorite shell
also lets you to omit the input, output, or both, allowing it to be used to pipe (|) 
cli output to/from other programs through it for conversion.

The desktop app allows you to load a text message, choose a code library, toggle 
encoding/decoding/encryption/decryption options, and view the result. You can load and 
install additional code libraries as well. The playground tab gives you a place to play 
with typing input text and immediately viewing the output, encode a word or sentence using 
all available code libraries at once for comparison (and as a way to see the results of all libraries), and even includes a GPT mode where you can chat with chatGPT (3.5 turbo). GPT was used to generate almost all the included libraries (113 at last count) and is great for creating a code library based on your own custom theme. There is also a code editor tab where code
library files can be loaded, edited, copies saved, etc. The desktop app is built using
customtkinter, a modern styled gui framework based on tkinter, and should work on any
platform.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Built With

* [![Python][Python]][Python-url]
* [![VScode][VScode.com]][VScode-url]
* [![Github Copilot][github.com]][GHCP-url]
* [![chatGPT][chat.openai.com]][GPT-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
# Getting Started

To use Natoify on cli (after installation via pip):
* bash
```sh
  natocli -m message.txt -o encoded.txt  # uses NATO library - default
```
or use to encode output from other cli programs:
* bash
```sh
  ls | natocli -o encoded.txt -c "REDNECK"
```
having a rough day and need a giggle, try this:
* bash
```sh
  head file_giving_me_headaches.py | natocli -c "GHETTO"
```
To see all available code libraries use `-l` or `--list-codes` (or use `--help` for a list of all options):
* bash
```sh
  natocli --list-codes
```
To run in interactive mode use `-r` or `--repl`:
* bash
```sh
  natocli -r
```
To run the desktop app:
* bash
```sh
  natoapp
```

# Installation

1. As a python package:
   ```sh
   pip install natoify
   ```
OR:
1. Or clone the repo:
   ```sh
   git clone https://github.com/darkbiscuits/natoify.git
   ```
2. And install required PYPI packages (see requirements.txt):
   ```sh
   pip install importlib_metadata customtkinter click openai tiktoken
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
# Usage

Basic usage of CLI program (uses "NATO" code library - default):
* bash
```
  natocli -m text_to_convert.txt -o encoded_text.txt
```
Basic usage of desktop program:
* bash
```
  natoapp
```

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
# License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
# Contact

DarkBiscuits on Github

Project Link: [https://github.com/darkbiscuits/natoify](https://github.com/darkbiscuits/natoify)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/darkbiscuits/natoify.svg?style=for-the-badge
[contributors-url]: https://github.com/darkbiscuits/natoify/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/darkbiscuits/natoify.svg?style=for-the-badge
[forks-url]: https://github.com/darkbiscuits/natoify/network/members
[stars-shield]: https://img.shields.io/github/stars/darkbiscuits/natoify.svg?style=for-the-badge
[stars-url]: https://github.com/darkbiscuits/natoify/stargazers
[issues-shield]: https://img.shields.io/github/issues/darkbiscuits/natoify.svg?style=for-the-badge
[issues-url]: https://github.com/darkbiscuits/natoify/issues
[license-shield]: https://img.shields.io/github/license/darkbiscuits/natoify.svg?style=for-the-badge
[license-url]: https://github.com/darkbiscuits/natoify/blob/master/LICENSE.txt
[natocli-screenshot]: images/natocli-screenshot.png
[natoapp-screenshot]: images/natoapp-screenshot.png
[VScode.com]: https://img.shields.io/static/v1?label=VScode&message=OSX-13.3&color=9fc&style=for-the-badge
[VScode-url]: https://code.visualstudio.com/
[github.com]: https://img.shields.io/static/v1?label=Github&message=Copilot&color=yellowgreen&style=for-the-badge
[GHCP-url]: https://github.com/features/copilot
[chat.openai.com]: https://img.shields.io/static/v1?label=chatGPT&message=GPT-3.5-turbo&color=blue&style=for-the-badge
[GPT-url]: https://chat.openai.com
[Python]: https://img.shields.io/static/v1?label=Python&message=3.110&color=green&style=for-the-badge
[Python-url]: https://www.python.org/