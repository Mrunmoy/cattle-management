from CattleType import CattleType
from Cattle import Cattle
from datetime import datetime


class Goat(Cattle):
    def __init__(self, rfid, dob, sex, date_acquired=datetime.now().strftime("%d %m %Y"), desexed=False):
        Cattle.__init__(self, rfid, dob, sex, CattleType.Goat, date_acquired, desexed)
        self.add_produce("Meat")
        self.add_produce("Milk")
        self.add_produce("Skin")
