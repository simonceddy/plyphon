class Musician:
    name: str

class Drummer(Musician):
    def hasRhythm(self) -> bool:
        return hasattr(self, 'rhythm')

class Guitarist(Musician):
    def hasRiffs(self) -> bool:
        return hasattr(self, 'riffs')

class Bassist(Musician):
    def hasRhythm(self) -> bool:
        return hasattr(self, 'rhythm')

    def tooManySoloes(self) -> bool:
        return hasattr(self, 'soloes')

class Vocalist(Musician):
    def isJLo(self) -> bool:
        return self.name == 'J Lo'