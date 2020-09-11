# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentroom):
        self.name = name
        self.currentroom = currentroom
    def take_item(self, item):
        take = Take(item, self)
        self.items.append(take)
class Take:
    def __init__(self, item, player):
        self.item = item
        self.player = player

