#Resource handler
import pyglet
from pyglet.gl import *

pyglet.resource.path = ['resources']
pyglet.resource.reindex()

tile_one = pyglet.resource.image("tile_test_1.png")
tile_two = pyglet.resource.image("tile_test_2.png")
tile_three = pyglet.resource.image("tile_test_3.png")