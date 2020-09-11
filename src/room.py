# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, roomitems):
        self.name = name
        self.description = description
        self.roomitems = roomitems

class Item:
    def __init__(self, name, room):
        self.name = name
        self.room = room
