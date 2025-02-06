import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):

    def test_normal_item_quality_decreases(self):
        """Test that normal items decrease in quality each day"""
        items = [Item("Elixir of the Mongoose", 5, 7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(items[0].sell_in, 4)  # Sell-in decreases
        self.assertEqual(items[0].quality, 6)  # Quality should decrease

    def test_aged_brie_increases_in_quality(self):
        """Test that Aged Brie increases in quality as it ages"""
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(items[0].sell_in, 1)
        self.assertEqual(items[0].quality, 1)  # Quality should increase

    def test_backstage_passes_drop_to_zero_after_concert(self):
        """Test that Backstage passes' quality drops to zero after concert"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 0)  # Quality drops to zero

    def test_call_non_existent_method(self):
        """Syntax Error: Trying to call a method that does not exist"""
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        
        with self.assertRaises(AttributeError):
            gilded_rose.get_items()  # Method does not exist

if __name__ == '__main__':
    unittest.main()

