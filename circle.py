import math

def area(r):
    '''Принимает число r, возвращает площадь окружности с таким радиусом'''
    return math.pi * r * r

print(area(4))
'''Вывод: 50.26548245743669'''

def perimeter(r):
    '''Принимает число r, возвращает периметр окружности с таким радиусом'''
    return 2 * math.pi * r

print(perimeter(3))
'''Вывод: 18.84955592153876'''
