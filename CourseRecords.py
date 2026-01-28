import json

class FileHandler:

    def __init__ (self, filename):
        self._filename = filename

    def save_data(self, data):
        #Writing on the file
        try:
            with open(self._filename, "w", encoding="utf-8") as file:
                
                    #(what I want to save, where to save, indent if I want)
                    json.dump(data, file, indent=4)
                    print("DATA SAVED!")          
        except Exception as e:
            print(f"\nError: {e}")

    def load_data(self):
        #understanding the file
        try:
            with open(self._filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}


class StudentData:
    def __init__ (self, handler:FileHandler):
        self._handler = handler
        self._courses = self._handler.load_data()

    def add_course(self, name:str, grade:int, credit:int):
        self._courses[name.lower()] = (grade,credit)
        self._handler.save_data(self._courses)
        print("COURSE ADDED!")
        print()
    
    def search_data(self, name):
        if name.lower() in self._courses:
            print()
            print("COURSE FOUND!")
            print(f"Name: {name.capitalize()}")
            print(f"Grade: {self._courses[name.lower()][0]}")
            print(f"Credit: {self._courses[name.lower()][1]}")
            print()
        else:
            print()
            print("Course Wasn't Found!")
            print()

    def remove_course(self, name):
        if name.lower() in self._courses:
            self._courses.pop(name.lower())
            self._handler.save_data(self._courses)
            print("COURSE REMOVED!")
            print()
        else:
            print()
            print("Course Wasn't Found!")
            print()

    def complete_data(self):
        print("--------------")
        print("COMPLETE DATA")
        print("--------------")
        for key, value in self._courses.items():
            print()
            print(f"Name: {key.capitalize()}")
            print(f"Grade: {value[0]}")
            print(f"Credits: {value[1]}")
            print()

class CourseDataApp:
    def __init__ (self):
        self._handler = FileHandler("data.json")
        self._studentdata = StudentData(self._handler)

    def menu(self):
        print()
        print("<-- MENU -->")
        print()
        print("(1): Add Course")
        print("(2): Search Course")
        print("(3): Remove Course")
        print("(4): Complete Student Data")
        print("(0): Exit")
        print("-------------")


    def execute(self):
        while True:
            self.menu()
            try:
                opt = int(input("Option:"))
                match opt:
                        case 0:
                            break

                        case 1:
                            print()
                            name = input("Name:")
                            grade = int(input("Grade:"))
                            credits = int(input("Credits:"))
                            self._studentdata.add_course(name,grade,credits)
                            continue

                        case 2:
                            print()
                            name = input("Name:")
                            self._studentdata.search_data(name)
                            continue

                        case 3:
                            print()
                            name = input("Name:")
                            self._studentdata.remove_course(name)
                            continue

                        case 4:
                            print()
                            if self._studentdata._courses:
                                self._studentdata.complete_data()
                            else:
                                print("No Data Found!")
                                print()
                                continue

                        case _:
                            print()
                            print("Invalid Option!")
                            print()
                            continue
            except ValueError:
                print()
                print("Invalid Entry! Type a VAlid Option!")
                print()





#TITLE
title = "COURSE DATA APP"
print("-"*len(title))
print(title)
print("-"*len(title))

#APP
app = CourseDataApp()
app.execute()
print()
print("Shutting Down...")
print("Goodbye!")



        
