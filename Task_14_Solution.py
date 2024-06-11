/*14. Написать программу, имитирующую работу реестра домашних животных.
В программе должен быть реализован следующий функционал:
14.1 Завести новое животное
14.2 определять животное в правильный класс
14.3 увидеть список команд, которое выполняет животное
14.4 обучить животное новым командам
14.5 Реализовать навигацию по меню
15.Создайте класс Счетчик, у которого есть метод add(), увеличивающий̆
значение внутренней̆int переменной̆на 1 при нажатие “Завести новое
животное” Сделайте так, чтобы с объектом такого типа можно было работать в
блоке try-with-resources. Нужно бросить исключение, если работа с объектом
типа счетчик была не в ресурсном try и/или ресурс остался открыт. Значение
считать в ресурсе try, если при заведения животного заполнены все поля.*/




class Counter:
    def __init__(self):
        self.value = 0

    def add(self):
        self.value += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Error: {exc_type.__name__} - {exc_val}")
        elif self.value == 0:
            print("Resource not used")
        else:
            print(f"Resource used: {self.value}")

def add_animal(animals, animal_type, name):
    if animal_type == "Dog":
        animal = Dog(name)
    elif animal_type == "Cat":
        animal = Cat(name)
    elif animal_type == "Bird":
        animal = Bird(name)
    else:
        print("Invalid animal type.")
        return
    animals.append(animal)
    print(f"{animal_type} {name} has been added to the registry.")

def navigate_menu():
    animals = []
    counter = Counter()

    try:
        with counter:
            while True:
                print("\nMenu:")
                print("1. Add new animal")
                print("2. Determine animal class")
                print("3. List animal commands")
                print("4. Teach animal commands")
                print("5. Exit")
                choice = input("Enter your choice: ")

                if choice == "1":
                    animal_type = input("Enter the animal type (Dog, Cat, Bird): ")
                    name = input("Enter the animal's name: ")
                    add_animal(animals, animal_type, name)
                elif choice == "2":
                    animal_type = input("Enter the animal type (Dog, Cat, Bird): ")
                    animal_class = determine_animal_class(animal_type)
                    if animal_class:
                        name = input("Enter the animal's name: ")
                        animal = animal_class(name)
                        animals.append(animal)
                elif choice == "3":
                    if not animals:
                        print("No animals in the registry.")
                        continue
                    for i, animal in enumerate(animals):
                        print(f"{i}. {type(animal).__name__} {animal.name}")
                    animal_index = int(input("Enter the animal index: "))
                    animal = animals[animal_index]
                    list_animal_commands(animal)
                elif choice == "4":
                    if not animals:
                        print("No animals in the registry.")
                        continue
                    for i, animal in enumerate(animals):
                        print(f"{i}. {type(animal).__name__} {animal.name}")
                    animal_index = int(input("Enter the animal index: "))
                    animal = animals[animal_index]
                    teach_animal_commands(animal)
                elif choice == "5":
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"Error: {e}")

navigate_menu()