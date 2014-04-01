#Main runner file

import pyglet, math, random
from random import choice
from engine import tile, resources, map

windowHeight = 768
windowWidth = 1024

class mainWindow(pyglet.window.Window):
	def __init__(self):
		super(mainWindow, self).__init__(
			height=windowHeight,
			width=windowWidth)
			
		self.windowHeight = windowHeight
		self.windowWidth = windowWidth
		
		self.label = pyglet.text.Label('Main Window')
		self.map = map.Map(self)
		self.map.drawMap()
	
	#def update(self, dt):
	#	pass
	
	def on_draw(self):
		self.clear()
		self.label.draw()
		self.map.map_batch.draw()
		
if __name__ == '__main__':
	window = mainWindow()
	#pyglet.clock.schedule_interval(battleWindow.update, 1/120.0)
	pyglet.app.run()