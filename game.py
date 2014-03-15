#Main runner file

import pyglet, math, random
from random import choice
from engine import tile, resources

SCREEN_HEIGHT = 768
SCREEN_WIDTH = 1024
tile_width = 32
tile_height = 32

map_batch = pyglet.graphics.Batch()

tile1 = resources.tile_one
tile2 = resources.tile_two

tile_list = [tile1,tile2]
map = []

window = pyglet.window.Window(SCREEN_WIDTH,SCREEN_HEIGHT)

map_width = 1280 / 32
map_height = 1024 / 32
map_size = (map_width * map_height)

for a in xrange(map_height):
	tile = choice(tile_list)
	for j in xrange(map_width):
		xpos = j * 32
		ypos = a * 32
		map.append(pyglet.sprite.Sprite(tile, xpos, ypos, batch=map_batch))
		
@window.event
def on_draw():
	map_batch.draw()
	
if __name__ == '__main__':
	pyglet.app.run()