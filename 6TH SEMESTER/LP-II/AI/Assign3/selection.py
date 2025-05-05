"""
Assignment-A3.I (Selection Sort)

Problem Statement: Implement Greedy search algorithm for any of the following application:
    I. Selection Sort
"""

numbers = [] # Empty list to store numbers

# Function to take input for numbers
def input_numbers():
        total = int(input("\nHow many numbers you wish to enter?\nTotal numbers:\t"))
        for i in range(total):
                val = float(input(f"Enter number {i+1}:\t"))
                numbers.append(val)
        print("Numbers you've entered are:\t", numbers)

# Function for selection sort
def selection_sort():
    for i in range(len(numbers)):
        min_index = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i] # Swapping
    print("\nNumbers sorted in ascending order using selection sort:\t", numbers)

# Main function for menu
def main():
  while True:
    print("\n\n", "-"*10, "MAIN MENU", "-"*10)
    print("1. Enter numbers")
    print("2. Apply selection sort")
    print("3. List numbers")
    print("4. Exit")
    choice = int(input("Choose an option (1-4):\t"))
    print("-"*32)

    if (choice == 1):
      input_numbers()
    elif (choice == 2):
      selection_sort()
    elif (choice == 3):
      print("\nNumbers you've entered are:\t", numbers)
    elif (choice == 4):
      print("\n## END OF CODE\n")
      break
    else:
      print("\nPlease choose a valid option (1-4)")

main()
