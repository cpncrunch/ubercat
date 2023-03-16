#!/usr/bin/python3

"""
This program was originally created by Isaac Privett on 03-16-2023
Feel free to use it as you wish
"""

import subprocess
import tkinter as tk
from tkinter import ttk

class NetcatManager:
	def __init__(self):
		self.listeners = {}

	def create_listener(self, port):
		if port in self.listeners:
			return False
		listener = subprocess.Popen(["nc", "-lvn", "-p",  str(port)], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
		self.listeners[port] = listener
		return True

	def close_listener(self, port):
		if port not in self.listeners:
			return False
		listener = self.listeners[port]
		listener.terminate()
		listener.wait()
		del self.listeners[port]
		return True

class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Ubercat: Netcat Listener Manager")
		self.geometry("400x300")
		self.netcat_manager = NetcatManager()
		self.create_widgets()

	def create_widgets(self):
		self.header_frame = ttk.Frame(self)
		self.header_frame.pack(fill="x", padx=5, pady=5)
		self.header_label = ttk.Label(self.header_frame, text="Ubercat: Netcat Listener Manager")
		self.header_label.pack(side="left")

		self.form_frame = ttk.Frame(self)
		self.form_frame.pack(fill="x", padx=5, pady=5)

		self.port_label = ttk.Label(self.form_frame, text="Port:")
		self.port_label.grid(row=0, column=0)
		self.port_entry = ttk.Entry(self.form_frame)
		self.port_entry.grid(row=0, column=1)

		self.add_listener_button = ttk.Button(self.form_frame, text="Add Listener", command=self.add_listener)
		self.add_listener_button.grid(row=0, column=2)
		
		self.listeners_frame = ttk.Frame(self)
		self.listeners_frame.pack(fill="both", expand=True, padx=5, pady=5)

		self.listeners_listbox = tk.Listbox(self.listeners_frame)
		self.listeners_listbox.pack(side="left", fill="both", expand=True)

		self.scrollbar = ttk.Scrollbar(self.listeners_frame, orient="vertical", command=self.listeners_listbox.yview)
		self.scrollbar.pack(side="right", fill="y")
		self.listeners_listbox.config(yscrollcommand=self.scrollbar.set)

		self.bottom_frame = ttk.Frame(self)
		self.bottom_frame.pack(fill="x", padx=5, pady=5)

		self.remove_listener_button = ttk.Button(self.bottom_frame, text="Remove Listener", command=self.remove_listener)
		self.remove_listener_button.pack(side="right")

	def add_listener(self):
		port_str = self.port_entry.get()
		try:
			port = int(port_str)
		except ValueError:
			return

		if self.netcat_manager.create_listener(port):
			self.listeners_listbox.insert("end", f"Port {port}")
		else:
			print("Failed to create listener.")

	def remove_listener(self):
		selection = self.listeners_listbox.curselection()
		if not selection:
			return

		port_str = self.listeners_listbox.get(selection[0]).split()[-1]
		port = int(port_str)
		if self.netcat_manager.close_listener(port):
			self.listeners_listbox.delete(selection[0])
		else:
			print("Failed to remove listener.")

if __name__ == "__main__":
	app = App()
	app.mainloop()
