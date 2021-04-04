#new JV comment 
import sys
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


from kivy.core.window import Window
import fun
from fun import Sandbox_Widget


from importlib import reload


class Sandbox(App):


	def build(self, **kwargs):

		super(Sandbox,self).__init__(**kwargs)

		self.keyboard = Window.request_keyboard(self.keyboard_cleanup, self.root)
		self.keyboard.bind(on_key_down=self.keyboard_trigger)

		self.LT = Sandbox_Widget(Window)

		self.reload_container = BoxLayout()
		self.reload_container.add_widget(self.LT)

		return self.reload_container



	def keyboard_cleanup(self):
		self.keyboard.unbind(on_key_down=self.keyboard_trigger)
		self.keyboard = None


	def keyboard_trigger(self, keyboard, keycode, text, modifiers):
	
		#print(self, keyboard, keycode, text, modifiers)

		if keycode[1] == 'r':
			try:
				self.reload_container.remove_widget(self.LT)

				reload(fun)
				from fun import Sandbox_Widget

				self.LT = Sandbox_Widget(Window)
				self.reload_container.add_widget(self.LT)

			except:
				print("failed to reload!")
				print(sys.exc_info())


		if keycode[1] == 'c':
			self.LT.clear_canvas()


		if keycode[1] == 'v':
			self.LT.new_color()


		if keycode[1] == 'left':
			self.LT.moveleft()

		if keycode[1] == 'right':
			self.LT.moveright()

		if keycode[1] == 'up':
			self.LT.moveup()

		if keycode[1] == 'down':
			self.LT.movedown()

		if keycode[1] == 'spacebar':
			self.LT.pause()

				

if __name__ == "__main__":
	app = Sandbox().run()
