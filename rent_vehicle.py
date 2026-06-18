from abc import ABC,abstractmethod

class VehicleOnRent(ABC):
    
    @abstractmethod
    def rent_cost(self,days):
        pass

class Bike(VehicleOnRent):
    def rent_cost(self, days):
        return days*500
    
class Car(VehicleOnRent):
    def rent_cost(self, days):
        return days*1000
    
class Truck(VehicleOnRent):
    def rent_cost(self, days):
        return days*2000

vehicle = Car()
print(vehicle.rent_cost(3))