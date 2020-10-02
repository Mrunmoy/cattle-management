from CattleType import CattleType
from Cattle import Cattle
from datetime import datetime


class Sheep(Cattle):
    def __init__(self, rfid, dob, sex, date_acquired=datetime.now().strftime("%d %m %Y"), desexed=False):
        Cattle.__init__(self, rfid, dob, sex, CattleType.Sheep, date_acquired, desexed)
        self.add_produce("Meat")
        self.add_produce("Wool")
