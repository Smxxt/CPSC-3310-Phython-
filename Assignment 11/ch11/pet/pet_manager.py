from bird import Bird
from cat import Cat
from dog import Dog


def display_menu():
    print("\nPet Menu")
    print("1. Add Dog")
    print("2. Add Cat")
    print("3. Add Bird")
    print("4. Show All Pets")
    print("5. Exit")


def main():
    # Store pet objects in a list and process them polymorphically
    pets = []

    while True:
        display_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter dog's name: ").strip()
            pets.append(Dog(name))
        elif choice == "2":
            name = input("Enter cat's name: ").strip()
            pets.append(Cat(name))
        elif choice == "3":
            name = input("Enter bird's name: ").strip()
            pets.append(Bird(name))
        elif choice == "4":
            print("Your Pets:")
            for pet in pets:
                # Calls each pet's __str__() and overridden speak() method
                print(f"{pet} says {pet.speak()}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()