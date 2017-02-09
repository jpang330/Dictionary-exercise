shopping_list = {
    "target": ["socks", "soap", "detergent", "sponges"],
    "bi-rite": ["butter","cake","cookies","bread"],
    "berkeley_bowl": ["apples","oranges","bananas","milk"],
    "safeway": ["oreos","brownies","soda"],
    }

# print """0 Main Menu
# 1 Show all lists.
# 2 Show a specific list.
# 3 Add a new shopping list.
# 4 Add an item to a shopping list.
# 5 Remove an item from a shopping list.
# 6 Remove a list by nickname.
# 7 Exit when you are done."""
def user_choice(shopping_list):

    choice = int(raw_input("Choose a number option from the main menu?"))
    if choice == 1:
            return shopping_list
    
    if choice == 2:
        grocery_store = raw_input("which list do you want?")
        print shopping_list[grocery_store]
        return shopping_list
    if choice == 3:
        new_store = raw_input("what store would you like to add?")
        shopping_list[new_store]= []
        return shopping_list
#         new_items = raw_input("what is your shopping list? ")
#         shopping_list[new_store].append(new_items)
#         print shopping_list
# def add_list()
    if choice == 4:
        new_list = raw_input("what item would you like to add to list? ")
        new_store = raw_input("what is the name of list? ")
        shopping_list[new_store].append(new_list)
        return shopping_list

    if choice == 5:
        store = raw_input("which list do you want to look at? ")
        print shopping_list[store]
        remove_item = raw_input("What item would you like to remove? ")
        shopping_list[store].remove(remove_item)
        return shopping_list
    
    if choice == 6:
        delete_list = raw_input("which store list would you like to remove? ")
        del shopping_list[delete_list]
        return shopping_list

    if choice == 7:
        return False

def main():

    while shopping_list is not False:
        user_choice(shopping_list)
        print shopping_list

if __name__ == "__main__":
    main()