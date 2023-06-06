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



<h1 align="center">Natoify</h1>

  <p align="center">
    Encode and decode plain text messages using the NATO phonetic alphabet (and others...)
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

![Natoify: natocli Screen Shot][natocli-screenshot]


![Natoify: natoapp Screen Shot][natoapp-screenshot]

In the twisted world where learning Python coding and late-night junk food binges merge, things got out of hand. I blame Github Copilot and ChatGPT. These AI delinquents morphed a humble script into a full-fledged program, decked out with a CLI and a desktop app. And the result? A cryptic cabaret called "Natoify."

Natoify is the tongue-twisting lovechild of the NATO phonetic alphabet and a magic 8-ball. It takes your mundane messages and codes 'em using the NATO alphabet, transforming 'A' into 'ALFA', 'B' into 'BRAVO', and so on. Your once readable message is now a linguistic labyrinth of code words. Want to turn back the gibberish? Just feed it back to Natoify, and voila, you get your original message, digits, and doodads intact. And NATO is not the only way to fly. There are more...many, many more ways to play such as STARWARS, JOHNWICK, HARRYPOTTER, SOUTHPARK, and REDNECK. More than a hundred, last I checked, due to ChatGPT's enthusiasm.

The package comes with the essentials: an encoder and decoder, a CLI, and a desktop app. The CLI lets you play God with your text files, encoding, decoding, encrypting, and decrypting to your heart's content. It's like a Swiss army knife for text manipulation. For those who prefer a fancier toy, the desktop app provides a slick playground to experiment with your text, allowing for on-the-fly encoding, decoding, and even some chit-chat with our AI buddy, ChatGPT 3.5 turbo. The app is built with customtkinter, a nifty GUI framework, so it's ready to rock 'n roll on any platform. So, brace yourself for some NATO-style fun!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Built With

* [![Python][Python]][Python-url]
* [![VScode][VScode.com]][VScode-url]
* [![Github Copilot][github.com]][GHCP-url]
* [![chatGPT][chat.openai.com]][GPT-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



# Installation

1. As a python package:
   ```sh
   pip install natoify
   ```
OR:
1. Clone the repo (or download the zip):
   ```sh
   git clone 'https://github.com/darkbiscuits/natoify.git'
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


<!-- GETTING STARTED -->
# Getting Started

To use Natoify on cli (after installation via pip):
* bash
```sh
  natocli -m message.txt -o encoded.txt  # uses NATO library - default
```
Or use to encode output from other cli programs:
* bash
```sh
  ls | natocli -o encoded.txt -c "REDNECK"
```
Having a rough day and need a giggle, try this:
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


<!-- LICENSE -->
# License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
# Contact

<img src="_static/DarkBiscuit.jpg" alt="DarkBiscuits" width="80" height="80"> DarkBiscuits on Github

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
[natocli-screenshot]: _static/natocli-screenshot.png
[natoapp-screenshot]: _static/natoapp-screenshot.png
[VScode.com]: https://img.shields.io/static/v1?label=VScode&message=OSX-13.3&color=9fc&style=for-the-badge
[VScode-url]: https://code.visualstudio.com/
[github.com]: https://img.shields.io/static/v1?label=Github&message=Copilot&color=yellowgreen&style=for-the-badge
[GHCP-url]: https://github.com/features/copilot
[chat.openai.com]: https://img.shields.io/static/v1?label=chatGPT&message=GPT-3.5-turbo&color=blue&style=for-the-badge
[GPT-url]: https://chat.openai.com
[Python]: https://img.shields.io/static/v1?label=Python&message=3.110&color=green&style=for-the-badge
[Python-url]: https://www.python.org/