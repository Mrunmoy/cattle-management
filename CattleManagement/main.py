# This is a sample Python script.
from Goat import Goat
from Sex import Sex
from Sheep import Sheep
from datetime import datetime, date
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lamb = Sheep(123, "12 03 2019", Sex.Male)
    print(lamb.rfid())
    print(lamb.type())
    print(lamb.dob())
    lamb.set_date_of_death(datetime.now().strftime("%d %m %Y"))
    print(lamb.age())
    print(lamb.survival_days())
    produce = lamb.produce()
    for p in produce:
        print(p)

    print("\n----------------------------\n")
    goat1 = Goat(234, "6 2 2017", Sex.Female)
    goat1.set_genetics("Boer")

    goat2 = Goat(374, "1 8 2018", Sex.Male)
    goat2.set_genetics("Black Bengal")

    goat3 = Goat(567, "3 1 2020", Sex.Male)
    print(goat3.rfid())
    print(goat3.type())
    print(goat3.dob())
    print(goat3.age())
    goat3.set_mother(goat1)
    goat3.set_father(goat2)
    genetics = goat3.genetics()
    for g in genetics:
        print(g)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
