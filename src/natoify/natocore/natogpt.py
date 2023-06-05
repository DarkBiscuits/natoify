"""
This module adds chatGPT functionality to the Natoity app.
"""

import os
import json
import glob
import datetime
from typing import Tuple
import openai
import tiktoken
from tkinter import messagebox


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
		num_tokens_from_messages(messages: list) -> int: Get the number of tokens in a list of messages.
	
	"""

	def __init__(self, api_key: str):
		'''Get current directory and path to code_lib directory. 
		Set the api key and system message storage.
		
		Args:
			api_key (str): The api key for the openai api.

		'''
		CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
		self.CHAT_LOG_DIR = os.path.join(CURRENT_DIR, "../chat_log")

		# Set the api key and system message
		openai.api_key = api_key
		self.all_messages = []
		self.set_new_session()
		self.current_tokens = 0
	
	def set_new_session(self) -> None:
		"""Set defaults for a new chat session."""

		self.messages = [ {"role": "system", "content":
					"You are a intelligent, friendly, and funny assistant."} ]
		self.all_messages.append(self.messages[0])
		self.default_msg_len = len(self.messages)
		
	def add_to_chat(self, message: str) -> Tuple[str, str]:
		"""Send message to chatGPT and return the reply.
		
		Args:
			message (str): The message to send to chatGPT (prompt).

		Returns:	
			prompt (str): The message sent to chatGPT.
			reply (str): The reply from chatGPT.
		
		"""

		prompt = message
		
		if message:
			# Check token count and shorten messages if necessary
			msg = {"role": "user", "content": message}
			msgs_tokens = self.num_tokens_from_messages(self.messages)
			msgs_tokens += self.num_tokens_from_messages([msg])

			if msgs_tokens > 2500:
				num_back = int(len(self.messages) / 2) * -1
				self.messages = self.messages[num_back:]
		
			self.messages.append(msg)
			self.all_messages.append(msg)

			chat = openai.ChatCompletion.create(
				model="gpt-3.5-turbo", messages=self.messages
			)
			reply = chat.choices[0].message.content
			
			# Add the reply to the messages list
			rply = {"role": "assistant", "content": reply}
			self.messages.append(rply)
			self.all_messages.append(rply)

			msgs_tokens = self.num_tokens_from_messages(self.messages)
			self.current_tokens = msgs_tokens
			print(f'Last msg total tokens: {msgs_tokens}')
		
		return prompt, reply

	def save_chat_log(self) -> None:
		"""Save the chat log to the chat_log directory.
		It will be saved as chat_<date-time>.json if a
		chat session has occurred.
		"""

		# Check if a chat session has occurred, if not, return
		if len(self.all_messages) == self.default_msg_len:
			return

		# Get the current date and time to form the chat log name
		now = datetime.datetime.now()
		chat_fname = now.strftime("chat_%Y-%m-%d-%H-%M-%S.json")
		chat_fpath = os.path.join(self.CHAT_LOG_DIR, chat_fname)

		# Save the chat log to the chat_log directory
		with open(chat_fpath, 'w') as f:
			json.dump(self.all_messages, f, indent=4)

	def load_chat_log(self, chat_log: str) -> str:
		"""Load a chat log by name from the chat_log directory.
		
		Args:
			chat_log (str): The name of the chat log to load.
			
		Returns:
			chat_log (str): All messages in the chat log as a single string.
		
		"""

		# Get the path to the chat log
		fpath = os.path.join(self.CHAT_LOG_DIR, chat_log)

		# Load the chat log
		try:
			with open(fpath, 'r') as f:
				self.all_messages = json.load(f)
		except json.decoder.JSONDecodeError:
			messagebox.showerror("Error", "Improperly formatted json. Probably a failed final response. Check the file.")
			return

		# Load the all_messages list and reduce the messages list if necessary
		tks = self.num_tokens_from_messages(self.all_messages)
		if tks > 2500:
			num_back = int(len(self.all_messages) * (2500/tks)) * -1
			self.messages = self.all_messages[num_back:]
			print(len(self.all_messages), len(self.messages))

		# Get the user and assistant messages
		user_messages = [m['content'] for m in self.all_messages if m['role'] == 'user']
		assistant_messages = [m['content'] for m in self.all_messages if m['role'] == 'assistant']

		# Sort the messages so that the user and assistant messages are in order
		messages = []
		
		# If there are more user messages than assistant messages, add a missing assistant message
		if len(user_messages) > len(assistant_messages):
			assistant_messages.append('MISSING ASSISTANT MESSAGE')

		for i in range(len(user_messages)):
			messages.append(user_messages[i])
			messages.append(f"{'*'*60}")
			messages.append(assistant_messages[i])
			messages.append(f"{'='*60}")
		
		# Convert the messages to a string
		messages = '\n'.join(messages)
		return messages

	def get_chat_logs(self) -> list:
		"""Get a list of all chat logs in the chat_log directory.
		
		Returns:
			chat_logs (list): A list of all chat logs in the chat_log directory.
		
		"""

		# Get the path to the chat log
		chat_files = glob.glob(f"{self.CHAT_LOG_DIR}/*.json")
		return sorted(chat_files, key=os.path.getmtime, reverse=True)
	
	def num_tokens_from_messages(self, messages, model="gpt-3.5-turbo-0301"):
		"""Returns the number of tokens used by a list of messages.
		
		Args:
			messages (list): A list of messages.
			model (str): The model to use for tokenization. (default: "gpt-3.5-turbo-0301")

		Returns:
			num_tokens (int): The number of tokens that will be used by the messages.

		"""
		try:
			encoding = tiktoken.encoding_for_model(model)
		except KeyError:
			print("Warning: model not found. Using cl100k_base encoding.")
			encoding = tiktoken.get_encoding("cl100k_base")
		if model == "gpt-3.5-turbo":
			print("Warning: gpt-3.5-turbo may change over time. Returning num tokens assuming gpt-3.5-turbo-0301.")
			return self.num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301")
		elif model == "gpt-4":
			print("Warning: gpt-4 may change over time. Returning num tokens assuming gpt-4-0314.")
			return self.num_tokens_from_messages(messages, model="gpt-4-0314")
		elif model == "gpt-3.5-turbo-0301":
			tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
			tokens_per_name = -1  # if there's a name, the role is omitted
		elif model == "gpt-4-0314":
			tokens_per_message = 3
			tokens_per_name = 1
		else:
			raise NotImplementedError(f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")
		num_tokens = 0
		for message in messages:
			num_tokens += tokens_per_message
			for key, value in message.items():
				num_tokens += len(encoding.encode(value))
				if key == "name":
					num_tokens += tokens_per_name
		num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
		return num_tokens

