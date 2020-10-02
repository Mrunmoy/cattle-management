from datetime import datetime, date

DEFAULT_RFID = 111111111111


class Cattle:
    def __init__(self, rfid, dob, sex, cattle_type, date_purchased, desexed=False):
        self._rfid = rfid
        self._dob = datetime.strptime(dob, "%d %m %Y")
        self._sex = sex
        self._type = cattle_type
        self._date_purchased = datetime.strptime(date_purchased, "%d %m %Y")
        self._desexed = desexed
        self._date_sold = 0
        self._cost_price = 0
        self._sold_price = 0
        self._food_units_per_day = 0
        self._food_cost_per_unit = 0
        self._vaccination_date = None
        self._shed_id = None
        self._date_of_death = None
        self._mother = None
        self._father = None
        self._children = []
        self._produce = []
        self._medicine = []
        self._disease = []
        self._vet_visit_date = []
        self._genetics = []

    def rfid(self):
        return self._rfid

    def set_rfid(self, rfid):
        self._rfid = rfid

    def genetics(self):
        return self._genetics

    def set_genetics(self, genetics):
        self._genetics.append(genetics)

    def add_medicine(self, med):
        self._medicine.append(med)

    def medicine(self):
        return self._medicine

    def add_disease(self, dis):
        self._disease.append(dis)

    def diseases(self):
        return self._disease

    def set_vet_visit(self, dt):
        self._vet_visit_date.append(dt)

    def vet_visit_dates(self):
        return self._vet_visit_date

    def sex(self):
        return self._sex

    def type(self):
        return self._type

    def set_mother(self, mom):
        self._mother = mom
        moms_genetics = mom.genetics()
        for ea in moms_genetics:
            self._genetics.append(ea)

    def set_father(self, dad):
        self._father = dad
        dads_genetics = dad.genetics()
        for ea in dads_genetics:
            self._genetics.append(ea)

    def add_child(self, child):
        self._children.append(child)

    def produce(self):
        return self._produce

    def add_produce(self, produce_type):
        self._produce.append(produce_type)

    def remove_produce(self, produce_type):
        self._produce.remove(produce_type)

    def food_consumed_per_day(self):
        return self._food_units_per_day

    def set_food_consumed_per_day(self, units_per_day):
        self._food_units_per_day = units_per_day

    def food_cost_per_day(self):
        return self._food_units_per_day * self._food_cost_per_unit

    def set_food_cost(self, cost_per_unit):
        self._food_cost_per_unit = cost_per_unit

    def dob(self):
        return self._dob

    def age(self):
        today = date.today()
        age = today.year - self._dob.year - ((today.month, today.day) < (self._dob.month, self._dob.day))
        return age

    def set_date_of_death(self, dt):
        self._date_of_death = datetime.strptime(dt, "%d %m %Y")

    def survival_days(self):
        num_days = self._date_of_death - self._dob
        return num_days.days

    def desexed(self):
        return self._desexed

    def set_desexed(self, status):
        self._desexed = status

    def shed_id(self):
        return self._shed_id

    def set_shed(self, shed):
        self._shed_id = shed

    def purchased_date(self):
        return self._date_purchased

    def purchase_price(self):
        return self._cost_price

    def set_purchase_price(self, price):
        self._cost_price = price

    def sold_date(self):
        return self._date_sold

    def set_sold_date(self, dt):
        self._date_sold = dt

    def sold_price(self):
        return self._sold_price

    def set_sold_price(self, price):
        self._sold_price = price

    def vaccination_date(self):
        return self._vaccination_date

    def set_vaccination_date(self, dt):
        self._vaccination_date = datetime.strptime(dt, "%d %m %Y")