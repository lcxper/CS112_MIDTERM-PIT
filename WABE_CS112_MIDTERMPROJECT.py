import random


# Function to determine if a pet gets sick or injured with a given probability
def get_sick_or_injured(probability=0.10):
    return random.random() < probability


# Function to simulate the death of a pet based on its age and a death probability
def simulate_pet_death(lifespan, age, death_probability=0.05):
    return age >= lifespan - 1 and random.random() < death_probability


# Function to adopt a pet and get its initial attributes
def adopt_pet():
    pet_type = random.choice(["cat", "dog"])
    name = input(f"Enter a name for your {pet_type}: ")

    age = random.randint(1, 10)  # Assign a random age between 1 and 10 years
    lifespan = 15 if pet_type == "cat" else 12

    hunger = random.randint(30, 70)  # Random initial hunger level between 30 and 70
    happiness = random.randint(30, 70)  # Random initial happiness level between 30 and 70

    return name, pet_type, age, lifespan, hunger, happiness


# Function to get a newborn pet and specify its initial attributes
def get_newborn_pet():
    pet_type = None
    while pet_type not in ["cat", "dog"]:
        pet_type = input("Do you want a cat or a dog? ").lower()

    name = input(f"Enter a name for your {pet_type}: ")
    age = 0

    lifespan = 15 if pet_type == "cat" else 12

    return name, pet_type, age, lifespan


# Function to adjust hunger and happiness as a pet ages
def age_health_changes(age, happiness, hunger):
    new_hunger = max(min(hunger - age, 100), 0)
    new_happiness = max(min(happiness - age, 100), 0)
    return new_hunger, new_happiness


# Function to feed the pet with a risk of food poisoning
def feed_pet_with_risk(name, hunger, happiness):
    food_poisoning_probability = 0.30
    if random.random() < food_poisoning_probability:
        print(f"Oh no! {name} got food poisoning.")
        return True
    else:
        max(min(hunger, happiness - 15, 100), 0)
        return False


# Function to simulate overplaying with the pet with a risk of injury
def overplay_with_pet(name, happiness):
    injury_probability = 0.30
    if random.random() < injury_probability:
        print(f"\nOh no! {name} got injured while playing.")
        return True
    else:
        max(min(happiness - 15, 100), 0)
        return False


# Function to celebrate a pet's birthday
def celebrate_birthday(name, age):
    print(f"Happy Birthday, {name}! {name} is now {age} years old.")


# Function to simulate a walk with the pet and adjust its happiness
def walk_pet(happiness):
    success_probability = 0.90
    new_happiness = max(min(happiness + 10 if random.random() < success_probability else happiness - 5, 100), 0)
    return new_happiness


# Function to feed the pet
def feed_pet(name, hunger, happiness):
    new_hunger = max(min(hunger + 15, 100), 0)
    new_happiness = max(min(happiness + 5, 100), 0)  # Increase happiness after feeding
    print(f"{name} is fed.")
    return new_hunger, new_happiness


# Function to play with the pet
def play_with_pet(name, happiness, hunger):
    new_happiness = max(min(happiness + 20, 100), 0)
    new_hunger = max(min(hunger - 10, 100), 0)
    print(f"{name} is happy!")
    return new_happiness, new_hunger


# Function to treat the pet during a vet visit when hunger or happiness is below 30
def treat_pet(name, hunger, happiness):
    print(f"\n{name} is receiving treatment at the vet.")

    # Treat hunger and happiness
    new_hunger = min(hunger + 10, 100)
    new_happiness = min(happiness + 10, 100)

    print(f"{name}'s condition has improved. Hunger: {new_hunger}, Happiness: {new_happiness}")

    return new_hunger, new_happiness


# Function to check if the pet needs a vet visit
def seek_vet_help(name):
    print(f"\n{name} seems to be showing unusual behavior or signs of sickness.")
    choice = input(f"Do you want to take {name} to the vet for a check-up? (yes/no): ")
    return choice.lower() == 'yes'


# Function to determine the outcome of a vet visit
def vet_visit_outcome(hunger, happiness):
    success_probability = 0.70  # Adjust the probability as needed
    return random.random() < success_probability and (hunger < 30 or happiness < 30)


# Function to ask the user if they want to take their pet to the vet
def take_pet_to_vet(name):
    choice = input(f"Do you want to take {name} to the vet for a check-up? (yes/no): ")
    return choice.lower() == 'yes'


# Main function to simulate the virtual pet game
def main():
    print("Welcome to the Virtual Pet Simulator!")
    print("1. Adopt a Pet")
    print("2. Get a Newborn Pet")

    while True:
        choice = input("Enter your choice (1/2): ")
        if choice in ["1", "2"]:
            break
        else:
            print("Invalid choice. Please enter '1' or '2'.")

    if choice == "1":
        name, pet_type, age, lifespan, hunger, happiness = adopt_pet()
    else:
        name, pet_type, age, lifespan = get_newborn_pet()
        hunger = 50
        happiness = 50

    activity_counter = 0

    print(f"You adopted a {pet_type} named {name}.")
    print(f"{name}'s Stats: Hunger: {hunger}, Happiness: {happiness}\n")

    while age < lifespan:
        print(f"{name}'s Stats: Hunger: {hunger}, Happiness: {happiness}")
        print(f"{name} is a {pet_type} aged {age} (Lifespan: {lifespan} years)")
        print("What would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Go to Vet")
        print("4. Walk/Stroll")
        print("5. Quit")

        while True:
            choice = input("Enter your choice (1/2/3/4/5): ")
            if choice.isdigit() and 1 <= int(choice) <= 5:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        if choice == "5":
            print("Goodbye! Thanks for playing.")
            break

        if simulate_pet_death(lifespan, age):
            print(f"{name} suddenly passed away. Game over!")
            break

        if happiness <= 0:
            print(f"{name} has become depressed and refuses to eat, play, or walk.")
            choice = input(f"Do you want to take {name} to the vet for a check-up? (yes/no): ")
            if choice.lower() == 'yes':
                if take_pet_to_vet(name):
                    if vet_visit_outcome(hunger, happiness):
                        hunger, happiness = treat_pet(name, hunger, happiness)
                    else:
                        print(f"{name} is still not feeling well. Please monitor {name}'s condition.")
                else:
                    print(f"{name} is not feeling well. Consider visiting the vet soon.")
            else:
                print(f"{name} remains depressed.")

        if hunger >= 100:
            print(f"{name} has become sick due to overeating.")
            choice = input(f"Do you want to take {name} to the vet for a check-up? (yes/no): ")
            if choice.lower() == 'yes':
                if take_pet_to_vet(name):
                    if vet_visit_outcome(hunger, happiness):
                        hunger, happiness = treat_pet(name, hunger, happiness)
                    else:
                        print(f"{name} is still not feeling well. Please monitor {name}'s condition.")
                else:
                    print(f"{name} remains sick due to overeating.")

        elif choice == "1":
            hunger, happiness = feed_pet(name, hunger, happiness)
            if feed_pet_with_risk(name, hunger):
                print(f"Urgent! {name} needs to go to the vet for food poisoning.")
                if take_pet_to_vet(name):
                    if vet_visit_outcome(hunger, happiness):
                        hunger, happiness = treat_pet(name, hunger, happiness)
                    else:
                        print(f"{name} is still not feeling well. Please monitor {name}'s condition.")
                else:
                    print(f"{name} might need to see a vet soon.")

        elif choice == "2":
            happiness, hunger = play_with_pet(name, happiness, hunger)
            if overplay_with_pet(name, happiness):
                print(f"Urgent! {name} needs to go to the vet for an injury.")
                if take_pet_to_vet(name):
                    if vet_visit_outcome(hunger, happiness):
                        hunger, happiness = treat_pet(name, hunger, happiness)
                    else:
                        print(f"{name} is still not feeling well. Please monitor {name}'s condition.")
                else:
                    print(f"{name} might need to see a vet soon.")

        elif choice == "3":
            if get_sick_or_injured():
                print(f"\nOh no! {name} is feeling sick or injured.")
                if take_pet_to_vet(name):
                    if vet_visit_outcome(hunger, happiness):
                        hunger, happiness = treat_pet(name, hunger, happiness)
                    else:
                        print(f"{name} is still not feeling well. Please monitor {name}'s condition.")
                else:
                    print(f"{name} is not feeling well. Consider visiting the vet soon.")
                happiness = max(happiness - 10, 0)  # Decrease happiness after going to vet
            else:
                print(f"{name} is healthy as a horse!")

        elif choice == "4":
            happiness = walk_pet(happiness)
            hunger = max(hunger - 5, 0)  # Decrease hunger after walking
            print(f"{name} is happy!")

        activity_counter += 1

        if activity_counter >= 12:
            activity_counter = 0
            age += 1
            celebrate_birthday(name, age)

        hunger, happiness = age_health_changes(age, happiness, hunger)

        if hunger <= 20:
            print(f"{name} is hungry! Please feed {name}.")
        if happiness <= 20:
            print(f"{name} is sad! Spend some time with {name}.")

        while True:
            another_action = input(f"Do you want to do something else with {name}? (yes/no): ")
            if another_action.lower() == 'yes' or another_action.lower() == 'no':
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if another_action.lower() != 'yes':
            break

    print(f"{name} has reached the end of its lifespan. Goodbye!")


if __name__ == "__main__":
    main()

# End
