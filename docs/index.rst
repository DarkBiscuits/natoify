=======
NATOify
=======

This is the documentation of **Natoify**.

Contents
========

.. toctree::
   :maxdepth: 2

   Overview <README.md>
   Tutorials <tutorials.md>
   API Reference <api>
   Module Reference <api/modules>
   Requirements <Requirements>
   License <license>

Overview
--------

Natoify is the tongue-twisting lovechild of the NATO phonetic alphabet and a magic 8-ball. It takes your mundane messages and codes 'em using the NATO alphabet, transforming 'A' into 'ALFA', 'B' into 'BRAVO', and so on. Your once readable message is now a linguistic labyrinth of code words. Want to turn back the gibberish? Just feed it back to Natoify, and voila, you get your original message, digits, and doodads intact. And NATO is not the only way to fly. There are more...many, many more ways to play such as STARWARS, JOHNWICK, HARRYPOTTER, SOUTHPARK, and REDNECK. More than a hundred, last I checked, due to ChatGPT's enthusiasm.

Interested? Read on in the :doc:`README`.

This python package includes the basic encoder and decoder `engine.py` along
with a cli program `natocli.py` and a desktop app `natoapp.py` based on the
customtkinter library \(cross-platform\).

See the :doc:`README` for more information.

.. Image:: _static/natocli-screenshot.png
   
.. Image:: _static/natoapp-screenshot.png

Quick Reference
------------------------

Installation (if I manage to get it uploaded to Pypi at some point).

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

