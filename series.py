# Write your solution here:
class Series:
    def __init__(self, title: str, num_seasons: int, genres: list):
        self.title = title
        self.num_seasons = num_seasons
        self.genres = genres
        self.list_ratings = []

    def rate(self, rating: int):
        if rating < 0 or rating > 5:
            raise ValueError("ValueError: You only can rate between 0 and 5.")
        else:
            self.list_ratings.append(rating)

    def __str__(self):        
        if len(self.list_ratings) > 0:
            number_ratings = len(self.list_ratings)
            sum_ratings = 0
            for rating in self.list_ratings:
                sum_ratings += rating
            average = sum_ratings/number_ratings
            return f"{self.title} ({self.num_seasons} seasons)\ngenres: {', '.join(self.genres)}\n{number_ratings} ratings, average {round(average,1)} points"
        else:
            return f"{self.title} ({self.num_seasons} seasons)\ngenres: {', '.join(self.genres)}\nno ratings"

def minimum_grade(rating: float, series_list: list):
    list_of_series = []
    for series in series_list:
        sum_ratings = 0
        for r in series.list_ratings:
            sum_ratings += r
        average_rating = sum_ratings/len(series.list_ratings)
        if average_rating >= rating:
            list_of_series.append(series)
    return list_of_series

def includes_genre(genre: str, series_list: list):
    list_of_series = []
    for series in series_list:
        if genre in series.genres:
            list_of_series.append(series)
    return list_of_series


if __name__ == "__main__":
    # s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    # s1.rate(5)

    # s2 = Series("South Park", 24, ["Animation", "Comedy"])
    # s2.rate(3)

    # s3 = Series("Friends", 10, ["Romance", "Comedy"])
    # s3.rate(2)


    # series_list = [s1, s2, s3]

    # minimum_grade(4.5, series_list)
    # print("a minimum grade of 4.5:")
    # for series in minimum_grade(4.5, series_list):
    #     print(series.title)

    # print("genre Comedy:")
    # for series in includes_genre("Comedy", series_list):
    #     print(series.title)

    serie = Series("Dexter", 8, ['Crime', 'Drama', 'Mystery', 'Thriller'])
    print(serie)