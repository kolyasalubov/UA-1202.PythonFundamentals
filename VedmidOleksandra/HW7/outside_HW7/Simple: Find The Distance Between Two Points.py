# Given two ordered pairs calculate the distance between them.
# Round to two decimal places. This should be easy to do in 0(1) timing.

def distance(x1, y1, x2, y2):
    distance_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2
    distance_o = round(distance_squared ** 0.5, 2)  # Округление до двух десятичных знаков
    return distance_o


