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


    def test_increases_quality_by_one_for_products_that_get_better_as_they_age(self):
        items = [
                Item("Aged Brie", 20, 30),
                Item("Backstage passes to a TAFKAL80ETC concert", 20, 30)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self._assert_quality_and_sell_in(items[0], sell_in=19, quality=31)
        self._assert_quality_and_sell_in(items[1], sell_in=19, quality=31)


    def test_increase_quality_by_two_for_products_that_get_better_as_they_age_and_there_are_10_days_or_less_left(self):
        items = [
                Item("Aged Brie", 10, 34),
                Item("Backstage passes to a TAFKAL80ETC concert", 8, 30)
                ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # FIXME Possible BUG
        # self._assert_quality_and_sell_in(items[0], sell_in=9, quality=36)
        self._assert_quality_and_sell_in(items[1], sell_in=7, quality=32)

    def test_quality_zero_for_backstage_passes_and_brie_when_we_have_passed_the_sell_in_date(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)

        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        self._assert_quality_and_sell_in(item, sell_in=-1, quality=0)

    def test_decreases_the_quality_of_the_rpoducts_twice_as_fast_when_we_have_passed_the_sell_in_date(self):
        items = [
                Item("+5 Dexterity Vest", 0, 20),
                Item("Conjured Mana Cake", 0, 6)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self._assert_quality_and_sell_in(items[0], sell_in=-1, quality=18)
        self._assert_quality_and_sell_in(items[1], sell_in=-1, quality=4)

    def test_increases_the_quality_by_three_of_the_products_that_get_better_as_they_age_when_there_are_5_days_or_less_left(self):
        items = [
                Item("Aged Brie", 4, 11),
                Item("Backstage passes to a TAFKAL80ETC concert", 5, 15)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # FIXME Possible BUG
        #self._assert_quality_and_sell_in(items[0], sell_in=3, quality=14)
        self._assert_quality_and_sell_in(items[1], sell_in=4, quality=18)

    def test_does_not_alter_quality_of_sulfuras_witch_is_allways_80(self):
        items = [ Item("Sulfuras, Hand of Ragnaros", 0, 80), ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self._assert_quality_and_sell_in(items[0], sell_in=0, quality=80)

    def test_does_not_increase_quality_over_50(self):
        items = [ Item("Aged Brie", 4, 49), ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self._assert_quality_and_sell_in(items[0], sell_in=3, quality=50)

    def _assert_quality_and_sell_in(self, item, sell_in, quality):
        self.assertEquals(sell_in, item.sell_in)
        self.assertEquals(quality, item.quality)


if __name__ == '__main__':
    unittest.main()
