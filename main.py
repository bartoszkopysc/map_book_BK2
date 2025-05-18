

users:list = [
    {"name:":"Maciej","location":"Łódź","posts":100},
    {"name:":"Mateusz","location":"Łódź","posts":200},
    {"name:":"Maciej01","location":"Łódź","posts":300},
    {"name:":"Konrad","location":"Łódź","posts":400},
]


def get_user_info(users_data:list)->None:
    for user in users_data:
        print(f'Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user["posts"]} postów')

get_user_info(users)