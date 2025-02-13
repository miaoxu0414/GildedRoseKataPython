import unittest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    # Test: Aged Brie should increase in quality by 1 each day
    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 1)  

    # Test: Backstage passes should drop to 0 quality after the concert
    def test_backstage_passes_drop_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)  

    # Test: Normal items should decrease in quality by 1 each day
    def test_normal_item_quality_decreases(self):
        items = [Item("Elixir of the Mongoose", 5, 7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 6)  

    # Test: Calling a non-existent method should raise an AttributeError
    def test_call_non_existent_method(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        with self.assertRaises(AttributeError):
            gilded_rose.get_items()  


if __name__ == '__main__':
    unittest.main()
