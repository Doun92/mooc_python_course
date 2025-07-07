class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution herer:
def sort_by_length(routes: list):

    def by_length(route: ClimbingRoute):
        return -route.length

    return [route for route in sorted(routes, key=by_length)]

def sort_by_difficulty(routes: list):
    grade_order = [
        "4", "4+", "5", "5+","6A", "6A+", "6B",
        "6B+", "6C", "6C+", "7A", "7A+", "7B",
        "7B+", "7C", "7C+","8A", "8A+", "8B",
        "8B+", "8C", "8C+"
    ]
    def by_grade(route: ClimbingRoute):
        return (grade_order.index(route.grade), route.length)

    return [route for route in sorted(routes, key=by_grade, reverse=True)]

if __name__ == "__main__":
    r1 = ClimbingRoute("Edge", 38, "6A+")
    r2 = ClimbingRoute("Smooth operator", 9, "7A")
    r3 = ClimbingRoute("Syncro", 14, "8C+")
    r4 = ClimbingRoute("Big cut", 36, "6B")
    r5 = ClimbingRoute("Fruit garden", 8, "6A")
    r6 = ClimbingRoute("No grip", 12 , "6B+")
    r7 = ClimbingRoute("Small steps", 13, "6A+")
    r8 = ClimbingRoute("The Swedish route", 42, "5+")
    sort_by_difficulty([r1, r2, r3, r4, r5, r6, r7, r8])
