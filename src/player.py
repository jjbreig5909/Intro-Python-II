# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentroom, items):
        self.name = name
        self.currentroom = currentroom
        self.items = items
    def take_item(self, item):
        take = Take(item, self)
        self.items.append(take)
    def drop_item(self, item):
        take = Drop(item, self)
        self.items.remove(take)
        
class Take:
    def __init__(self, item, player):
        self.item = item
        self.player = player
class Drop:
    def __init__(self, item, player):
        self.item = item
        self.player = player

