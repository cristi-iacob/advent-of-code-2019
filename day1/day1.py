def calculate_fuel(mass):
    return mass // 3 - 2


def calculate_total_fuel_for_mass(mass):
    total = 0

    while mass > 0:
        current_fuel = calculate_fuel(mass)

        if current_fuel > 0:
            total += current_fuel

        mass = current_fuel

    return total


def read_data():
    file = open("input.txt", "r")
    ret_list = []

    for line in file:
        ret_list.append(int(line))

    return ret_list


def solve_task1():
    masses = read_data()
    answer = 0

    for mass in masses:
        answer += calculate_fuel(mass)

    print(answer)


def solve_task2():
    masses = read_data()
    answer = 0

    for mass in masses:
        answer += calculate_total_fuel_for_mass(mass)

    print(answer)


solve_task2()
