# -*- coding: utf-8 -*-

class Item:
    """DO NOT CHANGE THIS CLASS!!!"""
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
        # Map item names to their corresponding strategies
        self.strategies = {
            "Aged Brie": AgedBrieStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
            "Conjured": ConjuredItemStrategy(),  # Added support for Conjured items
        }
        self.default_strategy = NormalItemStrategy()  # Default strategy for normal items

    def update_quality(self):
        for item in self.items:
            # Select the appropriate strategy based on item name
            strategy = self.strategies.get(item.name, self.default_strategy)
            strategy.update_quality(item)  # Update quality using the selected strategy
            # Update sell_in for all items except Sulfuras
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1

# Strategy Interface
class QualityStrategy:
    """Interface for quality update behavior."""
    def update_quality(self, item):
        pass

# Concrete Strategies
class AgedBrieStrategy(QualityStrategy):
    """Strategy for updating quality of 'Aged Brie'."""
    def update_quality(self, item):
        if item.quality < 50:
            item.quality += 1  # Quality increases by 1
        if item.sell_in <= 0 and item.quality < 50:
            item.quality += 1  # Quality increases again if sell_in is past


class BackstagePassStrategy(QualityStrategy):
    """Strategy for updating quality of 'Backstage passes'."""
    def update_quality(self, item):
        if item.quality < 50:
            item.quality += 1  # Base quality increase
            if item.sell_in < 11 and item.quality < 50:
                item.quality += 1  # Increase more if sell_in < 11
            if item.sell_in < 6 and item.quality < 50:
                item.quality += 1  # Increase even more if sell_in < 6
        if item.sell_in <= 0:
            item.quality = 0  # Quality drops to 0 after the concert


class NormalItemStrategy(QualityStrategy):
    """Strategy for updating quality of normal items."""
    def update_quality(self, item):
        if item.quality > 0:
            item.quality -= 1  # Quality decreases by 1
        if item.sell_in <= 0 and item.quality > 0:
            item.quality -= 1  # Quality decreases again if sell_in is past


class SulfurasStrategy(QualityStrategy):
    """Strategy for 'Sulfuras', which never changes."""
    def update_quality(self, item):
        pass  # Sulfuras never changes in quality or sell_in
            # Decrease sell_in for all items except Sulfuras
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1
