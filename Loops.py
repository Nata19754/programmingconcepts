#   This is an opportunity to include all the concepts we have learned previously.  We will use Lists, If-else, variables, functions, and our new concept, loops.  The user will be greeted with a welcome message when the program begins.  The welcome message will say "Welcome to Taco Palace, please view the menu below and enter the number that represents your selection."  Below that message will be menu that will have 4 food options and 1 quit option.  The menu will be text and be produced by function call.  So therefore, there needs to be a function that prints a menu.  The user will make a selection (1 or 2 or etc).  The input is an integer.  The 4 options are food items that would be on a Taco Palace menu.  For example, Tacos, Burritos, Nachos.  Once selected, a message will state, "You have selected (fill in food item here)."  The option will call a function that retrieves the price of the food item.  Once the price is retrieved, the total amount due is updated.  The name of the item chosen is stored in a list.  The program then loops back to the beginning and asks for the other order.  It will continue to loop (repeat) until the user selects option 5 to quit.  Once the user quits the application, then you print the list of the food items the user ordered and the total price due.

items = ["Taco", "Burrito", "Nachos", "Soft Drink"]
prices = [3.00, 5.00, 4.00, 2.00]

# Prints menu items to user
def print_Menu():
    print("\nTaco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")

# Takes the users choice and returns the matching item name
def get_Item_Name(choice):
    return items[int(choice) - 1]

#Takes the users choice number and returns the matching price
def get_Item_Price(choice):
    return prices[int(choice) - 1]

# Turns the items orderedx into a sentence
def join_Sentence(words):
    n = len(words)
    if n == 0:
        return ""
    if n == 1:
        return words[0]
    if n == 2:
        return f"{words[0]} and {words[1]}"
    return ", ".join(words[:-1]) + f", and {words[-1]}"

# Uses a loop with counter to display each ordered item
def print_with_counter(seq):
    counter = 0
    while counter < len(seq):
        print(f"{counter + 1}. {seq[counter]}")
        counter = counter + 1
    print("end of list")

# Displays a welcome message to the user
def main():
    print("Welcome to Taco Palace! Please view the menu below and enter the number that represents your selection.")

    order_list = []
    total = 0.0
# Shows the menu until the user chooses to quit
    while True:
        print_Menu()
        choice = input("Enter your selection (1-5): ").strip()
        print(f"User entered: {choice}")

        if not choice.isdigit():
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        choice = int(choice)

        if choice == 5:
            break
        elif 1 <= choice <= 4:
            item = get_Item_Name(choice)
            price = get_Item_Price(choice)
            print(f"You selected a {item}")
            order_list.append(item)
            total = total + price
        else:
            print("Invalid selection. Please choose 1–5.")

    if len(order_list) > 0:
        print("\nYou ordered the following menu items:")
        print_with_counter(order_list)
        summary = join_Sentence(order_list)
        print(f"You ordered {summary}. Your total is ${total:.2f}")
    else:
        print("\nNo items were ordered. Goodbye!")

if __name__ == "__main__":
    main()