# We can use the Dungeon class from a different file by importing it like so
from Dungeon import Dungeon
# Note pls: This works like 'from FilenameWithout.py import NameOfClass'

# Geeze the Dungeon.py file if ya aint been yet for a gaze at classes

# Note pls: we can also just write "import Dungeon" which works like 
# 'import FilenameWithout.py' but then we'd use it by typin up:
# Dungeon.Dungeon('My Tough Den Of Masculine Manliness')
# 
# And I think that looks gross cos I just wanna use Dungeon('The Plus Lair'),
# hence the from bit

# Here we make a new Dungeon object with a handy name for remembrun
# We're assigning the new Dungeon to a variable called 'cave'
cave = Dungeon('Terrible Cavern of Horrific Monstrous Atrocities')

# Now we've done as the romans and made a cave we can not just enter it...
cave.enter()

# ... but also leave too
cave.leave()