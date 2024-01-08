#[Temprature Coverter] 
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    while True:
        print("\n*** Temperature Converter ***")
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print("\n---------------------------------------------")
            print(f'{fahrenheit}°F is equal to {celsius:.2f}°C')
            print("---------------------------------------------")
        elif choice == '2':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print("\n---------------------------------------------")
            print(f'{celsius}°C is equal to {fahrenheit:.2f}°F')
            print("---------------------------------------------")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
