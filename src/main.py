"""
@author: Daniel Torac
year: 2023
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import os


PATH = os.path.join("./data/dat")
ICON = os.path.join("./data/icon.jpg")


def read_file(filename):
	try:
		with open(filename, 'r') as f:
			return f.read()
	except IOError:
		print("Error: could not read file " + filename)


def write_file(filename, count: int):
	try:
		with open(filename, 'w') as f:
			f.write(str(count))
	except IOError:
		print("Error: could not write file " + filename)


class MainBoxLayout(BoxLayout):
	count_str = read_file(filename=PATH)
	if count_str is None:
		count_str = "0"
	count = int(count_str)
	display = StringProperty(count_str)
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	
	def add(self):
		self.count += 1
		write_file(filename=PATH, count=self.count)
		self.check_color()
		self.display = read_file(filename=PATH)
	
	def remove(self):
		self.count -= 1
		write_file(filename=PATH, count=self.count)
		self.check_color()
		self.display = read_file(filename=PATH)
	
	def check_color(self):
		if self.count > -1:
			self.ids.count_coffee.color = (152 / 255, 251 / 255, 152 / 255, 1)
		else:
			self.ids.count_coffee.color = (180 / 255, 0, 130 / 255, 1)
		return self.ids.count_coffee.color


class CCI(App):
	def build(self):
		self.title = "Coffee Mania"
		self.icon = ICON


if __name__ == "__main__":
	CCI().run()
