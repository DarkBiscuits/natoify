"""
A desktop application for natoify created using customtkinter and tkinter.
It is a simple GUI application that allows the user to convert a string to
its NATO phonetic alphabet equivalent.

Features:
    - Loading and display of text files using a file dialog
    - Loading of text files from an internet URL
    - Conversion of text to NATO phonetic alphabet using one of the many libraries
    - Viewing of all libraries available, with the ability to add/remove libraries
      - Display of sample text converted using each library
    - Saving of converted text to a text file
    - Copying of converted text to clipboard
    - ChatGPT integration for generating text to encode
      - Including generation of new code libraries
    
"""

# Imports
import os
import sys
import shutil
import json
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from typing import Optional, Tuple, Union

import customtkinter as ctk

from natoify.engine import Natoify

# Constants
__version__ = "0.1.0"
THEME_COLORS = ["blue", "dark-blue", "green"]

# Classes

class NatoApp(ctk.CTk):
    """ The main application class for natoify. """
    
    scr_w, scr_h = 800, 600
    current_file_path = ""
    decode = False
    encrypt = 0
    code_lib_list = []
    current_code_lib = "NATO"

    def __init__(self):
        super().__init__()
        ctk.set_default_color_theme(THEME_COLORS[1])
        
        # Setup the natoify engine
        self.nato_eng = NatoEngine(master=self)
        
        # Setup the window
        scr_width = self.winfo_screenwidth()
        scr_height = self.winfo_screenheight()
        scr_x_pos = int((scr_width/2)-(self.scr_w/2))
        scr_y_pos = int((scr_height/2)-(self.scr_h/2))
        self.geometry(f"{self.scr_w}x{self.scr_h}+{scr_x_pos}+{scr_y_pos}")
        self.title_text = f"Natoify v{__version__}"
        self.title(self.title_text)
        self.minsize(840, 400)

        # Setup the grid layout
        self.grid_columnconfigure(0, weight=1, pad=5)
        self.grid_rowconfigure(0, weight=0, pad=5)
        self.grid_rowconfigure(1, weight=1, pad=5)

        # Create the top menu bar
        self.toppanel = TopMenuBar(master=self)
        self.toppanel.grid(row=0, column=0, sticky="nsew")
        
        # Create the main tab view and text editor
        self.tabview = MainTabView(master=self, command=self.tabview_callback)
        self.tabview.grid(row=1, column=0, sticky="nsew")


    def tabview_callback(self):
        """ Callback function for when the tabview changes tab. """
        tab_name = self.tabview.get()
        
        if tab_name == "Message Text":
            pass
        elif tab_name == "Playground":
            pass
        elif tab_name == "Natoified Text":
            self.generate_nato_text()
        else:
            pass
            
    def generate_nato_text(self):
        """ Encode/decode and update the text in the editor. """
        txt = self.tabview.text_msg.get("0.0", "end")
        self.tabview.text_enc.delete("0.0", "end")
        if self.decode:
            nato_txt = self.nato_eng.decode(txt, bool(self.encrypt))
        else:
            nato_txt = self.nato_eng.encode(txt, bool(self.encrypt))
        self.tabview.text_enc.insert("0.0", nato_txt)

    def update_code_lib_display(self):
        """ Update the code library dropdown. """
        self.code_lib_list = self.nato_eng.list_libraries()
        self.current_code_lib = self.nato_eng.current_code
        self.toppanel.code_lib_dd.configure(values=self.code_lib_list)
        self.toppanel.code_lib_dd.set(self.current_code_lib)
    
    def reload_code_libs(self):
        """ Reload the code libraries. """
        self.nato_eng.reload_libraries()
        self.update_code_lib_display()


class MainTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.msg_tab = self.add("Message Text")
        self.enc_tab = self.add("Natoified Text")
        self.play_tab = self.add("Playground")
        self.edit_tab = self.add("CodeEditor")
        self.msg_tab.grid_columnconfigure(0, weight=1)
        self.msg_tab.grid_rowconfigure(0, weight=1)
        self.enc_tab.grid_columnconfigure(0, weight=1)
        self.enc_tab.grid_rowconfigure(0, weight=1)
        self.play_tab.grid_columnconfigure(0, weight=1)
        self.play_tab.grid_rowconfigure(0, weight=1)
        self.edit_tab.grid_columnconfigure(0, weight=1)
        self.edit_tab.grid_rowconfigure(0, weight=1)
        self.edit_tab.grid_rowconfigure(1, weight=0)

        # add widgets on tabs
        self.text_msg = ctk.CTkTextbox(master=self.msg_tab)
        self.text_msg.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.text_msg.insert("0.0", "This is the message editor.\n")
        
        self.text_enc = ctk.CTkTextbox(master=self.enc_tab)
        self.text_enc.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.text_enc.insert("0.0", "THIS IS THE ENCODE/DECODE EDITOR.\n")
        
        self.text_play = ctk.CTkTextbox(master=self.play_tab)
        self.text_play.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.text_play.insert("0.0", "THIS IS THE PLAYGROUND.\n")
        
        self.text_edit = ctk.CTkTextbox(master=self.edit_tab)
        self.text_edit.grid(row=0, column=0, padx=5, pady=5, columnspan=4, sticky="nsew")
        self.text_edit.insert("0.0", "THIS IS THE CODE EDITOR.\n")
        
        self.lft_btns = ctk.CTkFrame(master=self.edit_tab)
        self.lft_btns.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        
        self.code_reload_btn = ctk.CTkButton(master=self.lft_btns, text="Reload All Codes", 
                                             command=self.reload_code_lib)
        self.code_reload_btn.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        self.code_clear_btn = ctk.CTkButton(master=self.lft_btns, text="Clear Editor", command=self.clear_code)
        self.code_clear_btn.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        self.code_open_btn = ctk.CTkButton(master=self.edit_tab, text="Open Code", command=self.load_code)
        self.code_open_btn.grid(row=1, column=2, padx=5, pady=5, sticky="se")
        
        self.code_save_btn = ctk.CTkButton(master=self.edit_tab, text="Save Code", command=self.save_code)
        self.code_save_btn.grid(row=1, column=3, padx=5, pady=5, sticky="se")

        # Editor configuration
        wd, ht = 500, 800
        c_r = 3
        wrp = "word"
        fnt = ("Courier New", 18)
        self.text_msg.configure(width=0, height=0, corner_radius=c_r, 
                                wrap=wrp, font=fnt)
        self.text_enc.configure(width=0, height=0, corner_radius=c_r, 
                                wrap=wrp, font=fnt)
        self.text_play.configure(width=0, height=0, corner_radius=c_r, 
                                wrap=wrp, font=fnt)
        self.text_edit.configure(width=0, height=0, corner_radius=c_r, 
                                wrap=wrp, font=fnt)
        
    def load_code(self):
        """ Load code from a file into the editor. """
        filetypes = [("Text Files", "*.json"), ("All Files", "*.*")]
        file_path = filedialog.askopenfilename(title="Select a json code library to load",
                                            filetypes=filetypes,
                                            initialdir=self.master.nato_eng.code_lib_path)

        if file_path:
            with open(file_path, "r") as f:
                code = json.load(f)

            formatted_code = json.dumps(code, indent=4)
            self.text_edit.delete("0.0", "end")
            self.text_edit.insert("0.0", formatted_code)

    def save_code(self):
        """ Save code from the editor into a file. """
        filetypes = [("Text Files", "*.json"), ("All Files", "*.*")]
        file_path = filedialog.asksaveasfilename(title="Save the code library",
                                                filetypes=filetypes,
                                                initialdir=self.master.nato_eng.code_lib_path)

        if file_path:
            code = self.text_edit.get("0.0", "end")
            with open(file_path, "w") as f:
                f.write(code)

    def reload_code_lib(self):  
        """ Reload the code library from the default file. """
        self.master.reload_code_libs()


    def clear_code(self):
        """ Clear the code editor. """
        self.text_edit.delete("0.0", "end")


class TopMenuBar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

        self.grid_columnconfigure(1, weight=1, pad=5)
        self.grid_columnconfigure(2, weight=1, pad=5)
        self.grid_rowconfigure(0, weight=0, pad=5)

        # add widgets onto the frame...
        self.file_frm = ctk.CTkFrame(self)
        self.file_frm.grid(row=0, column=0, padx=5, sticky="w")
        self.file_btn = ctk.CTkButton(master=self.file_frm, text="Load File", command=self.file_dialog)
        self.file_btn.grid(row=0, column=0, padx=5, sticky="w")
        self.save_btn = ctk.CTkButton(master=self.file_frm, text="Save File", command=self.save_file)
        self.save_btn.grid(row=0, column=1, padx=5, sticky="w")
        self.enc_frm = ctk.CTkFrame(self)
        self.enc_frm.grid(row=0, column=1, padx=5, sticky="e")
        self.enc_dec_btn = ctk.CTkSegmentedButton(master=self.enc_frm, values=["Encode", "Decode"], command=self.set_encode_decode) 
        self.enc_dec_btn.grid(row=0, column=0, padx=5, sticky="e")
        self.enc_dec_btn.set("Encode")
        self.chk_encrypt = ctk.CTkCheckBox(master=self.enc_frm, text="Encrypt", command=self.toggle_encrypt)
        self.chk_encrypt.grid(row=0, column=1, padx=5, sticky="e")
        self.chk_encrypt.deselect()
        self.code_frm = ctk.CTkFrame(self)
        self.code_frm.grid(row=0, column=2, padx=5, sticky="e")
        self.code_lib_dd = ctk.CTkComboBox(master=self.code_frm, values=["NATO", "GHETTO"], command=self.set_code_lib)
        self.code_lib_dd.grid(row=0, column=0, padx=5, sticky="e")
        self.code_lib_dd.configure(values=self.master.code_lib_list, state="readonly")
        self.code_lib_dd.set(self.master.current_code_lib)
        self.lib_btn = ctk.CTkButton(master=self.code_frm, text="Install Code", command=self.load_code_lib_file)
        self.lib_btn.grid(row=0, column=1, padx=5, sticky="e")

    
    def file_dialog(self):
        """ Open a file dialog for selecting a file to load. """
        filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")]
        file_path = filedialog.askopenfilename(title="Select a file to load",
                                               filetypes=filetypes)

        if file_path:
            with open(file_path, "r") as f:
                self.master.tabview.text_msg.delete("1.0", "end")
                self.master.tabview.text_msg.insert("1.0", f.read())
                file_name = os.path.basename(file_path)
                self.master.title(f"{self.master.title_text} - {file_name}")
                self.master.current_file_path = file_path

    def save_file(self):
        """ Save the current message to a file. """
        if self.master.current_file_path:
            cur_file = self.master.current_file_path
        else:
            cur_file = "Untitled.txt"
        init_dir = os.path.dirname(cur_file)
        cur_file_name = os.path.basename(cur_file)
        filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")]
        file_path = filedialog.asksaveasfilename(title="Save the current message",
                                                 filetypes=filetypes,
                                                 initialdir=init_dir,
                                                 initialfile=cur_file_name)
        
        # Get the current tab, and save the text from that tab
        current_tab = self.master.tabview.get()
        if current_tab == "Message Text":
            output_text = self.master.tabview.text_msg.get("1.0", "end")
        else:
            output_text = self.master.tabview.text_enc.get("1.0", "end")

        if file_path:
            with open(file_path, "w") as f:
                f.write(output_text)

    def load_code_lib_file(self):
        """ Load a code library from a file. """
        filetypes = [("Text Files", "*.json"), ("All Files", "*.*")]
        file_path = filedialog.askopenfilename(title="Select a json code library to load",
                                               filetypes=filetypes)

        if file_path:
            self.master.nato_eng.add_library(file_path)
            self.master.update_code_lib_display()
            self.master.generate_nato_text()
   
    def set_encode_decode(self, btn_name: str):
        """ Set flags for encoding and encrypting. """
        if btn_name == "Encode":
            self.master.decode = False
            self.chk_encrypt.configure(text="Encrypt")
        else:
            self.master.decode = True
            self.chk_encrypt.configure(text="Decrypt")
        
        # Generate naotified text when switching between encode/decode
        self.master.generate_nato_text()

    def toggle_encrypt(self):
        """ Set the encrypt flag. """
        self.master.encrypt = self.chk_encrypt.get()
        self.master.tabview_callback()

    def set_code_lib(self, lib_name: str):
        """ Set the code library. """
        self.master.current_code_lib = lib_name
        self.master.nato_eng.load_library(lib_name)
        self.master.generate_nato_text()


class NatoEngine():
    """ The main engine for natoify. """
    def __init__(self, master):
        self.master = master
        self.nato = Natoify()
        self.code_lib_path = self.nato.CODE_LIB_DIR
        self.current_code = self.nato.current_code
        self.master.code_lib_list = self.list_libraries()
        self.master.current_code_lib = self.nato.current_code

    def encode(self, text: str, encrypt: bool) -> str:
        """ Encode the given text using the given library. """
        return self.nato.encode(text, encrypt)

    def decode(self, text: str, encrypt: bool) -> str:
        """ Decode the given text using the given library. """
        return self.nato.decode(text, encrypt)

    def load_library(self, library: str) -> None:
        """ Load the given library. """
        self.nato.set_code(library)
        self.current_code = self.nato.current_code

    def add_library(self, lib_file_path: str) -> None:
        """ Add the given library (json file) to the directory of libraries. """
        lib_file_name = os.path.basename(lib_file_path)
        lib_dest_path = os.path.join(self.nato.CODE_LIB_DIR, lib_file_name)

        if os.path.exists(lib_dest_path):
            # If the file already exists, ask the user if they want to change the name or cancel
            response = messagebox.askyesnocancel("File Already Exists", f"The file '{lib_file_name}' already exists. Do you want to change the name or cancel?")
            if response is None:
                # If the user cancels, do nothing
                return
            elif response:
                # If the user wants to change the name, ask them to choose a new name
                lib_file_name = filedialog.asksaveasfilename(initialdir=self.nato.CODE_LIB_DIR, initialfile=lib_file_name)
                if not lib_file_name:
                    # If the user cancels, do nothing
                    return
                lib_dest_path = os.path.join(self.nato.CODE_LIB_DIR, os.path.basename(lib_file_name))

        shutil.copy(lib_file_path, lib_dest_path)
        self.nato.load_codes()

    def remove_library(self, library: str) -> None:
        """ Remove the given library from the list of libraries. """
        pass

    def list_libraries(self) -> list:
        """ Return a list of all available libraries. """
        return self.nato.list_codes()
    
    def reload_libraries(self) -> None:
        """ Reload the list of libraries. """
        self.nato.CODE_LIBRARY = {}
        self.nato.load_codes()
        self.current_code = self.nato.current_code
        self.master.code_lib_list = self.list_libraries()


# Show the main window
app = NatoApp()
app.mainloop()
