from dataclasses import asdict, dataclass


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float
    INFO_MESSAGE: str = ('Тип тренировки: {training_type}; '
                         'Длительность: {duration:.3f} ч.; '
                         'Дистанция: {distance:.3f} км; '
                         'Ср. скорость: {speed:.3f} км/ч; '
                         'Потрачено ккал: {calories:.3f}.')

    def get_message(self) -> str:
        """Получить текст сообщения"""
        return self.INFO_MESSAGE.format(**asdict(self))


class Training:
    """Базовый класс тренировки."""

    M_IN_KM: int = 1000
    LEN_STEP: float = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action: int = action
        self.duration: float = duration
        self.weight: float = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""

        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError('define get_spent_calories in %s.'
                                  % (self.__class__.__name__))

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(type(self).__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""

    COEFF_GET_MEAN_SPEED_MULTIPLIER: int = 18
    COEFF_GET_MEAN_SPEED_SUBTRACT: int = 20
    MIN_IN_HOUR: int = 60

    def get_distance(self) -> float:
        return super().get_distance()

    def get_mean_speed(self) -> float:
        return super().get_mean_speed()

    def get_spent_calories(self) -> float:
        self.multiplier_and_subtract_get_mean_speed: float = (
            self.COEFF_GET_MEAN_SPEED_MULTIPLIER * self.get_mean_speed()
            - self.COEFF_GET_MEAN_SPEED_SUBTRACT)
        return (self.multiplier_and_subtract_get_mean_speed * self.weight
                / self.M_IN_KM
                * (self.duration * self.MIN_IN_HOUR))

    def show_training_info(self) -> InfoMessage:
        return super().show_training_info()


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    COEFF_WEIGHT_MULTIPLIER_1: float = 0.035
    COEFF_WEIGHT_MULTIPLIER_2: float = 0.029
    MIN_IN_HOUR: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float,) -> None:
        super().__init__(action, duration, weight)
        self.height: float = height

    def get_distance(self) -> float:
        return super().get_distance()

    def get_mean_speed(self) -> float:
        return super().get_mean_speed()

    def get_spent_calories(self) -> float:
        return ((self.COEFF_WEIGHT_MULTIPLIER_1 * self.weight
                + (self.get_mean_speed() ** 2 // self.height)
                * self.COEFF_WEIGHT_MULTIPLIER_2 * self.weight)
                * self.duration * self.MIN_IN_HOUR)

    def show_training_info(self) -> InfoMessage:
        return super().show_training_info()


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38
    COEFF_GET_MEAN_SPEED_ADDITION: float = 1.1
    COEFF_WEIGHT_MULTIPLIER: float = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int,) -> None:
        super().__init__(action, duration, weight)
        self.length_pool: int = length_pool
        self.count_pool: int = count_pool

    def get_distance(self) -> float:
        return super().get_distance()

    def get_mean_speed(self) -> float:
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed() + self.COEFF_GET_MEAN_SPEED_ADDITION)
                * self.COEFF_WEIGHT_MULTIPLIER * self.weight)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""

    training_type: dict[str, type[Training]] = {
        'RUN': Running,
        'WLK': SportsWalking,
        'SWM': Swimming
    }

    return training_type[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info: InfoMessage = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages: tuple[str, list[int]] = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training: Training = read_package(workout_type, data)
        main(training)
