print ("Работа в мак")

print (" Как будут звать вашаго героя?")

rabotnik = {
    "name": "",
    "age": "",
    "cfalifik": "",
}

rabotnik["name"] = str(input("Введите имя")) 

rabotnik["age"] = str(input("Введите возраст")) 

rabotnik["cfalifik"] = int(input("Введите специализацию вашего героя: 1 - бургеры, 2 - картошка, 3 - напитки")) 

cfalifik1 = rabotnik.pop("cfalifik")


if cfalifik1 == 1:
    print("Для того, чтобы взять Вас на работу, вам необходимо  выполнить 3 заказа")
    tuple_burg = ("1 заказ - сделать гамбургер", "2 заказ - сделать двойной чизбургер", "3 заказ - биг тести три сыра")
    
elif cfalifik1 == 2:
    print("Для того, чтобы взять Вас на работу, вам необходимо  выполнить 3 заказа")
    tuple_burg = ("1 заказ", "2 заказ", "3 заказ")
else:
    print("Для того, чтобы взять Вас на работу, вам необходимо  выполнить 3 заказа")
    tuple_burg = ("1 заказ", "2 заказ", "3 заказ")
