#Main runner file

import pyglet, math, random
from random import choice
from engine import tile, resources, map, util

windowDebug = False
scrollSpeed = 10

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
		
		self.mouseX = None
		self.mouseY = None
		self.mouseDX = None
		self.mouseDY = None
	
	def on_mouse_motion(self, x, y, dx, dy):
		self.mouseX = x
		self.mouseY = y
		self.mouseDX = dx
		self.mouseDY = dy
		
		if windowDebug: print self.mouseX, self.mouseY
		
		if self.mouseX in range(0, 10):
			for i in self.map.tileMap:
				i.x += scrollSpeed
		if self.mouseX in range((self.windowWidth - 10), 
										self.windowWidth):
			for i in self.map.tileMap:
				i.x -= scrollSpeed
		if self.mouseY in range(0, 10):
			for i in self.map.tileMap:
				i.y += scrollSpeed
		if self.mouseY in range((self.windowHeight - 10), 
										self.windowHeight):
			for i in self.map.tileMap:
				i.y -= scrollSpeed
	
	def on_mouse_press(self, x, y, button, modifiers):
		
		if button == pyglet.window.mouse.LEFT:
			print x, y
	
	def update(self, dt):
		self.on_mouse_motion(self.mouseX, self.mouseY, 
							self.mouseDX, self.mouseDY)
		
	def on_draw(self):
		self.clear()
		self.label.draw()
		self.map.map_batch.draw()
	
if __name__ == '__main__':
	window = mainWindow()
	#window.set_exclusive_mouse(True)
	pyglet.clock.schedule_interval(window.update, 1/120.0)
	pyglet.app.run()