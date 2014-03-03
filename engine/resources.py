#Resource handler
import pyglet

pyglet.resource.path = ['resources']
pyglet.resource.reindex()

tile_one = pyglet.resource.image("tile_test.jpg")
tile_two = pyglet.resource.image("tile_test_2.jpg")