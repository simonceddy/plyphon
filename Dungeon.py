# Dungeon class defines a cool dungeon object for you to enter and then
# also leave
# 
# A class is a container for bitsa code like functions and variables.
# When its bein run it creates an "object" inside your computer RAM.
# The object can be used by ya program to do stuff.
# 
# Note pls: enjoy
class Dungeon:
    # The Dungeon class has a property called 'name' which has to be a string
    # as defined by the : str bit
    # This property is where the name of the dungeon is stored
    # 
    # Note pls: a property is just a variable inside a class, nothing more
    # complication
    name: str

    # This __init__ deal is a constructor function. Every time we make a new
    # dungerydoo with Dungeon(etc) this function gets run
    # The arguments for the constructor are self and name.
    # self is internal and we only include it because the function is inside a
    # class.
    # We won't ever chuck it in ourselves. We only worry about name.
    # The name is the dungeon's fresh and hip name.
    # 
    # In order to make a dungeon we get this here and go like this here:
    # coolDungeon = Dungeon('Cool Name')
    def __init__(self, name) -> None:
        self.name = name

    # This is the method for entering the scary dungeon
    # 
    # Note pls: A method is just a function inside a class, nothing more
    # complication
    # 
    # Again this has a 'self' argument cos it inside class AND we are using
    # the class inside the function
    # self is always internal so we just run coolDungeon.enter()
    def enter(self):
        print('you have entered the %s'%(self.name))

    # This is the function for leaving the dungeon and rejoining society
    # Same deal with self. We just run coolDungeon.leave()
    def leave(self):
        print('you have left the %s'%(self.name))