from .musicians import Drummer, Guitarist, Vocalist, Bassist

class Band:
    name: str
    songs = []
    drummer: Drummer
    bassist: Bassist
    vocalist: Vocalist
    guitarist: Guitarist

    def __init__(self, name:str) -> None:
        self.name = name

    def play(self, song):
        return song

    def useDrummer(self, drummer: Drummer):
        self.drummer = drummer
        return self
        
    def useGuitarist(self, guitarist: Guitarist):
        self.guitarist = guitarist
        return self

    def useVocalist(self, vocalist: Vocalist):
        self.vocalist = vocalist
        return self
        
    def useBassist(self, bassist: Bassist):
        self.bassist = bassist
        return self
