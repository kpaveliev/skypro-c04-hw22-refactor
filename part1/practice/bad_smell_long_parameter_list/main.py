# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:

    CRAWL_SPEED_COEFFICIENT = 0.5
    FLY_SPEED_COEFFICIENT = 1.5

    def __init__(self, field, x: int, y: int, movement_type: str):
        """
        :param field: playing field
        :param x: coordinate
        :param Y: coordinate
        :param movement_type: could be "crawl" of "fly"
        """
        self._field = field
        self._x = x
        self._y = y
        self._movement_type = movement_type

    def _calculate_speed(self, speed):
        """Calculate speed based on movement type"""
        if self._movement_type == "fly":
            return speed * self.FLY_SPEED_COEFFICIENT
        elif self._movement_type == "crawl":
            return speed * self.CRAWL_SPEED_COEFFICIENT_SPEED_COEFFICIENT

    def move(self, direction, speed):
        """Move unit"""
        speed = self._calculate_speed(speed)

        if direction == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)

