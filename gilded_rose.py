# -*- coding: utf-8 -*-

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                # Aged Brie increases in quality as it gets older
                if item.quality < 50:
                    item.quality += 1
                if item.sell_in <= 0 and item.quality < 50:
                    item.quality += 1
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                # Backstage passes increase in quality as the concert approaches
                if item.quality < 50:
                    item.quality += 1
                    if item.sell_in < 11 and item.quality < 50:
                        item.quality += 1
                    if item.sell_in < 6 and item.quality < 50:
                        item.quality += 1
                if item.sell_in <= 0:
                    item.quality = 0
            elif item.name != "Sulfuras, Hand of Ragnaros":
                # Normal items decrease in quality
                if item.quality > 0:
                    item.quality -= 1
                if item.sell_in <= 0 and item.quality > 0:
                    item.quality -= 1

            # Decrease sell_in for all items except Sulfuras
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1
