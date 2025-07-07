# tee ratkaisusi tänne
class RecordApplication:
    def __init__(self):
        self.courses = {}

    def menu(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course_title = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        if course_title in self.courses.keys():
            self.courses[course_title].grade = grade
        else: 
            self.courses[course_title] = Course(course_title, grade, credits)

    def print_course(self):
        course_title = input("course: ")
        if course_title in self.courses:
            print(self.courses[course_title])
        else:
            print("no entry for this course")
            
    def get_stats(self):
        nb_completed_courses = 0
        total_credits = 0
        total_grades = 0
        grade_distr = {
            "5": 0,
            "4": 0,
            "3": 0,
            "2": 0,
            "1": 0
        }
        for course in self.courses.values():
            nb_completed_courses += 1
            total_credits += course.credits
            total_grades += course.grade
            grade_distr[str(course.grade)] += 1
        
        print(f"{nb_completed_courses} completed courses, a total of {total_credits} credits")
        print(f"mean {round(total_grades/nb_completed_courses, 1)}")
        print("grade distribution")
        for k,v in grade_distr.items():
            print(f"{k}: {'x'*v}")


    def execute(self):
        self.menu()
        while True:
            print("")
            cmd = input("command: ")
            if cmd == "1":
                self.add_course()
            elif cmd == "2":
                self.print_course()
            elif cmd == "3":
                self.get_stats()
            elif cmd == "0":
                break
            else:
                self.menu()


class Course:
    def __init__(self, title:str, grade:int, credits:int):
        self.title = title
        self._grade = grade
        self.credits = credits

    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, new_grade):
        if new_grade > self._grade:
            self._grade = new_grade

    def __str__(self):
        return f"{self.title} ({self.credits} cr) grade {self._grade}"

application = RecordApplication()
application.execute()
