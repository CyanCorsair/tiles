#Map class.
#Stores all map mechanisms
#and handles creation of map array.

import numpy, pyglet, math
from random import choice, randint
import tile, resources

debug = False

class Map(object):
	def __init__(self, game):
		self.tile1 = resources.tile_one
		self.tile2 = resources.tile_two
		
		self.game = game
		self.map_batch = pyglet.graphics.Batch()
		
		self.mapWidth = game.windowWidth / 32
		self.mapHeight = game.windowHeight / 32
		self.tileMap = []
		
		self.createArray()
		
	def createArray(self):
		self.tiles = numpy.zeros((self.mapHeight, self.mapWidth), dtype=int)
		for x in range(self.mapWidth):
			for y in range(self.mapHeight):
				self.tiles[y,x] = randint(0,1)
		
		if debug: print "Tiles: \n", self.tiles
		
	def drawMap(self):
		for a in range(self.mapWidth):
			for j in range(self.mapHeight):
				self.plotid = self.tiles[j,a]
				#self.choice = tile.tileList[self.plotid]
				self.x = a * 32
				self.y = j * 32
				if self.plotid == 0:
					self.tileMap.append(tile.orangeTile(x=self.x, y=self.y, batch=self.map_batch))
				elif self.plotid == 1:
					self.tileMap.append(tile.blueTile(x=self.x, y=self.y, batch=self.map_batch))
				else:
					print "Error"
				#self.tileMap.append(tile.Tile(self.choice, self.x, self.y, batch=self.map_batch))
		#print self.tileMap