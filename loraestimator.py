import os
import time
import math

TOTAL_MAX = 4500
ACCEPTABLE_MIN = 3000

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Simple input validation
def validate_user_input(prompt):
     while True:
          user_input = input(prompt)
          try:
               return int(user_input)
          except ValueError:
               print(f"Invalid input, please enter a valid value")

# Find the ideal epoch ranges
def calculator(size, repeats, batch, ga):
     results = {
          "min_estimated_steps": 0,
          "max_estimated_steps": 0,
          "min_effective_steps": 0,
          "max_effective_steps": 0,
          "min_recommended_epochs": 0,
          "max_recommended_epochs": 0,
     }
     effective_multiplier = batch * ga
     image_count_total = size * repeats
     results["min_recommended_epochs"] = int(math.ceil(((ACCEPTABLE_MIN * batch * ga)/ (size * repeats)) / effective_multiplier))
     results["max_recommended_epochs"] = int(math.ceil(((TOTAL_MAX * batch * ga) / (size * repeats)) / effective_multiplier))
     results["min_estimated_steps"] = int(image_count_total * results["min_recommended_epochs"])
     results["max_estimated_steps"] = int(image_count_total * results["max_recommended_epochs"])
     results["min_effective_steps"] = int((image_count_total * results["min_recommended_epochs"]) / effective_multiplier)
     results["max_effective_steps"] = int((image_count_total * results["max_recommended_epochs"]) / effective_multiplier)
     return results

# Simple TUI-like prompt
def tui():
    print(f"##########################")
    print(f"# Kiba's Lora Calculator #")
    print(f"##########################")
    print(f"\n")
    print(f"Free and open pupware(tm)")
    print(f"Free to use and modify~!")
    time.sleep(1)
    
    # Dataset size
    clearscreen()
    print("What's the size of your dataset?")
    print(f"\n")
    setsize = validate_user_input("Dataset size: ")

    # Repeat count
    clearscreen()
    print(f"How many repeats do you want to work with?")
    print(f"\n")
    imgrepeats = validate_user_input("Repeats: ")

    # Batch size
    clearscreen()
    print(f"What batch size are you working with?")
    print(f"\n")
    batchsize = validate_user_input("Batch size: ")

    # GA steps
    clearscreen()
    print(f"What GA (Gradient Accumulation) steps are you working with?")
    print(f"\n")
    gasteps = validate_user_input("GA Steps: ")

    # Final result
    clearscreen()
    finalresults = calculator(setsize, imgrepeats, batchsize, gasteps)
    print(f"###############################")
    print(f"Here's your recommended params:")
    print(f"\n")
    print(f"Given image set count", setsize)
    print(f"Given image repeats:", imgrepeats)
    print(f"Given batch size:", batchsize)
    print(f"Given GA steps:", gasteps)
    print(f"Recommended Max Epoch range:", finalresults["min_recommended_epochs"], "-", finalresults["max_recommended_epochs"])
    print(f"Estimated steps range:", finalresults["min_estimated_steps"], "-", finalresults["max_estimated_steps"])
    print(f"Effective steps range:", finalresults["min_effective_steps"], "-", finalresults["max_effective_steps"])
            
def main():
    tui()

if __name__ == "__main__":
    main()
