#Map class.
#Stores all map mechanisms
#and handles creation of map array.

import numpy, pyglet, math
from random import choice, randint
import tile, resources
import cPickle as pickle

mapDebug = False
algoDebug = True

class Map(object):
	def __init__(self, game):
		self.tile1 = resources.tile_one
		self.tile2 = resources.tile_two
		
		self.game = game
		self.map_batch = pyglet.graphics.Batch()
		
		self.hugeMap = [2046, 2046]
		self.largeMap = [1280, 1280]
		self.mediumMap = [1024, 1024]
		self.smallMap = [768, 768]
		
		self.tileWidth = 32
		self.tileHeight = 32
		self.mapWidth = self.hugeMap[0] / self.tileWidth
		self.mapHeight = self.hugeMap[1] / self.tileHeight
		self.tileMap = []
		
		self.isoY = None
		self.isoX = None
		self.cartY = None
		self.cartX = None
		self.locX = None
		self.locY = None
		
		#self.createArray()
		self.baseAlgorithm()
		
	def createArray(self):
		self.tiles = numpy.zeros((self.mapHeight, self.mapWidth), dtype=int)
		for x in range(self.mapWidth):
			for y in range(self.mapHeight):
				self.tiles[y,x] = randint(0,2)
		
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
	
	def baseAlgorithm(self):
		self.tiles = numpy.zeros((self.mapHeight, self.mapWidth), dtype=int)
		for x in range(self.mapWidth):
			for y in range(self.mapHeight):
				if x == 0:
					self.tiles[y,x] = 0
				elif y == 0:
					self.tiles[y,x] = 0
				elif x == 62:
					self.tiles[y,x] = 0
				elif y == 62:
					self.tiles[y,x] = 0
				else:
					self.tiles[y,x] = randint(1,2)
		
		if algoDebug: print "Tiles: \n", self.tiles
	
	def drawMap(self):
		for i in range(self.mapWidth):
			for j in range(self.mapHeight):
				self.plotid = self.tiles[j,i]
				self.x = i * self.tileHeight
				self.y = j * self.tileWidth
				self.cartToIso(self.x, self.y)
				if self.plotid == 0:
					self.tileMap.append(tile.orangeTile(x=self.isoX, 
									y=self.isoY, batch=self.map_batch))
				elif self.plotid == 1:
					self.tileMap.append(tile.blueTile(x=self.isoX, 
									y=self.isoY, batch=self.map_batch))
				elif self.plotid == 2:
					self.tileMap.append(tile.greenTile(x=self.isoX, 
									y=self.isoY, batch=self.map_batch))
				else:
					print "Error"