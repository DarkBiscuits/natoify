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
import shutil
import threading
import json
from tkinter import filedialog, messagebox

import customtkinter as ctk

from natoify.engine import Natoify
from natoify.natogpt import NatoGPT


# Constants
__version__ = "0.1.0"
THEME_COLORS = ["blue", "dark-blue", "green"]

# Classes

class NatoApp(ctk.CTk):
    """ The main application class for natoify. 
    
    Attributes:
        nato_eng (NatoEngine): The engine used to convert text to NATO phonetic alphabet.
        decode (bool): Whether to decode the text or not.
        encrypt (int): The encryption level to use.
        code_lib_list (list): A list of all code libraries.
        current_code_lib (str): The current code library.
        chat_eng (NatoGPT): The engine used to chat with chatGPT.
        log_names_list (list): A list of all chat logs.
        current_file_path (str): The path to the current file.
        play_mode (str): The mode to use for the playground.
        title_text (str): The text to use for the title.

    Methods:
        tabview_callback(event: Event) -> None: The callback for the tabview.
        generate_nato_text() -> None: Generate the NATO text.
        update_code_lib_display() -> None: Update the code library display.
        TODO: Finish documenting methods.
    """
    
    def __init__(self):
        super().__init__()
        ctk.set_default_color_theme(THEME_COLORS[1])
        
        # Setup the natoify engine
        self.nato_eng = NatoEngine(master=self)
        self.decode = False
        self.encrypt = 0
        self.code_lib_list = []
        self.current_code_lib = "NATO"

        
        # When a message is open and in editor
        self.current_file_path = ""

        # Setup for the playground
        self.play_mode = "Current"
        
        # Setup the window
        scr_w, scr_h = 800, 600
        scr_width = self.winfo_screenwidth()
        scr_height = self.winfo_screenheight()
        scr_x_pos = int((scr_width/2)-(scr_w/2))
        scr_y_pos = int((scr_height/2)-(scr_h/2))
        self.geometry(f"{scr_w}x{scr_h}+{scr_x_pos}+{scr_y_pos}")
        self.title_text = f"Natoify v{__version__}"
        self.title(self.title_text)
        self.minsize(840, 400)

        # Setup the main grid layout
        self.grid_columnconfigure(0, weight=1, pad=5)
        self.grid_rowconfigure(0, weight=0, pad=5)
        self.grid_rowconfigure(1, weight=1, pad=5)

        # Create the top menu bar
        self.toppanel = TopMenuBar(master=self)
        self.toppanel.grid(row=0, column=0, sticky="nsew")
        
        # Create the main tab view and text editor
        self.tabview = MainTabView(master=self, command=self.tabview_callback)
        self.tabview.grid(row=1, column=0, sticky="nsew")

        # Load the code libraries into the dropdown
        self.update_code_lib_display()

        # Check for openai key
        gpt_key = ""
        if not os.environ.get('OPENAI_API_KEY'):
            get_key = ctk.CTkInputDialog(text="Enter your OpenAI API key", title="OpenAI API Key")
            aikey = get_key.get_input()
            if aikey:
                gpt_key = aikey
        else:
            gpt_key = os.environ.get('OPENAI_API_KEY')

        # Setup the chatGPT engine
        self.chat_eng = NatoGPT(gpt_key)
        self.log_names_list = []

    def tabview_callback(self):
        """ Callback function for when the tabview changes tab. """
        tab_name = self.tabview.get()
        
        if tab_name == "Message Text":
            # Set the encode button to normal
            self.toppanel.enc_dec_btn.configure(state="normal")
            self.toppanel.file_btn.configure(state="normal")
        elif tab_name == "Natoified Text":
            # Set the encode button to normal
            self.toppanel.enc_dec_btn.configure(state="normal")
            self.toppanel.file_btn.configure(state="disabled")
            self.generate_nato_text()
        elif tab_name == "Playground":
            # btn_txt = self.tabview.using_btns.get()
            # self.set_play_mode()
            self.toppanel.file_btn.configure(state="disabled")
        else:
            # Set the encode button to normal
            self.toppanel.enc_dec_btn.configure(state="normal")
            self.toppanel.file_btn.configure(state="disabled")
            
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

    def open_txt_file(self):
        """ Open a file dialog for selecting a file to load. """
        filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")]
        file_path = filedialog.askopenfilename(title="Select a file to load",
                                               filetypes=filetypes)

        if file_path:
            with open(file_path, "r") as f:
                self.tabview.text_msg.delete("1.0", "end")
                self.tabview.text_msg.insert("1.0", f.read())
                file_name = os.path.basename(file_path)
                self.title(f"{self.title_text} - {file_name}")
                self.current_file_path = file_path

    def save_txt_file(self):
        """ Save the current message to a file. """
        if self.current_file_path:
            cur_file = self.current_file_path
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
        current_tab = self.tabview.get()
        if current_tab == "Message Text":
            output_text = self.tabview.text_msg.get("1.0", "end")
        elif current_tab == "Natoified Text":
            output_text = self.tabview.text_enc.get("1.0", "end")
        elif current_tab == "Playground":
            output_text = self.tabview.text_play.get("1.0", "end")
        elif current_tab == "CodeEditor":
            output_text = self.tabview.text_edit.get("1.0", "end")
        else:
            print("Unknown tab")

        if file_path:
            with open(file_path, "w") as f:
                f.write(output_text)

    def load_code_lib_file(self):
        """ Load a code library from a file. """
        filetypes = [("Text Files", "*.json"), ("All Files", "*.*")]
        file_path = filedialog.askopenfilename(title="Select a json code library to load",
                                               filetypes=filetypes)

        if file_path:
            self.nato_eng.add_library(file_path)
            self.update_code_lib_display()
            self.generate_nato_text()

    def set_play_mode(self, btn_name: str):
        """ Set the play mode. """
        self.tabview.save_chat_btn.configure(state="disabled")
        self.tabview.chat_list_dd.configure(state="disabled")
        if btn_name == "All":
            self.play_mode = "All"
            # Set the encode button to encode and disabled
            # self.toppanel.enc_dec_btn.set("Encode")
            # self.toppanel.enc_dec_btn.configure(state="disabled")
        elif btn_name == "ChatGPT":
            self.play_mode = "ChatGPT"
            # Set the encode button to disabled
            # self.toppanel.enc_dec_btn.configure(state="disabled")
            self.tabview.save_chat_btn.configure(state="normal")
            self.update_chat_session_ddlist()
        else:
            self.play_mode = "Current"
            # Set the encode button to normal
            # self.toppanel.enc_dec_btn.configure(state="normal")

    def update_playground(self):
        """ Update the playground. """
        if self.play_mode == "Current":
            # Get the current text in the entry box and in the editor
            txt = self.tabview.play_entry.get("0.0", "end")
            editor_txt = self.tabview.text_play.get("0.0", "end")
            
            # Clear the editor
            self.tabview.text_play.delete("0.0", "end")

            # Encode/decode the text and update the editor
            if self.decode:
                ntxt = self.nato_eng.decode(txt, bool(self.encrypt))
            else:
                ntxt = self.nato_eng.encode(txt, bool(self.encrypt))
            
            # Update the editor
            self.tabview.text_play.insert("0.0", editor_txt + ntxt)
            self.tabview.text_play.see("end")
        elif self.play_mode == "All":
            # Get the current text in the entry box
            txt = self.tabview.play_entry.get("0.0", "end")
            
            # Clear the editor
            self.tabview.text_play.delete("0.0", "end")

            # Encode/decode the text using each code, collect all, and update the editor
            ntxt = ""
            curr_code = self.current_code_lib

            # Get the len of longest code name
            max_len = max([len(code) for code in self.code_lib_list])    

            # Loop through each code library
            for code in self.code_lib_list:
                title = f"{code}:{'-'*(max_len-len(code))} "
                ntxt += title
                self.nato_eng.load_library(code)
                if self.decode:
                    ntxt += self.nato_eng.decode(txt, bool(self.encrypt))
                else:
                    ntxt += self.nato_eng.encode(txt, bool(self.encrypt))
                ntxt += "\n\n"
            
            # Reset the code library to original
            self.nato_eng.load_library(curr_code)
            
            # Update the editor
            self.tabview.text_play.insert("0.0", ntxt)
            # self.tabview.text_play.see("end")
        elif self.play_mode == "ChatGPT":
            # Get the current text in the entry box
            txt = self.tabview.play_entry.get("0.0", "end")

            # Clear the entry box
            prompt = self.tabview.play_entry.get("0.0", "end")
            self.tabview.text_play.insert("end", f"{prompt}\n{'*'*60}\n")
            self.tabview.text_play.see("end")
            self.tabview.play_entry.delete("0.0", "end")
            wait_txt = f"Last message tokens: {self.chat_eng.current_tokens}\nWaiting for AI response..."
            self.tabview.play_entry.insert("0.0", wait_txt) 
            
            # Run the add_to_chat method in another thread
            t = threading.Thread(target=self.add_to_chat_thread, args=(txt,))
            t.start()


    def add_to_chat_thread(self, txt: str):
        # Send message to chatbot
        prompt, response = self.chat_eng.add_to_chat(txt)
        
        # Update the editor
        self.tabview.play_entry.delete("0.0", "end")
        self.tabview.text_play.insert("end", f"{response}\n{'='*60}\n")
        self.tabview.text_play.insert("end", f"Last Message Tokens: {self.chat_eng.current_tokens}\n{'='*60}\n")
        self.tabview.text_play.see("end")

    def save_chat_session(self):
        self.chat_eng.save_chat_log()
        self.update_chat_session_ddlist()
        self.tabview.chat_list_dd.set(self.log_names_list[0])

    def update_chat_session_ddlist(self):
        self.log_names_list = [os.path.basename(name) for name in self.chat_eng.get_chat_logs()]
        self.log_names_list.append("New Session")
        self.tabview.chat_list_dd.configure(values=self.log_names_list, state="readonly")
        self.tabview.chat_list_dd.set("New Session")



class TopMenuBar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

        self.grid_columnconfigure(1, weight=1, pad=5)
        self.grid_columnconfigure(2, weight=1, pad=5)
        self.grid_rowconfigure(0, weight=0, pad=5)

        # add file loading and saving buttons
        self.file_frm = ctk.CTkFrame(self)
        self.file_frm.grid(row=0, column=0, padx=5, sticky="w")
        self.file_btn = ctk.CTkButton(master=self.file_frm, text="Load File", command=self.open_file)
        self.file_btn.grid(row=0, column=0, padx=5, sticky="w")       
        self.save_btn = ctk.CTkButton(master=self.file_frm, text="Save File", command=self.save_file)
        self.save_btn.grid(row=0, column=1, padx=5, sticky="w")
        
        # add encoding and decoding buttons
        self.enc_frm = ctk.CTkFrame(self)
        self.enc_frm.grid(row=0, column=1, padx=5, sticky="e")
        self.enc_dec_btn = ctk.CTkSegmentedButton(master=self.enc_frm, values=["Encode", "Decode"], command=self.set_encode_decode) 
        self.enc_dec_btn.grid(row=0, column=0, padx=5, sticky="e")
        self.enc_dec_btn.set("Encode")
        self.chk_encrypt = ctk.CTkCheckBox(master=self.enc_frm, text="Encrypt", command=self.toggle_encrypt)
        self.chk_encrypt.grid(row=0, column=1, padx=5, sticky="e")
        self.chk_encrypt.deselect()
        
        # add code library selection and loading buttons
        self.code_frm = ctk.CTkFrame(self)
        self.code_frm.grid(row=0, column=2, padx=5, sticky="e")
        self.code_lib_dd = ctk.CTkComboBox(master=self.code_frm, values=["NATO", "GHETTO"], command=self.set_code_lib)
        self.code_lib_dd.grid(row=0, column=0, padx=5, sticky="e")
        self.code_lib_dd.configure(values=self.master.code_lib_list, state="readonly")
        self.code_lib_dd.set(self.master.current_code_lib)
        self.lib_btn = ctk.CTkButton(master=self.code_frm, text="Install Code", command=self.load_code_lib_file)
        self.lib_btn.grid(row=0, column=1, padx=5, sticky="e")

    
    def open_file(self):
        """ Open a file dialog for selecting a file to load. """
        self.master.open_txt_file()

    def save_file(self):
        """ Save the current message to a file. """
        self.master.save_txt_file()

    def load_code_lib_file(self):
        """ Load a code library from a file. """
        self.master.load_code_lib_file()
   
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


class MainTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

        # create tabs
        self.msg_tab = self.add("Message Text")
        self.enc_tab = self.add("Natoified Text")
        self.play_tab = self.add("Playground")
        self.edit_tab = self.add("CodeEditor")
        
        # configure tab weights
        self.msg_tab.grid_columnconfigure(0, weight=1)
        self.msg_tab.grid_rowconfigure(0, weight=1)
        
        self.enc_tab.grid_columnconfigure(0, weight=1)
        self.enc_tab.grid_rowconfigure(0, weight=1)
        
        self.play_tab.grid_columnconfigure(0, weight=1)
        self.play_tab.grid_rowconfigure(0, weight=1)
        self.play_tab.grid_rowconfigure(1, weight=0)
        
        self.edit_tab.grid_columnconfigure(0, weight=1)
        self.edit_tab.grid_rowconfigure(0, weight=1)
        self.edit_tab.grid_rowconfigure(1, weight=0)

        # add text edit widgets on tabs
        self.text_msg = ctk.CTkTextbox(master=self.msg_tab)
        self.text_msg.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.text_msg.insert("0.0", "This is the message editor.\n")
        
        self.text_enc = ctk.CTkTextbox(master=self.enc_tab)
        self.text_enc.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.text_enc.insert("0.0", "THIS IS THE ENCODE/DECODE EDITOR.\n")
        
        self.text_play = ctk.CTkTextbox(master=self.play_tab)
        self.text_play.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        # self.text_play.insert("0.0", "THIS IS THE PLAYGROUND.\n")
        
        self.text_edit = ctk.CTkTextbox(master=self.edit_tab)
        self.text_edit.grid(row=0, column=0, padx=5, pady=5, columnspan=4, sticky="nsew")
        self.text_edit.insert("0.0", "THIS IS THE CODE EDITOR.\n")
        
        # Text edit widgets configurations
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
        
        # Buttons for Playground tab lower frame
        self.play_btns_frm = ctk.CTkFrame(master=self.play_tab)
        self.play_btns_frm.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        self.play_btns_frm.grid_columnconfigure(1, weight=1)

        self.using_btns = ctk.CTkSegmentedButton(master=self.play_btns_frm, 
                                                 values=["Current", "All", "ChatGPT"],
                                                 command=self.master.set_play_mode)
        self.using_btns.grid(row=0, column=0, padx=5, pady=5, sticky="sw")
        self.using_btns.set("Current")

        self.save_chat_btn = ctk.CTkButton(master=self.play_btns_frm, text="Save Chat Log",
                                             command=self.save_chat)
        self.save_chat_btn.grid(row=1, column=0, padx=5, pady=5, sticky="sw")
        self.save_chat_btn.configure(state="disabled")

        self.play_entry = ctk.CTkTextbox(master=self.play_btns_frm)
        self.play_entry.grid(row=0, column=1, rowspan=2, padx=5, pady=5, sticky="ew")

        self.chat_list_dd = ctk.CTkComboBox(master=self.play_btns_frm, 
                                         values=["Unsaved Session"], command=self.set_chat_log)
        self.chat_list_dd.configure(state="disabled")
        self.chat_list_dd.grid(row=0, column=2, padx=5, pady=5, sticky="se")

        self.enter_btn = ctk.CTkButton(master=self.play_btns_frm, text="Enter",
                                        command=self.master.update_playground)
        self.enter_btn.grid(row=1, column=2, padx=5, pady=5, sticky="se")
        
        self.play_entry.configure(width=0, height=60, corner_radius=c_r, 
                                wrap=wrp, font=fnt)
        
        # Buttons for CodeEditor tab lower frame
        self.lft_btns = ctk.CTkFrame(master=self.edit_tab)
        self.lft_btns.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.code_reload_btn = ctk.CTkButton(master=self.lft_btns, text="Reload All Codes", 
                                             command=self.reload_codes)
        self.code_reload_btn.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.code_clear_btn = ctk.CTkButton(master=self.lft_btns, text="Clear Editor", 
                                            command=self.clear_code)
        self.code_clear_btn.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        self.rt_btns = ctk.CTkFrame(master=self.edit_tab)
        self.rt_btns.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.code_open_btn = ctk.CTkButton(master=self.rt_btns, text="Open Code", 
                                           command=self.load_code)
        self.code_open_btn.grid(row=0, column=2, padx=5, pady=5, sticky="se")
        self.code_save_btn = ctk.CTkButton(master=self.rt_btns, text="Save Code", 
                                           command=self.save_code)
        self.code_save_btn.grid(row=0, column=3, padx=5, pady=5, sticky="se")

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
                                                initialdir=self.master.nato_eng.code_lib_path,
                                                initialfile="myCode.json")

        if file_path:
            code = self.text_edit.get("0.0", "end")
            with open(file_path, "w") as f:
                f.write(code)

    def reload_codes(self):  
        """ Reload the code library files from the default directory. """
        self.master.reload_code_libs()


    def clear_code(self):
        """ Clear the code editor. """
        self.text_edit.delete("0.0", "end")

    def set_chat_log(self, chat_log: str) -> None:
        """ Set the chat log to the given chat log. """
        if chat_log == "New Session":
            self.text_play.delete("0.0", "end")
            self.master.chat_eng.set_new_session()
            return
        else:
            self.chat_list_dd.set(chat_log)
            session_txt = self.master.chat_eng.load_chat_log(chat_log)
            self.text_play.delete("0.0", "end")
            self.text_play.insert("0.0", session_txt)

    def save_chat(self) -> None:
        """ Save the current chat log to a file. """
        self.master.save_chat_session()



class NatoEngine():
    """ The main engine for natoify. """
    def __init__(self, master):
        self.master = master
        self.nato = Natoify()
        self.code_lib_path = self.nato.CODE_LIB_DIR
        self.current_code = self.nato.current_code

    def encode(self, text: str, encrypt: bool) -> str:
        """ Encode the given text using the given library. """
        return self.nato.encode(text, encrypt)

    def decode(self, text: str, encrypt: bool) -> str:
        """ Decode the given text using the given library. """
        return self.nato.decode(text, encrypt)

    def load_library(self, library: str) -> None:
        """ Load and set the given library. """
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

    def list_libraries(self) -> list:
        """ Return a list of all available libraries. """
        return self.nato.list_codes()
    
    def reload_libraries(self) -> None:
        """ Reload the list of libraries. """
        self.nato.CODE_LIBRARY = {}
        self.nato.load_codes()
        self.current_code = self.nato.current_code


# Show the main window
app = NatoApp()
app.mainloop()
