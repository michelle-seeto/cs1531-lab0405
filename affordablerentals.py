from abc import ABC, abstractmethod

vehicles = []

class Customer:
    def __init__(self, name = None, age = None, licence_number = None, email_address = None):
        self._name = name
        self._age = age
        self._licence_number = licence_number
        self._email_address = email_address

    def reserve_car(self, selected_car):
        print("Reserving: " + str(selected_car.__str__()))
        self.set_name(input("Name: "))
        self.set_age(input("Age: "))
        self.set_licence_number(input("Licence Number: "))
        self.set_email_address(input("Email Address: "))
        start_date = input("Start date: ")
        rental_period = int(input("How many days would you like to rent the car? "))
        pick_up_location = input("Pick up location: ")
        drop_off_location = input("Drop off location: ")
        price = selected_car.calculate_price(rental_period)
        reservation = RentalReservation(self, selected_car, start_date, rental_period, False, pick_up_location, drop_off_location, price)
        reservation.send_confirmation_email()

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_licence_number(self):
        return self._licence_number

    def get_email_address(self):
        return self._email_address

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_licence_number(self, licence_number):
        self._licence_number = licence_number

    def set_email_address(self, email_address):
        self._email_address = email_address

class RentalReservation:
    def __init__(self, customer, car, start_date, rental_period, insurance_cover, pick_up_location, drop_off_location, total_price):
        self._customer = customer
        self._car = car
        self._start_date = start_date
        self._rental_period = rental_period
        self._insurance_cover = insurance_cover
        self._pick_up_location = pick_up_location
        self._drop_off_location = drop_off_location
        self._total_price = total_price

    def send_confirmation_email(self):
        print("~~~ Confirmation email to " + self._customer.get_email_address() + " ~~~")
        print(self._customer.get_name() + " (" + self._customer.get_age() + " years old)")
        print("Licence number: " + self._customer.get_licence_number())
        print("Car: " + self._car.__str__() + " (Registration no.: " + self._car.get_registration() + ")")
        print("Rental period of " + str(self._rental_period) + " days commences " + self._start_date)
        print("Additional insurance? " + str(self._insurance_cover))
        print("Pick up location: " + self._pick_up_location)
        print("Drop off location: " + self._drop_off_location)
        print("Total price: $" + "{:.2f}".format(self._car.calculate_price(self._rental_period)))

    def get_customer(self):
        return self._customer

    def get_car(self):
        return self._car

    def get_start_date(self):
        return self._start_date

    def get_rental_period(self):
        return self._rental_period

    def get_total_price(self):
        return self._total_price

    def get_pick_up_location(self):
        return self._pick_up_location

    def get_drop_off_location(self):
        return self._drop_off_location

    def has_insurance_cover(self):
        return self._insurance_cover

    def set_customer(self, customer):
        self._customer = customer

    def set_car(self, car):
        self._car = car

    def set_start_date(self, start_date):
        self._start_date = start_date

    def set_rental_period(self, rental_period):
        self._rental_period = rental_period

    def set_total_price(self, total_price):
        self._total_price = total_price

    def set_insurance_cover(self, insurance_cover):
        self._insurance_cover = insurance_cover

    def set_pick_up_location(self, pick_up_location):
        self._pick_up_location = pick_up_location

    def set_drop_off_location(self, drop_off_location):
        self._drop_off_location = drop_off_location

class RentalCar(ABC):
    def __init__(self, model, make, year, registration, daily_rate):
        self._model = model
        self._make = make
        self._year = year
        self._registration = registration
        self._daily_rate = daily_rate

    def calculate_price(self, rental_period):
        return self._daily_rate * rental_period

    def __str__(self):
        return self._model + " " + self._make + " " + str(self._year)

    def get_model(self):
        return self._model

    def get_make(self):
        return self._make

    def get_year(self):
        return self._year

    def get_registration(self):
        return self._registration

    def get_daily_rate(self):
        return self._daily_rate

    def set_model(self, model):
        self._model = model

    def set_make(self, make):
        self._make = make

    def set_year(self, year):
        self._year = year

    def set_registration(self, registration):
        self._registration = registration

    def set_daily_rate(self, daily_rate):
        self._daily_rate = daily_rate

class SmallCar(RentalCar):
    def __init__(self, model, make, year, registration, daily_rate):
        RentalCar.__init__(self, model, make, year, registration, daily_rate)

class MediumCar(RentalCar):
    def __init__(self, model, make, year, registration, daily_rate):
        RentalCar.__init__(self, model, make, year, registration, daily_rate)

class LargeCar(RentalCar):
    def __init__(self, model, make, year, registration, daily_rate):
        RentalCar.__init__(self, model, make, year, registration, daily_rate)

    def calculate_price(self, rental_period):
        super()
        price = self._daily_rate * rental_period
        if rental_period > 7:
            price *= 0.95
        return price

class PremiumCar(RentalCar):
    def __init__(self, model, make, year, registration, daily_rate):
        RentalCar.__init__(self, model, make, year, registration, daily_rate)

    def calculate_price(self, rental_period):
        super()
        price = self._daily_rate * rental_period * 1.15
        if rental_period > 7:
            price *= 0.95
        return price

class StaffAdmin:
    def __init__(self, name, username):
        self._name = name
        self._username = username

    def add_new_car(self, new_car):
        vehicles.append(new_car)

    def get_name(self):
        return self._name

    def get_username(self):
        return self._username

    def set_name(self, name):
        self._name = name

    def set_username(self, username):
        self._username = username

class StaffManager(StaffAdmin):
    def __init__(self, name, username):
        self._name = name
        self._username = username

staff1 = StaffAdmin("Ngarie MacDonald", "nmd")
customer1 = Customer()
customer2 = Customer()
customer3 = Customer()
car1 = SmallCar("Honda", "Bug 2.0", 2018, "REGO2468", 100)
car2 = LargeCar("Toyota", "Tree", 2006, "REGO1357", 200)
car3 = PremiumCar("Mercedes", "Panther", 2020, "REGO1234", 200)
staff1.add_new_car(car1)
staff1.add_new_car(car2)
staff1.add_new_car(car3)
customer1.reserve_car(car1)
#customer2.reserve_car(car2)
#customer3.reserve_car(car3)
