import pdb

def get_name(person):
    return(person["name"])

def get_favourite_tv_show(person):
    return (person["favourites"]["tv_show"])

def likes_to_eat(person,food):
        
    food_found = False

    for snack in person["favourites"]["snacks"]:
            if snack == food:
                food_found = True
    
    return food_found


def add_friend(person, new_friend):
    person["friends"].append(new_friend)


def remove_friend(person, ex_friend):

    person["friends"].remove(ex_friend)

def total_money(people):
    total_cash = 0

    for person in people:
        total_cash += person["monies"]
    
    return total_cash

def l_money(person2, person1, money_lent):
    person1["monies"] += money_lent
    person2["monies"] -= money_lent


def all_favourite_foods(people):
    food_list = []

    for person in people:
    
        food_list += person["favourites"]["snacks"]
        
    return food_list

def find_no_friendends(people):
    friendless = []
    for person in people:
        if len(person["friends"]) == 0:
            friendless.append(person)
            # friendless += person
    pdb.set_trace()
    return friendless