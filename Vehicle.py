class Vehicle(object):
    def __init__(self, name, context):
        self.name = name
        self.context = context

class Car(Vehicle):

    def __init__(self, name):
        Vehicle.__init__(self, name, "Land")
        self.speed = 0.0
        self._year = 2001
        self.make = "genric"
        self.model = "thing"
        self.speed = 60.0
        self.position = 0
        self.road = None

    def setYear(self,value):
        self._year = value

    def getYear(self):
        return self._year

    def moveCar(self, delta):
        raise NotImplementedError

    def driveForward(self, distance):
        """Moves car forward raises error if car has
        collided with another. """
        raise NotImplementedError

    def driveBackwards(self, distance):
        """Moves car backward raises error if car has
        collided with another. """
        raise NotImplementedError

    year = property(getYear,setYear,"What it does")

class Road(object):

    def __init__(self, name, speedLimit):
        self.name = name
        self.speedLimit = speedLimit
        self.cars = []
        #Miles
        self.length = 10

    def setSpeedLimit(self, speed):
        self.speedLimit = speed

    def getSpeedLimit(self):
        return self.speedLimit

    def addCar(self, car):
        car.road = self
        self.cars.append(car)

    def clockCar(self, car):
        if car.speed > self.speedLimit:
            print "%s is speeding!" % car.name

    def speedingCars(self):
        speedingCars = []
        for car in self.cars:
            if car.speed > self.speedLimit:
                speedingCars.append(car)
        return speedingCars

if __name__ == '__main__':
    car = Car("Fast guy")
    car.speed = 80.0
    car2 = Car("Blue car")
    car2.speed = 60
    road = Road("Lonely road", 75)
    print car.road == None
    road.addCar(car)
    print car.road == road
    road.addCar(car2)
    print road.speedingCars()

