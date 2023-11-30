from cars import Commission
import menu

commission = Commission()
commission.load_data()

cont = True
while cont:
    print(" 1 - Buy!")
    print(" 2 - Sell!")
    print(" 3 - About us")
    print(" 4 - Save changes")
    print(" 5 - Close")

    text = input()
    match text:
        case "1": menu.buy(commission)
        case "2": commission.sell()
        case "3": menu.about_us(commission)
        case "4": menu.save(commission)
        case "5": 
            print("Thank you!")
            cont = False
