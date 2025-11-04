money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

months = 0
current = money_capital
current_spend = spend

while current + salary >= current_spend:
    current = current + salary - current_spend
    months += 1
    current_spend *= (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", months)