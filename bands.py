from band.Band import Band
from band.BattleOfTheBands import BattleOfTheBands
from band.musicians import Bassist, Drummer, Guitarist, Vocalist

class PoorOldLostWatson(Drummer):
    name: str = 'Poor Old Lost Watson'

class MetronomeTron(Drummer):
    rhythm: bool = True
    name: str = 'Metronome Tron'

class SludgeyJohn(Guitarist):
    name: str = 'Sludgey John'
    riffs = []

class SilverchairBill(Guitarist):
    name: str = 'Silverchair Bill'

class SlappyTheBassKangaroo(Bassist):
    name: str = 'Slappy the Bass Kangaroo'
    soloes: bool = True

class StanleyClarke(Bassist):
    name: str = 'Stanley Clarke'
    soloes: bool = True

    def tooManySoloes(self) -> bool:
        print('i have soloes but also i am stanley clarke')
        return False

class JLo(Vocalist):
    name: str = 'J Lo'

class JNo(Vocalist):
    name: str = 'Not J Lo'

freshBand = Band('Diggers')

freshBand.useDrummer(PoorOldLostWatson()).useBassist(SlappyTheBassKangaroo()).useGuitarist(SilverchairBill()).useVocalist(JNo())

frostenNightMill = Band('Frosten Night Mill')

frostenNightMill.useDrummer(MetronomeTron()).useBassist(StanleyClarke()).useGuitarist(SludgeyJohn()).useVocalist(JLo())

BattleOfTheBands([freshBand, frostenNightMill]).battle()