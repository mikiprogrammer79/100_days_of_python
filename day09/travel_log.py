# Travel Log

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

# Write the function that will allow new countries to be added to the travel_log. 
def add_new_country(country, num_visits, cities):
    travel_log.append({"country": country, "visits": num_visits, "cities": cities})

# While loop
alive = True
while alive:    
    # Prompt user 
    prompt = input("Type 'p' to print the travel log, or type 'add' to add new country: ").lower()
    if prompt == "p":
        for i in range(0, len(travel_log)):
            print(f"{travel_log[i]['country']}\n{travel_log[i]['visits']}\n{travel_log[i]['cities']}\n")
    elif prompt == "add":
        country = input("Add country name to your Travel Log: ").capitalize() # Add Country 
        visits = int(input("Number of visits: ")) # Number of visits 
        list_of_cities = input("Add cities (use comas ',') visited in that country: ").capitalize().split(", ")
        add_new_country(country, visits, list_of_cities)
    else:
        print("TypoError, type 'p' for print, or 'add' to add a new country to your travel log")
    exit = input("Do you want to exit? Type 'yes' for exit: ").lower()
    if exit == 'yes':
        alive = False
        print("Good Bye")