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

       	self._assert_quality_and_sell_in(items[0], sell_in=9, quality=19)
       	self._assert_quality_and_sell_in(items[1], sell_in=2, quality=5)

    def _assert_quality_and_sell_in(self, item, sell_in, quality):
    	self.assertEquals(sell_in, item.sell_in)
        self.assertEquals(quality, item.quality)
        



if __name__ == '__main__':
    unittest.main()
