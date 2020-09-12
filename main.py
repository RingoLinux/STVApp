import requests
from bs4 import BeautifulSoup
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty




class STV_Home(Screen):
	menuHome = "Trang Chủ"
class STV_ScreenManager(ScreenManager):
	pass
class MyApp(App):
	def build(self):
		return STV_Home()
		
if __name__ == '__main__':
	MyApp().run() 