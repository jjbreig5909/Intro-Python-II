from room import Room, Item
from player import Player, Take

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",["compass"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [""]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [""]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["torch"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["dusty coin"]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = {'newplayer': Player('Jeff', room['outside'], [""])}
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
game = True
while game == True:
    usermove = input("Please input a command: ")
    if usermove == "q":
        print("Thanks for playing!")
        game = False
    elif usermove == "n":
        if hasattr(player['newplayer'].currentroom, 'n_to'):
            print("You moved north!")
            player['newplayer'].currentroom = player['newplayer'].currentroom.n_to
            print (player['newplayer'].currentroom.name)
            print(player['newplayer'].currentroom.description)
        else:
            print("You can't move that direction!")
    elif usermove == "s":
        if hasattr(player['newplayer'].currentroom, 's_to'):
            print("You moved south!")
            player['newplayer'].currentroom = player['newplayer'].currentroom.s_to
            print (player['newplayer'].currentroom.name)
            print(player['newplayer'].currentroom.description)
        else:
            print("You can't move that direction!")
    elif usermove == "e":
        if hasattr(player['newplayer'].currentroom, 'e_to'):
            print("You moved east!")
            player['newplayer'].currentroom = player['newplayer'].currentroom.e_to
            print (player['newplayer'].currentroom.name)
            print(player['newplayer'].currentroom.description)
        else:
            print("You can't move that direction!")
    elif usermove == "w":
        if hasattr(player['newplayer'].currentroom, 'w_to'):
            print("You moved west!")
            player['newplayer'].currentroom = player['newplayer'].currentroom.w_to
            print (player['newplayer'].currentroom.name)
            print(player['newplayer'].currentroom.description)
        else:
            print("You can't move that direction!")
    elif usermove == "take":
        print("The items are currently in this room are", player['newplayer'].currentroom.roomitems)
        request = input('What would you like to take?')
        if request in player['newplayer'].currentroom.roomitems:
            player['newplayer'].take_item(request)
            print("You took "+request)
            player['newplayer'].currentroom.roomitems.remove(request)
        else:
            print("That isn't in this room!")
    elif usermove == "drop":
        print("You're currently carrying ", player['newplayer'].items)
        request = input("What would you like to drop?")
        if request in player['newplayer'].items:
            player['newplayer'].drop_item(request)
            player['newplayer'].currentroom.roomitems.append(request)
            print("You dropped "+request)
        else:
            print("You aren't carrying that item!")
    elif usermove == "i":
        if player['newplayer'].items == []:
            print("You aren't carrying anything")
        else:
            print("You're currently carrying ", player['newplayer'].items)

