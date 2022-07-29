class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass


class Training:
    """Базовый класс тренировки."""
    
    M_IN_KM: int = 1000
    LEN_STEP: float = 0.65
    action: int
    duration: float
    weight: float

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""

        return self.action * self.LEN_STEP / self.M_IN_KM      
        

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        
        return self.distance / self.duration
        

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    """Тренировка: бег."""
    
    coeff_calorie_1: int = 18
    coeff_calorie_2: int = 20

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        super().__init__(action, duration, weight)

    def get_distance(self) -> float:
        return super().get_distance()

    def get_mean_speed(self) -> float:
        return super().get_mean_speed()        

    def get_spent_calories(self) -> float:
        return ((self.coeff_calorie_1 * self.mean_speed - self.coeff_calorie_2)
                                * self.weight / self.M_IN_KM * self.duration)

    def show_training_info(self) -> InfoMessage:
        return super().show_training_info()                            
        

class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    height: float
    coeff_calorie_1: float = 0.035
    coeff_calorie_2: float = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height
    
    def get_distance(self) -> float:
        return super().get_distance()

    def get_mean_speed(self) -> float:
        return super().get_mean_speed()    

    def get_spent_calories(self) -> float:
        return ((self.coeff_calorie_1 * self.weight + 
                               (self.mean_speed ** 2 / self.height) * 
                                self.coeff_calorie_2 * self.weight) *
                                self.duration)

    def show_training_info(self) -> InfoMessage:
        return super().show_training_info() 


class Swimming(Training):
    """Тренировка: плавание."""
    
    LEN_STEP: float = 1.38
    lenght_pool: int
    count_pool: int
    coeff_calorie_1: float = 1.1
    coeff_calorie_2: float = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 lenght_pool: int,
                 count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.lenght_pool = lenght_pool
        self.count_pool = count_pool

    def get_distance(self) -> float:
        return super().get_distance()

    def get_mean_speed(self) -> float:
        return (self.lenght_pool * self.count_pool /
                           self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        return ((self.mean_speed + self.coeff_calorie_1) *
                                self.coeff_calorie_2 * self.weight)  
                


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

