# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(items: list):
    def get_rating(item:dict):
        return -item["rating"]

    return [item for item in sorted(items, key=get_rating)]

if __name__ == "__main__":
    shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]

    print("Rating according to IMDB")
    for show in sort_by_ratings(shows):
        print(f"{show['name']}  {show['rating']}")