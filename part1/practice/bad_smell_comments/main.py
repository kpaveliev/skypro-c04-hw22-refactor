# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:

    CRAWL_SPEED_COEFFICIENT = 0.5
    FLY_SPEED_COEFFICIENT = 1.5

    def __init__(self, field, x: int, y: int, state: str, speed: int):
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
        self._speed = speed


    def move(self, direction):
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


    def _calculate_speed(self):
        """Calculate speed based on movement type"""
        if self._movement_type == "fly":
            return self._speed * self.FLY_SPEED_COEFFICIENT
        elif self._movement_type == "crawl":
            return self._speed * self.CRAWL_SPEED_COEFFICIENT
