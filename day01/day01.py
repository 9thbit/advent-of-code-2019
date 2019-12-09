
def read_input(filename):
    with open(filename, "rt") as input_file:
        return [int(line) for line in input_file if line.strip()]


def compute_fuel(module):
    return (module // 3) - 2


def compute_fuel_for_fuel(initial_fuel):
    additional_mass = initial_fuel
    additional_fuel = 0
    while additional_mass > 0:
        additional_mass = compute_fuel(additional_mass)
        additional_fuel += max(additional_mass, 0)  # last one before breaking can be negative

    return additional_fuel


def main():
    filename = "input.txt"
    modules = read_input(filename)

    fuel_required = sum(map(compute_fuel, modules))
    print(f'Part 1: {fuel_required}')

    total_fuel_required = 0
    for module in modules:
        module_fuel = compute_fuel(module)
        fuel_for_fuel = compute_fuel_for_fuel(module_fuel)
        total_fuel_required += module_fuel + fuel_for_fuel
    print(f'Part 2: {total_fuel_required}')


if __name__ == "__main__":
    main()
