# Write your solution here:
def sort_by_seasons(items:list):
    
    def get_season(item:dict):
        return item["seasons"]

    return [item for item in sorted(items, key=get_season)]


if __name__ == "__main__":
    shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]

    for show in sort_by_seasons(shows):
        print(f"{show['name']} {show['seasons']} seasons")