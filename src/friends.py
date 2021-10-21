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


