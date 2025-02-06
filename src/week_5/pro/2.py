from abc import ABC, abstractmethod


class User:
    def __init__(self, user_id: int, name: str, balance: int):
        self.user_id = user_id
        self.name = name
        self.balance = balance
        self.active_rent = False
        self.rental_history = []
        self.current_duration_minutes = 0
        self.current_distance_km = 0
        self.current_car: Car = None

    def top_up_balance(self, amount):
        self.balance += amount

    def rent_car(self, car, duration_minutes, distance_km):
        if self.balance > 0:
            if self.active_rent == False:
                if car.status == 'available':

                    if isinstance(car, StandardCar):
                        available_distance = car.current_fuel - car.fuel_consumption * (distance_km / 100)
                    else:
                        available_distance = car.current_charge - car.energy_consumption * (distance_km / 100)

                    if available_distance >= 0:
                        rent_amount = duration_minutes * car.price_per_minute
                        self.balance -= rent_amount
                        self.active_rent = True
                        self.current_car = car
                        self.current_distance_km = distance_km
                        self.current_duration_minutes = duration_minutes

                        car.status = 'rented'

                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def end_rental(self):

        if isinstance(self.current_car, StandardCar):
            self.current_car.current_fuel -= self.current_car.fuel_consumption * (self.current_distance_km / 100)
        elif isinstance(self.current_car, ElectricCar):
            self.current_car.current_charge -= self.current_car.energy_consumption * (self.current_distance_km / 100)
        self.current_car.status = 'available'

        self.active_rent = False
        history_dict = {"car": self.current_car.model, "duration": self.current_duration_minutes,
                        "distance": self.current_distance_km}
        self.rental_history.append(history_dict)
        self.current_duration_minutes = 0
        self.current_distance_km = 0
        self.current_car = None


class Car(ABC):
    def __init__(self, model, registration_number, price_per_minute):
        self.model = model
        self.registration_number = registration_number
        self.price_per_minute = price_per_minute
        self.status = 'available'

    @abstractmethod
    def refill(self):
        pass


class StandardCar(Car):
    def __init__(self,
                 model,
                 registration_number,
                 price_per_minute,
                 fuel_capacity,
                 fuel_consumption,
                 current_fuel
                 ):
        super().__init__(model, registration_number, price_per_minute)
        self.fuel_capacity = fuel_capacity
        self.fuel_consumption = fuel_consumption
        self.current_fuel = current_fuel

    def refill(self):
        self.current_fuel = self.fuel_capacity


class ElectricCar(Car):
    def __init__(self,
                 model,
                 registration_number,
                 price_per_minute,
                 battery_capacity,
                 energy_consumption,
                 current_charge
                 ):
        super().__init__(model, registration_number, price_per_minute)
        self.battery_capacity = battery_capacity
        self.energy_consumption = energy_consumption
        self.current_charge = current_charge

    def refill(self):
        self.current_charge = self.battery_capacity


class Car:
    def __init__(self, model, registration_number, price_per_minute):
        self.model = model
        self.registration_number = registration_number
        self.price_per_minute = price_per_minute
        self.status = 'available'

    @abstractmethod
    def refill(self):
        pass


class StandardCar(Car):
    def __init__(self,
                 model,
                 registration_number,
                 price_per_minute,
                 fuel_capacity,
                 fuel_consumption,
                 current_fuel
                 ):
        super().__init__(model, registration_number, price_per_minute)
        self.fuel_capacity = fuel_capacity
        self.fuel_consumption = fuel_consumption
        self.current_fuel = current_fuel

    def refill(self):
        self.current_fuel = self.fuel_capacity


class ElectricCar(Car):
    def __init__(self,
                 model,
                 registration_number,
                 price_per_minute,
                 battery_capacity,
                 energy_consumption,
                 current_charge
                 ):
        super().__init__(model, registration_number, price_per_minute)
        self.battery_capacity = battery_capacity
        self.energy_consumption = energy_consumption
        self.current_charge = current_charge

    def refill(self):
        self.current_charge = self.battery_capacity


user = User(user_id=1, name="Борис", balance=1000)

car = StandardCar(model="Toyota Camry", registration_number="A123BB", price_per_minute=10, fuel_capacity=60,
                  fuel_consumption=8, current_fuel=60)

print(user.balance)  # 1000
print(car.current_fuel)  # 60

print(user.rent_car(car, duration_minutes=30, distance_km=20))

user.end_rental()

print(user.balance)  # 700
print(car.current_fuel)  # 58.4

user.top_up_balance(500)
car.refill()

print(user.balance)  # 1200
print(car.current_fuel)  # 60
