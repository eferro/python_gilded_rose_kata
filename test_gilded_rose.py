# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_decreses_by_one_the_quality_and_sell_in_for_regular_items(self):
        items = [
        	Item("+5 Dexterity Vest", 10, 20),
        	Item("Conjured Mana Cake", 3,6) 
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(19, items[0].quality)
        self.assertEquals(2, items[1].sell_in)
        self.assertEquals(5, items[1].quality)

if __name__ == '__main__':
    unittest.main()
