#Main runner file

import pyglet, math, random
from random import choice
from engine import tile, resources

SCREEN_HEIGHT = 768
SCREEN_WIDTH = 1024
tile_width = 32
tile_height = 32

tile_batch = pyglet.graphics.Batch()
map_batch = pyglet.graphics.Batch()

tile1 = tile.Tile(img=resources.tile_one,x=0,y=0,batch=tile_batch)
tile2 = tile.Tile(img=resources.tile_two,x=0,y=0,batch=tile_batch)

tile_list = [tile1,tile2]
map_count = []
map = []


window = pyglet.window.Window(SCREEN_WIDTH,SCREEN_HEIGHT)

map_width = SCREEN_WIDTH / tile_width
map_height = SCREEN_HEIGHT / tile_height

def getTilecount():
	i = 0
	
	map_size = map_width * map_height
	
	while i < map_size:
		i+= 1
		map_count.append(i)
		return map_count
	
	createTilemap()
		
def createTilemap():
	for i in map_count:
		tileimg = choice(tile_list)
		if tileimg.x == SCREEN_WIDTH:
			tileimg.x = -1
			tileimg.y += tile_height
			tileimg.x += tile_width
		else:
			tileimg.x += tile_width
		map_batch
	return map
		
@window.event
def on_draw():
	#window.clear()
	for tile in map:
		tile.draw()
	
if __name__ == '__main__':
	pyglet.app.run()