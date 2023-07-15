"""
Переписать код SpeedCalculation в соответствии с Open-Closed Principle:

public class SpeedCalculation {
    public double calculateAllowedSpeed(Vehicle vehicle) {
        if (vehicle.getType().equalsIgnoreCase("Car")) {
            return vehicle.getMaxSpeed() * 0.8;
        } else if (vehicle.getType().equalsIgnoreCase("Bus")) {
            return vehicle.getMaxSpeed() * 0.6;
        }
        return 0.0;
    }
}

public class Vehicle {
    int maxSpeed;
    String type;
    public Vehicle(int maxSpeed, String type) {
        this.maxSpeed = maxSpeed;
        this.type = type;
    }
    public int getMaxSpeed() {
        return this.maxSpeed;
    }
    public String getType() {
        return this.type;
    }
}

Подсказка: создайте два дополнительных класса Car и Bus(наследников Vehicle),
напишите метод calculateAllowedSpeed(). Использование этого метода позволит
сделать класс SpeedCalculation соответствующим OCP
"""
from abc import abstractmethod, ABC


# Реализовал Vehicle как класс, с абстрактным методом calculate_allowed_speed
# Наследники имеют собственные реализации данного метода. Сам класс Speed
# Calculation при этом менять, при появлении нового наследника Vehicle, будет
# не нужно и он не зависит от типа класса нового наследника (другими словами,
# без if..else обходится)
class Vehicle(ABC):
    def __init__(self, max_speed: int, vehicle_type: str):
        self.max_speed = max_speed
        self.vehicle_type = vehicle_type

    def get_max_speed(self) -> int:
        return self.max_speed

    def get_type(self) -> str:
        return self.vehicle_type

    @abstractmethod
    def calculate_allowed_speed(self) -> float: pass


class Car(Vehicle):
    def __init__(self, max_speed: int):
        super().__init__(max_speed=max_speed,
                         vehicle_type=self.__class__.__name__.lower())

    def calculate_allowed_speed(self):
        return self.max_speed * 0.8


class Bus(Vehicle):
    def __init__(self, max_speed: int):
        super().__init__(max_speed=max_speed,
                         vehicle_type=self.__class__.__name__.lower())

    def calculate_allowed_speed(self):
        return self.max_speed * 0.6


class SpeedCalculation:
    @staticmethod
    def get_allowed_speed(vehicle: Vehicle) -> float:
        return vehicle.calculate_allowed_speed()


tran_1 = Car(max_speed=200)
tran_2 = Bus(max_speed=120)

print(SpeedCalculation.get_allowed_speed(tran_1))
print(SpeedCalculation.get_allowed_speed(tran_2))

