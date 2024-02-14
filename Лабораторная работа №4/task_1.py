class Car:
    """Базовый класс автомобиля."""
    def __init__(self, speed: float, number: str, model: str):
        """
        Конструктор класса Car.

        Args:
            speed: Максимальная скорость автомобиля.
            number: Номер автомобиля.
            model: Модель автомобиля.
        """
        self.__speed = speed
        self.__number = number
        self.__model = model

    @property
    def speed(self) -> float:
        """Максимальная скорость автомобиля."""
        return self.__speed

    @property
    def number(self) -> str:
        """Номер автомобиля."""
        return self.__number

    @property
    def model(self) -> str:
        """Модель автомобиля."""
        return self.__model

    def __str__(self) -> str:
        """Возвращает строковое представление экземпляра класса Car."""
        return f"Автомобиль модели {self.model}, максимальная скорость {self.speed}, номер {self.number}."

    def __repr__(self) -> str:
        """Возвращает строковое представление экземпляра класса Car для отладочных целей."""
        return f"{self.__class__.__name__}(speed={self.speed!r}, model={self.model!r}, number={self.number!r})"


class PassengerCar(Car):
    """Класс легкового автомобиля."""
    def __init__(self, speed: float, number: str, model: str, seats: int):
        """
        Конструктор класса PassengerCar.

        Args:
            speed: Максимальная скорость автомобиля.
            number: Номер автомобиля.
            model: Модель автомобиля.
            seats: Количество пассажирских мест.
        """
        super().__init__(speed, number, model)
        self.__seats = seats

    @property
    def seats(self) -> int:
        """Количество пассажирских мест."""
        return self.__seats

    @seats.setter
    def seats(self, seats: int):
        """
        Установить количество пассажирских мест.

        Args:
            seats: Количество пассажирских мест.
        """
        if isinstance(seats, int) and seats > 0:
            self.__seats = seats

    def drive(self) -> None:
        """Метод, описывающий движение легкового автомобиля."""
        print("Легковой автомобиль начал движение.")

    def __str__(self) -> str:
        """Возвращает строковое представление экземпляра класса PassengerCar."""
        return super().__str__() + f" Вместимость: {self.seats} пассажиров."


class TruckCar(Car):
    """Класс грузового автомобиля."""
    def __init__(self, speed: float, number: str, model: str, payload: float):
        """
        Конструктор класса TruckCar.

        Args:
            speed: Максимальная скорость автомобиля.
            number: Номер автомобиля.
            model: Модель автомобиля.
            payload: Грузоподъемность автомобиля.
        """
        super().__init__(speed, number, model)
        self.__payload = payload

    @property
    def payload(self) -> float:
        """Грузоподъемность автомобиля."""
        return self.__payload

    @payload.setter
    def payload(self, payload: float):
        """
        Установить грузоподъемность автомобиля.

        Args:
            payload: Грузоподъемность автомобиля.
        """
        if isinstance(payload, float) and payload > 0:
            self.__payload = payload

    def load(self) -> None:
        """Метод, описывающий погрузку грузового автомобиля."""
        print("Грузовой автомобиль начал погрузку.")

    def __str__(self) -> str:
        """Возвращает строковое представление экземпляра класса TruckCar."""
        return super().__str__() + f" Грузоподъемность: {self.payload} кг."
