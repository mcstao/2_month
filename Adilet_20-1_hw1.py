class Car:
    def __init__(self,title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color
    def start_engine(self):
        print(f"Engine on {self.title} {self.model} started")
    def stop_engine(self):
        print(f"Engine on {self.title} {self.model} off")
    def info(self):
        print( f' All info :{self.title} {self.model} {self.weight} {self.hp} {self.nm} {self.max_speed} {self.color}')
Mercedes = Car('Mercedes', 'S600', 2335, 530, 900, 250, 'white')
BMW = Car('BMW', 'X7', 2550, 530, 750, 250, 'black' )
Mercedes.start_engine()
Mercedes.stop_engine()
Mercedes.info()
BMW.start_engine()
BMW.stop_engine()
BMW.info()
