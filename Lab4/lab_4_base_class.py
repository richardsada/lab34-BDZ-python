class Product:
    @classmethod
    def __check_value(self, x): # проверка чтобы был тип инт или флоат
        return (type(x) == int or type(x) == float) and x > 0

    def __init__(self, price, width, height, depth, name):
        
        if self.__check_value(price) and self.__check_value(width) and self.__check_value(height) and self.__check_value(depth):
            self.price = price
            self.width = width
            self.height = height
            self.depth = depth
            self.name = name
        else:
            raise ValueError("Недопустимое значение параметров")

    def discount(self, sale):
        if self.__check_value(sale):
            sale = self.price - (self.price * sale / 100)
            return round(sale, 2)
        else:
            raise ValueError("Недопустимое значение скидки")
# ПЕРЕГРУЗКА
    def __str__(self): # Вывод
        return f"({self.name }, {self.price}, {self.width}, {self.height}, {self.depth})"



