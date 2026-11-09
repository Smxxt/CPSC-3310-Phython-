import random

def main():
    states_capitals = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock',
        'California': 'Sacramento',
        'Colorado': 'Denver',
        'Connecticut': 'Hartford',
        'Delaware': 'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta',
        'Hawaii': 'Honolulu',
        'Idaho': 'Boise',
        'Illinois': 'Springfield',
        'Indiana': 'Indianapolis',
        'Wyoming': 'Cheyenne',
        'New Hampshire': 'Concord'
    }
    
    correct_count = 0
    incorrect_count = 0
    
    states_list = list(states_capitals.keys())
    
    while True:
        selected_state = random.choice(states_list)
        correct_capital = states_capitals[selected_state]
        
        user_input = input(f"What is the capital of {selected_state}? (or enter 0 to quit): ").strip()
        
        if user_input == '0':
            break
        
        if user_input.lower() == correct_capital.lower():
            print("That is correct.")
            correct_count += 1
        else:
            print("That is incorrect.")
            incorrect_count += 1
        
    print(f"You had {correct_count} correct responses and {incorrect_count} incorrect responses.")

if __name__ == '__main__':
    main()