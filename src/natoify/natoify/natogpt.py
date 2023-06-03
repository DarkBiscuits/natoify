"""
This module adds chatGPT functionality to the Natoity app.
"""

import os
import json
import glob
import datetime
from typing import Tuple
import openai


class NatoGPT():
	"""
	This class is used to chat with chatGPT.

	Attributes:
		CHAT_LOG_DIR (str): The path to the chat log directory.
		messages (list): A list of messages in the chat session.
		default_msg_len (int): The default length of the messages list.

	Methods:
		set_new_session() -> None: Set a new chat session.
		add_to_chat(message: str) -> Tuple[str, str]: Add a message to the chat session.
		save_chat_log() -> None: Save the chat session to the chat_log directory.
		load_chat_log(chat_log: str) -> str: Load a chat log from the chat_log directory.
		get_chat_logs() -> list: Get a list of all chat logs in the chat_log directory.
	
	"""

	def __init__(self):
		# Get current director and path to code_lib directory
		CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
		self.CHAT_LOG_DIR = os.path.join(CURRENT_DIR, "../chat_log")

		# Set the api key and system message
		openai.api_key = os.environ.get('OPENAI_API_KEY')
		self.set_new_session()
	
	def set_new_session(self) -> None:
		self.messages = [ {"role": "system", "content":
					"You are a intelligent, friendly, and sarcasticly funny assistant."} ]
		self.default_msg_len = len(self.messages)
		
	def add_to_chat(self, message: str) -> Tuple[str, str]:
		"""Send message to chatGPT and return the reply."""
		prompt = message
		if message:
			self.messages.append(
				{"role": "user", "content": message},
			)
			chat = openai.ChatCompletion.create(
				model="gpt-3.5-turbo", messages=self.messages
			)
		reply = chat.choices[0].message.content
		# print(f"ChatGPT: {reply}")
		self.messages.append({"role": "assistant", "content": reply})
		return prompt, reply

	def save_chat_log(self) -> None:
		"""Save the chat log to the chat_log directory.
		It will be saved as chat_<date-time>.json if a
		chat session has occurred.
		"""
		# Check if a chat session has occurred, if not, return
		if len(self.messages) == self.default_msg_len:
			return

		# Get the current date and time to form the chat log name
		now = datetime.datetime.now()
		chat_fname = now.strftime("chat_%Y-%m-%d-%H-%M-%S.json")
		chat_fpath = os.path.join(self.CHAT_LOG_DIR, chat_fname)

		# Save the chat log to the chat_log directory
		with open(chat_fpath, 'w') as f:
			json.dump(self.messages, f, indent=4)

	def load_chat_log(self, chat_log: str) -> str:
		"""Load a chat log by name from the chat_log directory."""

		# Get the path to the chat log
		fpath = os.path.join(self.CHAT_LOG_DIR, chat_log)

		# Load the chat log
		with open(fpath, 'r') as f:
			self.messages = json.load(f)

		# Get the user and assistant messages
		user_messages = [m['content'] for m in self.messages if m['role'] == 'user']
		assistant_messages = [m['content'] for m in self.messages if m['role'] == 'assistant']

		# Sort the messages so that the user and assistant messages are in order
		messages = []
		for i in range(len(user_messages)):
			messages.append(user_messages[i])
			messages.append(f"{'*'*60}")
			messages.append(assistant_messages[i])
			messages.append(f"{'='*60}")
		
		# Convert the messages to a string
		messages = '\n'.join(messages)
		return messages

	def get_chat_logs(self) -> list:
		"""Get a list of all chat logs in the chat_log directory."""

		# Get the path to the chat log
		chat_files = glob.glob(f"{self.CHAT_LOG_DIR}/*.json")
		return sorted(chat_files, key=os.path.getmtime, reverse=True)

