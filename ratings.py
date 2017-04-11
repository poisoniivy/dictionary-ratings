def get_restaurants(filename):
    """Returns dictionary of restaurants with their rating after user input."""

    restaurants = {}
    restaurant_list = open(filename)

    for line in restaurant_list:
        line = line.rstrip()
        line = line.split(":")
        restaurants[line[0]] = line[1]

    return restaurants


def print_ratings(restaurants):
    """Prints an alphabetical list of restaurants and its rating. """

    for restaurant, rating in sorted(restaurants.iteritems()):
        print "{} is rated at {}.".format(restaurant, rating)


def add_restaurant(restaurants):
    rest_name = raw_input("Enter a restaurant name: ")
    rating = raw_input("Enter a rating: ")

    restaurants[rest_name] = rating

restaurants = get_restaurants("scores.txt")
add_restaurant(restaurants)
print_ratings(restaurants)
