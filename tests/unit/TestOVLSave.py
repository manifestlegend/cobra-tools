import unittest
from generated.formats.ovl import OvlFile, get_game, set_game


class TestOVLSave(unittest.TestCase):
	"""create a new empty OVL, save the ovl with diff formats, and try loading it again"""

	# load an empty ovl file for each test case
	def setUp(self):
		self.ovlfile = OvlFile()

	def test_ovl_save_pc(self):
		game = "Planet Coaster"
		file = 'tests/tmp/pc.ovl'
		set_game(self.ovlfile.context, game)
		set_game(self.ovlfile, game)
		self.ovlfile.save(file)
		self.ovlfile.load(file)
		self.assertEqual(game, get_game(self.ovlfile)[0].value, "Should have the same game")

	def test_ovl_save_pz(self):
		game = "Planet Zoo"
		file = 'tests/tmp/pz.ovl'
		set_game(self.ovlfile.context, game)
		set_game(self.ovlfile, game)
		self.ovlfile.save(file)
		self.ovlfile.load(file)
		self.assertEqual(game, get_game(self.ovlfile)[0].value, "Should have the same game")

	def test_ovl_save_jwe1(self):
		game = "Jurassic World Evolution"
		file = 'tests/tmp/jwe.ovl'
		set_game(self.ovlfile.context, game)
		set_game(self.ovlfile, game)
		self.ovlfile.save(file)
		self.ovlfile.load(file)
		self.assertEqual(game, get_game(self.ovlfile)[0].value, "Should have the same game")

	def test_ovl_save_jwe2(self):
		game = "Jurassic World Evolution 2"
		file = 'tests/tmp/jwe2.ovl'
		set_game(self.ovlfile.context, game)
		set_game(self.ovlfile, game)
		self.ovlfile.save(file)
		self.ovlfile.load(file)
		self.assertEqual(game, get_game(self.ovlfile)[0].value, "Should have the same game")


if __name__ == '__main__':
	unittest.main()