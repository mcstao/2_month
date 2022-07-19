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