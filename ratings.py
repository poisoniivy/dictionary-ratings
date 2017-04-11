RESTAURANTS = {}

def get_restaurants():
    """Returns dictionary of restaurants with their rating after user input."""

    restaurant_list = open('scores.txt')

    for line in restaurant_list:
        line = line.rstrip()
        line = line.split(":")
        RESTAURANTS[line[0]] = line[1]

   # return restaurants


def print_ratings():
    """Prints an alphabetical list of restaurants and its rating. """

    for restaurant, rating in sorted(RESTAURANTS.iteritems()):
        print "{} is rated at {}.".format(restaurant, rating)


def add_restaurant():
    rest_name = raw_input("Enter a restaurant name: ")
           
    while True:
        rating = int(raw_input("Enter a rating: "))
        if rating not in range(1,6):
            print "That's not a valid score!"
            continue
        else:
            break
    RESTAURANTS[rest_name] = rating


def menu_choice():
    """Prompts user to chose a menu option."""

    while True:        
        print """Menu Choices:
                 1. See all ratings
                 2. Add a new restaurant
                 3. Quit
              """

        option = raw_input("Enter number: ")

        if option == '1':
            get_restaurants()
            print_ratings()
        elif option == '2':
            #restaurants = get_restaurants("scores.txt")
            add_restaurant()
            print_ratings()
        elif option == '3':
            break
        else:
            print "That's not a valid menu choice!" 


menu_choice()

