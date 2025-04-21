
def main():
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    RESET = '\033[0m'
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    print(f"\nTemperature: {BOLD}{ITALIC}{fahrenheit}F{RESET} = {celsius}C")

if __name__ == '__main__':
    main()
