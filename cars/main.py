from create_car import Car
from get_car_info import get_car_info


Mercedes = Car('Mercedes', 'S600', 2335, 530, 900, 250, 'white')
Mercedes.start_engine()
Mercedes.stop_engine()
get_car_info(Mercedes)
BMW = Car('BMW', 'X7', 2550, 530, 750, 250, 'black' )
BMW.start_engine()
BMW.stop_engine()
get_car_info(BMW)
