
def main():
    C = 299792458
    while True:
        try:
            mass_input = input("Enter kilos of mass: ")
            if mass_input.lower() == 'exit':
                break
            m = float(mass_input)
            print(f"\n*{mass_input}*\n")
            print("e = m * C^2...\n")
            print(f"m = {m} kg")
            print(f"C = {C} m/s\n")
            energy = m * C ** 2
            print(f"{energy} joules of energy!\n")
        except ValueError:
            print("Please enter a valid number for mass.\n")

if __name__ == '__main__':
    main()
