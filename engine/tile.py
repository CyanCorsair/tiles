#Tile engine prototype

import pyglet, resources

class Tile(pyglet.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		super(Tile,self).__init__(*args, **kwargs)
		
		self.tile_width = 32
		self.tile_height = 32