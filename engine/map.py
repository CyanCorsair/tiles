#Map class.
#Stores all map mechanisms
#and handles creation of map array.

import numpy, pyglet, math
from random import choice, randint
import tile, resources

mapDebug = False

class Map(object):
	def __init__(self, game):
		self.tile1 = resources.tile_one
		self.tile2 = resources.tile_two
		
		self.game = game
		self.map_batch = pyglet.graphics.Batch()
		
		self.tileWidth = 32
		self.tileHeight = 32
		self.mapWidth = game.windowWidth / self.tileWidth
		self.mapHeight = game.windowHeight / self.tileHeight
		self.tileMap = []
		
		self.isoY = None
		self.isoX = None
		self.cartY = None
		self.cartX = None
		self.locX = None
		self.locY = None
		
		self.createArray()
		
	def createArray(self):
		self.tiles = numpy.zeros((self.mapHeight, self.mapWidth), dtype=int)
		for x in range(self.mapWidth):
			for y in range(self.mapHeight):
				self.tiles[y,x] = randint(0,1)
		
		if mapDebug: print "Tiles: \n", self.tiles
	
	def isoToCart(self, x, y):
		self.cartX = (2 * y + x) / 2
		self.cartY = (2 * y - x) / 2
		return self.cartX, self.cartY
	
	def cartToIso(self, x, y):
		self.isoX = x - y
		self.isoY = (x + y) / 2
		return self.isoX, self.isoY
	
	def getTileCords(self, x, y):
		self.isoX = x
		self.isoY = Y
		self.locX = Math.floor(self.isoX / self.tileHeight)
		self.locY = Math.floor(self.isoY / self.tileHeight)
		return self.locX, self.locY
	
	def drawMap(self):
		for i in range(self.mapWidth):
			for j in range(self.mapHeight):
				self.plotid = self.tiles[j,i]
				self.x = i * self.tileHeight
				self.y = j * self.tileWidth
				self.cartToIso(self.x, self.y)
				if self.plotid == 0:
					self.tileMap.append(tile.orangeTile(x=self.isoX, y=self.isoY, batch=self.map_batch))
				elif self.plotid == 1:
					self.tileMap.append(tile.blueTile(x=self.isoX, y=self.isoY, batch=self.map_batch))
				else:
					print "Error"