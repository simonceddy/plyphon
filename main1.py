import sys
import pprint

# Array of made up fictional data of which none is real
leaders = [['Kim Jong Uno', 'Jongs'], ['Voldemorte Putin', 'Putes'], ['Kerry Pacman', 'Shelfers'], ['Adam Bandt', 'Greens']]

class LetterWriter:
    sender = ''
    party = ''
    toName = ''
    toParty = ''

    def __init__(self, sender, party):
        self.sender = sender
        self.party = party

    def writeTo(self, name, party):
        self.toName = name
        self.toParty = party
        return self

    def readAloud(self):
        print('Most darest %s of Mighty %s\n' % (self.toName, self.toParty))
        print('With one face, they presented to the world, an appearance of respectability, but with the other, they said "ooh, goodie, let\'s pump ourselves full of magic monkey juice and take a trip to space land, because we\'d rather do that, than spend another minute with that poor sod"\n')
        print('Most regards,')
        print('%s, Supreme Leader of the %s\n' % (self.sender, self.party))

test = LetterWriter('Spoole', 'Cry Fountain Emotionauts of Sooking')

# for x in leaders:
#     test.writeTo(x[0], x[1]).readAloud()

pprint.pprint(sys.argv)