from .Band import Band

class BattleOfTheBands:
    bands: list

    def __init__(self, bands: list) -> None:
        self.bands = bands

    def judgeBand(self, band: Band) -> int:
        rating: int = 0

        if band.drummer.hasRhythm() is False:
            print('The drummer of %s, ye who benamed %s, hath no time beats'%(band.name, band.drummer.name))
            rating = rating - 1
        else:
            print('Nice time beats, noble %s of %s'%(band.drummer.name, band.name))
            rating = rating + 1
        if band.bassist.tooManySoloes():
            print('%s of %s assaults the bass like a pub biffo'%(band.bassist.name, band.name))
            rating = rating - 1
        else:
            print('We accept you %s of %s'%(band.bassist.name, band.name))
            rating = rating + 1
        if band.guitarist.hasRiffs() is False:
            print('%s guitarist %s loves no riff'%(band.name, band.guitarist.name))
            rating = rating - 1
        else:
            print('Big old %s is shredding the riffs of %s'%(band.guitarist.name, band.name))
            rating = rating + 1
        if band.vocalist.isJLo() is False:
            print('%s vocalist %s is not J Lo'%(band.name, band.vocalist.name))
            rating = rating - 1
        else:
            print('%s vocalist %s is J Lo'%(band.name, band.vocalist.name))
            rating = rating + 1
        return rating

    def passJudgement(self, band: Band):
        judgement = self.judgeBand(band)
        print('%s has been judged %i out of 4'%(band.name, judgement)) 

        return judgement

    def battle(self) -> None:
        judgements: list = []
        print('Starting the Battle of the Bands featuring:\n')
        for band in self.bands:
            print('-----**** %s ****-----\n'%(band.name))
            judgements.append(lambda: self.passJudgement(band))
        
        for judgement in judgements:
            judgement()
            print('\n')

