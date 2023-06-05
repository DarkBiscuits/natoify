=======
natoify
=======

This is the documentation of **natoify**.

Contents
========

.. toctree::
   :maxdepth: 2

   Overview <README.md>
   API Reference <api>
   Module Reference <modules>
   Requirements <Requirements>
   License <license>

Overview
--------
.. note::

    What started as a simple coding challenge while taking a basic Python course has 
gone horribly \(wonderfully\) wrong...thanks to Github Copilot and chatGPT. AI tools
made it easy to continue building out a simple script into a full blown program, 
complete with cli interface and windowed desktop app. What does it do?

Natoify encodes/decodes plain text messages using a NATO-style phonetic alphabet as a key.
In standard NATO speak: A=ALFA, B=BRAVO, C=CHARLIE, D=DELTA, etc. 
Each letter in the message is matched to its corresponding word from the selected
code library and it then outputs an encoded message in plain text. Decoding a message, the
text is searched for matching code words and they are replaced with the proper letter
\(or number/punctuation\). Encoding results in a message with no special characters or
numbers, only uppercase letters in the form of groups of words. Decoding reveals the
original message, complete with numbers and special characters.

This python package includes the basic encoder and decoder `engine.py` along
with a cli program `natocli.py` and a desktop app `natoapp.py` based on the
customtkinter library \(cross-platform\).

See the :doc:`README` for more information.

.. Image:: images/natocli-screenshot.png
   
.. Image:: images/natoapp-screenshot.png

Quick Reference
------------------------

Installation.

.. code-block:: console  
   
   pip install natoify

Run Natoify on CLI (using the default code library "NATO").

.. code-block:: console  
   
   natocli -m message.txt -o output.txt

Run Natoify as a desktop app.

.. code-block:: console  
   
   natoapp

See the :doc:`README` for more information.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

