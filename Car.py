class Car :
    def __init__(self):
        self.speed = 0
        self.odometer = 0
        self.time = 0
    def say_state(self):
        print("I am going {} kph".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        return self.odometer/self.time

if __name__ == '__main__' :
    my_car = Car()
    print("I am a car")
    while True :
        action = input('What should I do ? [A]ccelerate, [B]rake, show [O]dometer or show average[S]peed').upper()
        if action not in 'ABOS' or len(action)!= 1:
            print('Wrong choice')
            continue

        if action == 'A':
            my_car.accelerate()

        elif action == 'B':
            my_car.brake()

        elif action == 'O':
            print("Car has driven {} kms".format(my_car.odometer))

        elif action == 'S':
            print("The average speed of the car is {} kph".format(my_car.average_speed()))
        my_car.step()
        my_car.say_state()

        aage = input('Wanna stop? type STOP').upper()
        if aage == 'STOP':
            break