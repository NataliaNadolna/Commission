class Car():
    def __init__(self, make, model, capacity, year, mileage, gearbox):
        self.make = make
        self.model = model
        self.capacity = capacity
        self.year = year
        self.mileage = mileage
        self.gearbox = gearbox

    def __str__(self):
        return f"{self.make} {self.model} {self.capacity} {self.year} {self.mileage} {self.gearbox}"

class CarList(list):
    def __init__(self):
        super().__init__()

class Commission:
    def __init__(self):
        self.current_cars = CarList()
        self.sold_cars = CarList()
        self.bought_cars = CarList()

    def load_data(self):
        self.read_data(self.current_cars, path="_Commission/files/current.txt")
        self.read_data(self.sold_cars, path="_Commission/files/sold.txt")
        self.read_data(self.bought_cars, path="_Commission/files/bought.txt")

    def read_data(self, car_list: CarList, path: str):
        with open(path) as file:
            list = file.read().splitlines() 

        for index in range(0, len(list), 6): 
            make = list[index]
            model = list[index+1]
            capacity = list[index+2]
            year = list[index+3]
            mileage = list[index+4]
            gearbox = list[index+5]

            new_car = Car(make, model, capacity, year, mileage, gearbox)
            car_list.append(new_car)
        file.close

    def show_cars(self, car_list):
        for i, car in enumerate(car_list): #
            print(f"{i+1}. {car}")

    def show_car(self, car_list):
        print("Write index of the car")
        index = int(input())
        print(car_list[index-1])

    def sort(self, car_list):
        print("Tap the parameter by which you want to sort the list. \n(make, model, capacity, year, milage, gearbox)")
        text = input(" ")
        match text:
            case "make": car_list.sort(key=lambda x:x.make)
            case "model": car_list.sort(key=lambda x:x.model)
            case "capacity": car_list.sort(key=lambda x:x.capacity)
            case "year": car_list.sort(key=lambda x:x.year)
            case "milage": car_list.sort(key=lambda x:x.mileage)
            case "gearbox": car_list.sort(key=lambda x:x.gearbox)
        print("Sorted.")

    def bigger_than(self, car_list):
        print("Tap the parameter.")
        print("(capacity, year, milage)")
        text = input()
        print("Tap the parameter size.")
        number = input()
        match text:
            case "capacity": self.show_parameter(car_list, "capacity", number)
            case "year": self.show_parameter(car_list, "year", number)
            case "milage": self.show_parameter(car_list, "milage", number)

    def show_parameter(self, car_list, parameter, number):
        counter = 0
        for car in car_list:
            match parameter:
                case "capacity": element = car.capacity
                case "year": element = car.year
                case "milage": element = car.mileage

            if element >= number:
                counter += 1
                print(f"{counter}. {car}")

        if counter == 0: print("There is no such car.") 
            
    def sell(self):
        print("Tap make.")
        make = input()
        print("Tap model")
        model = input()
        print("Tap capacity.")
        capacity = input()
        print("Tap year.")
        year = input()
        print("Tap mileage")
        mileage = input()
        print("Tap gearbox.")
        gearbox = input()

        car = Car(make, model, capacity, year, mileage, gearbox)
        print(car)
        print("Do you want to sell it? (yes/no)")
        answer = input()
        if answer == "yes":
            self.current_cars.append(car)
            self.bought_cars.append(car)
            print("Sold!")

    def buy(self):
        print("Tap no. of the car, which you want to buy.")
        index = int(input())-1
        car = self.current_cars[index]
        print(car)
        print("Are you sure? (yes/no)")
        answer = input()
        if answer == "yes":
            self.current_cars.remove(car)
            self.sold_cars.append(car)
            print("Bought")

    def save(self, car_list, path: str):
        file = open(path, "w")
        for car in car_list:
            parameters = [car.make, car.model, car.capacity, 
                          car.year, car.mileage, car.gearbox]
            for parametr in parameters:
                file.write(f"{parametr}\n")
        file.close()
