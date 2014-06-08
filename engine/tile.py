#Tile engine prototype

import pyglet, resources

class Tile(pyglet.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		super(Tile,self).__init__(*args, **kwargs)
		
class orangeTile(Tile):
	def __init__(self, *args, **kwargs):
		super(orangeTile,self).__init__(
		img=resources.tile_one, *args, **kwargs)
		
class blueTile(Tile):
	def __init__(self, *args, **kwargs):
		super(blueTile,self).__init__(
		img=resources.tile_two, *args, **kwargs)