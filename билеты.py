num_tickets = int(input("Введите количество билетов: "))
total_price = 0
# Проверка на наличие скидки
discount = False
if num_tickets > 3:
    discount = True
# Цикл для каждого билета
for i in range(num_tickets):
    age = int(input("Введите возраст посетителя: "))
    # Подсчет стоимости в зависимости от возраста
    if age < 18:
        ticket_price = 0
    elif age >= 18 and age < 25:
        ticket_price = 990
    else:
        ticket_price = 1390
    # Применение скидки
    if discount:
        ticket_price = ticket_price * 0.9
    # Добавление стоимости билета к общей стоимости
    total_price += ticket_price
# Вывод общей стоимости
print("Общая стоимость билетов:", total_price, "руб.")
