print()
print("Welcome to the area and perimeter calculator.")
print()

def num_check(question):
    valid = False
    while not valid:

        error = ("Please enter a number that is more than zero")

        try:

            response = float(input(question))
            
            if response > 0:
                return response

            else:
                print(error)
                print()
        
        except ValueError:
            print(error)


keep_going = ""
while keep_going == "":

    width = num_check("width: ")
    height = num_check("height: ")

    area = width * height
    perimeter = 2 * (width + height)

    print()

    print("perimeter: {} units".format(perimeter))
    print("area: {:.2f} squared units".format(area))
    print()

    keep_going = input("Press <enter> to keep going or any key to quit")

print()
print("Thanks for using the area and perimeter calculator")
