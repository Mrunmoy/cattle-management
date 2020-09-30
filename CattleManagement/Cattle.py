import CattleType
from datetime import datetime, date

DEFAULT_RFID = 111111111111

class Cattle:
    def __init__(self, rfid, dob, cattleType):
        self._rfid = rfid
        self._dob = datetime.strptime(dob, "%d %m %Y")
        self._type = cattleType

    def rfid(self):
        return self._rfid

    def type(self):
        return self._type

    def dob(self):
        return self._dob

    def age(self):
        today = date.today()
        age = today.year - self._dob.year - ((today.month, today.day) < (self._dob.month, self._dob.day))
        return age

    def setRfid(self, rfid):
        self._rfid = rfid