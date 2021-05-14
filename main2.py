class Person:
    name = ''
    party = ''

    def __init__(self, name, party) -> None:
        self.name = name
        self.party = party

class Letter:
    sender: Person
    receiver: Person
    body: str
    postScript: str

    def __init__(self) -> None:
        pass

    def regards(self, sender: Person):
        self.sender = sender
        return self

    def dear(self, receiver: Person):
        self.receiver = receiver
        return self

    def contents(self, contents: str):
        self.body = contents
        return self

    def ps(self, contents: str):
        self.postScript = contents
        return self

    def toString(self) -> str:
        dear = 'Dear %s of the mighty %s,'%(self.receiver.name, self.receiver.party)
        regards = 'Regards sincerely, %s of great %s'%(self.sender.name, self.sender.party)
        letter =  '%s\n\n%s\n%s\n\nPS: %s\n'%(dear, self.body, regards, self.postScript)

        return letter

    def __str__(self) -> str:
        return self.toString()

leaders = [
    ['Kim Jong Uno', 'Jongs'],
    ['Voldemorte Putin', 'Putes'],
    ['Kerry Pacman', 'Shelfers'],
    ['Adam Bandt', 'Greens']
]

for leader in leaders:
    print(
        Letter()
            .dear(Person(leader[0], leader[1]))
            .contents('It\'s me, Nicky Winar')
            .regards(Person('Mister', 'Doctor'))
            .ps('It\'s me, Nicky Winar')
    )