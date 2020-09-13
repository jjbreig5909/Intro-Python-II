# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentroom, items):
        self.name = name
        self.currentroom = currentroom
        self.items = []
    def take_item(self, item):
        self.items.append(item)
    def drop_item(self, item):
        self.items.remove(item)

class Take:
    def __init__(self, item, player):
        self.item = item
        self.player = player
class Drop:
    def __init__(self, item, player):
        self.item = item
        self.player = player

