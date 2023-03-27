# ask the user for the number of tickets
num_tickets = int(input("Сколько билетов вы хотите купить? "))

# initialize variables for counting the number of visitors in different age groups
num_children = 0
num_students = 0
num_adults = 0

# ask for the age of each visitor and update the appropriate counter
for i in range(num_tickets):
    age = int(input("Укажите возраст посетителя: "))
    if age < 18:
        num_children += 1
    elif age < 25:
        num_students += 1
    else:
        num_adults += 1

# calculate the total cost
total_cost = num_students * 990 + num_adults * 1390

# apply the discount if applicable
if num_tickets > 3:
    total_cost *= 0.9

# output the result
print("Сумма к оплате:", total_cost, "руб.")