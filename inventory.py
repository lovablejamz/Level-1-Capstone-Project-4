class Shoes:

    # constructor
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # return the cost of the shoe
    def get_cost(self):
        return self.cost

    # return the quantity of the shoes
    def get_quantity(self):
        return self.quantity

    # return a string representation of a class
    def __str__(self):
        return self.country + ", " + self.code + ", " + self.product + ", " + str(self.cost) + ", " + str(self.quantity)


# create a variable with an empty list.
# this variable will be used to store a list of shoes objects
shoes = []

# open the file inventory.txt and read the data from this file
# transfer this object into the shoes list
def read_shoes_data():
    filename = "inventory.txt"
    try:
        lineNo = 0
        # open the file in read mode
        with open(filename, 'r') as f:
            # iterate through the file contents
            for line in f:
                if lineNo != 0:
                    # storing the read data by splitting
                    (country,code, product, cost, quantity) = line.rstrip('\n').strip().split(',')
                    # add the data to the shoes list
                    shoes.append(Shoes(country,code,product,int(cost),int(quantity)))

                lineNo += 1
        print("Reading Data from Inventory.txt file")
    except IOError:
        print("File ", filename, " not accessible")

read_shoes_data()

# this function will allow the user to capture data about a shoe
# and use this data to create a shoe object and append this object
# inside the shoe list
def capture_shoes():
    with open('inventory.txt', 'a') as f1:
        s_country = input("Enter country: ")
        s_code = input("Enter code: ")
        s_product = input("Enter product: ")
        s_cost = int(input("Enter the cost: "))
        s_quantity = int(input("Enter quantity: "))

        # create an instance of shoe object
        shoe = Shoes(s_country,s_code,s_product,s_cost,s_quantity)
        # add shoe to list
        shoes.append(shoe)
        f1.write("\n" + str(shoe))
        

# iterate over all the shoes list and print the details of each shoe
def view_all():
    for shoe in shoes:
        print(str(shoe))

# this function will find the shoe object with the lowest quantity,
# which is the shoe that needs to be restocked
def re_stock():
    lowest_quantity = shoes[0]
    # iterate through the list
    for shoe in shoes:
        # check which quantity is the lowest
        if shoe.get_quantity() < lowest_quantity.get_quantity():
            lowest_quantity = shoe

    print("Lowest Quantity Details\n" + str(lowest_quantity))

    # Check if the user wants to add the quantity of shoes
    # and if the user wants to update it
    need_restock = input("Add to quantity of shoes? (yes/no) \n")
    if need_restock.lower() == "yes":
        quantity_to_update = int(input("Enter quantity to update: "))
        lowest_quantity.quantity = lowest_quantity.get_quantity() + quantity_to_update
        s_shoes = ["{}\n".format(shoe) for shoe in shoes]

        # Write the new quantity to inventory.txt
        with open('inventory.txt', 'w') as fout:
            fout.writelines(s_shoes)
            print('Stock updated \n')
        fout.close()
    else:
        print("Do not restock")


# search for a shoe from the list using a code
def search_shoe(code):
    # iterate through the list
    for shoe in shoes:
        # check if the code is the same
        if shoe.code == code:
            return shoe

# calculate the total value for each item
def value_per_item():
    value = 0
    # iterate through the list
    for shoe in shoes:
        value = shoe.get_cost() * shoe.get_quantity()

        print(str(shoe) + " , Value: " + str(value))

    # return the value
    return value


# determine the product with the highest quantity
# print the shoe for sale
def highest_qty():
    highest_quantity_shoe = shoes[0]
    # iterate through the list
    for shoe in shoes:
        # check if quantity is the highest
        if shoe.get_quantity() > highest_quantity_shoe.get_quantity():
            highest_quantity_shoe = shoe

    print(str(highest_quantity_shoe))

if __name__ == '__main__':
    choice = 0
    while True:
        print("1. Capture shoes")
        print("2. View all shoes")
        print("3. Restock shoes")
        print("4. Search shoe")
        print("5. Total value of stock")
        print("6. Quit")

        # ask user to choose from menu
        choice = int(input("Enter the number of your choice: "))

        # base on user's choice
        # call appropriate functions
        if choice == 1:
            capture_shoes()
        elif choice == 2:
            view_all()
        elif choice == 3:
            re_stock()
        elif choice == 4:
            code = input("Enter code: ")
            print(str(search_shoe(code)))
        elif choice == 5:
            value_per_item()
        elif choice == 6:
            print("Thank you.")
            break
        else:
            print("Invalid choice. Please try again.\n")
