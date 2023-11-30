from cars import *

def buy(commission):
    while True:
        print("---BUY---")
        print(" 1 - Show list of current cars")
        print(" 2 - Show one car")
        print(" 3 - Sort")
        print(" 4 - Show cars with parameter bigger than...")
        print(" 5 - Buy")
        print(" 6 - Back")

        text = input()
        match text:
            case "1": commission.show_cars(commission.current_cars)
            case "2": commission.show_car(commission.current_cars)
            case "3": commission.sort(commission.current_cars)
            case "4": commission.bigger_than(commission.current_cars)
            case "5": commission.buy()
            case "6": return False

def about_us(commission):
    while True:
        print("---ABOUT---")
        print(" 1 - Current cars")
        print(" 2 - Sold cars")
        print(" 3 - Bought cars")
        print(" 4 - Back")

        text = input()
        match text:
            case "1": commission.show_cars(commission.current_cars)
            case "2": commission.show_cars(commission.sold_cars)
            case "3": commission.show_cars(commission.bought_cars)
            case "4": return False

def save(commission):
    commission.save(commission.current_cars, path="_Commission/files/after_current.txt")
    commission.save(commission.sold_cars, path="_Commission/files/after_sold.txt")
    commission.save(commission.bought_cars, path="_Commission/files/after_bought.txt")
    print("Saved")