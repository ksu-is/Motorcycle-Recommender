# main.py rough draft, established initial prompts

def get_user_input():
    print("Welcome to the Motorcycle Recommender!\nPlease answer a few questions:\n")

    height = float(input("What is your height in inches? "))
    weight = float(input("What is your weight in pounds? "))
    experience = int(input("How many years of riding experience do you have? "))
    purpose = input("What is your riding purpose? (e.g., commuting, racing, off-roading, stunting, cruising): ").strip().lower()
    preference = input("What type of motorcycle do you prefer? (e.g., sport, cruiser, dirt, naked, touring): ").strip().lower()

    return {
        "height": height,
        "weight": weight,
        "experience": experience,
        "purpose": purpose,
        "preference": preference
    }


def recommend_motorcycles(user_data):
    print("\nThanks! Based on your input, here are some motorcycle recommendations:\n")

    if user_data["preference"] == "sport":
        print("- Yamaha YZF-R3")
        print("- Kawasaki Ninja 400")
    elif user_data["preference"] == "cruiser":
        print("- Harley-Davidson Iron 883")
        print("- Honda Rebel 500")
    elif user_data["preference"] == "dirt":
        print("- Suzuki DR-Z400")
        print("- Honda CRF250F")
    elif user_data["preference"] == "naked":
        print("- KTM Duke 390")
        print("- Yamaha MT-07")
    elif user_data["preference"] == "touring":
        print("- BMW R1250RT")
        print("- Honda Goldwing")
    else:
        print("- Honda CB500X (a good all-rounder)")
        print("- Kawasaki Versys 650")


if __name__ == "__main__":
    user_input = get_user_input()
    recommend_motorcycles(user_input)
#test upload