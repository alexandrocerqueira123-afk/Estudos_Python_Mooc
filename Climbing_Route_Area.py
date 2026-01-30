
class ClimbingRoute:
    def __init__ (self, name:str, lenght:int, grade:str):
        self.name = name
        self.lenght = lenght
        self.grade = grade

    def __str__(self):
        return f"{self.name}, lenght {self.lenght}, grade {self.grade}"

class ClimbingArea:
    def __init__ (self, name:str):
        self.name = name
        self.climbing_list = []

    def add_route(self, route:ClimbingRoute):
        self.climbing_list.append(route)


    def sort_by_dif (self):
        return sorted(self.climbing_list, key=lambda r: (r.grade, r.lenght), reverse=True)
    
    def routes(self):
        if not self.climbing_list:
            print(f"[No Routes Added!]")
        else:
            for route in self.climbing_list:
                print(route)

    #HARDEST ROUTE IN AREA

    def hardest_route(self):
        if self.climbing_list:
            return self.sort_by_dif()[0]
        else:
            return None
    
    def __str__ (self):
        
        if not self.climbing_list:
            f"[No Routes Added!]"

        hardest = self.hardest_route()
        
        if hardest:
            return f"{self.name}, {len(self.climbing_list)} routes, hardest {self.hardest_route().grade}"
        else:
            return f"{self.name}, 0 routes, hardest N/A"
        
    

    
class ClimbingApp:
    def __init__ (self, list_areas:list):
        self.list_areas = list_areas

    def search_area(self, area_search_name:str):
        for area in self.list_areas:
            if area.name.lower() == area_search_name:
                selected_area = area
                return selected_area

    def help_1(self):
        print()
        print("(A): Choose Route Area")
        print("(B): Exit")

    def help_2(self):
        print()
        print("----AREA OPTIONS----")
        print()
        print("(1):Olhava")
        print("(2):Nummi")
        print("(3):Nalkkila slab")
        print("(0): Return")

    def help_3(self):
        print()
        print("(1): Show Routes")
        print("(2): Hardest Route")
        print("(0): Return")

    def execute(self):
        
        while True:
            self.help_1()

            try:
                op_1 = input("Option:").lower()

                match op_1:
                    
                    case 'a':
                        print("\n")

                        while True:

                            self.help_2()
                            
                            try:

                                op_2 = int(input("Option:"))
                                selected_area = None
                                print()

                                match op_2:

                                    case 0:
                                        break
                                    case 1:
                                        selected_area = self.search_area("olhava")
                                    case 2:
                                        selected_area = self.search_area("nummi")
                                    case 3:
                                        selected_area = self.search_area("nalkkila slab")
                                    case _:
                                        print("Type a Valid Area!")
                                        print()
                                        continue
                                                    

                                if selected_area:
                                    while True:
                                        self.help_3()
                                        try:
                                            op_3 = int(input("Option:"))
                                            match op_3:

                                                case 0:
                                                    break

                                                case 1:
                                                    print()
                                                    print("----ROUTE OPTIONS----")
                                                    print()
                                                    selected_area.routes()
                                                    print()
                                                    continue

                                                case 2:
                                                    print()
                                                    print("----HARDEST ROUTE----")
                                                    print()
                                                    print(f"{selected_area.hardest_route()}")
                                                    print()
                                                    continue
                                        
                                        except ValueError:
                                            print("[Type a Number!]")
                                            print()
                                else:
                                    print()
                                    print("[NO AREA ADDED!]")
                                    print()
                                    break

                            except ValueError:
                                print("[Type a Valid Number!]")
                                print()
                                continue

                    case 'b':
                        break

                    case _:
                        print("[Please, Type a Valid Option!]")
                        print()
            except ValueError:
                print("[Type a Valid Letter!]")
                print()


#TITLE

title = "CLIMBING APP"
print("-"*len(title))
print(title)
print("-"*len(title))

#EXECUTE

ca1 = ClimbingArea("Olhava")
ca1.add_route(ClimbingRoute("Edge", 38, "6A+"))
ca1.add_route(ClimbingRoute("Great cut", 36, "6B"))
ca1.add_route(ClimbingRoute("Swedish route", 42, "5+"))

ca2 = ClimbingArea("Nummi")
ca2.add_route(ClimbingRoute("Synchro", 14, "8C+"))

ca3 = ClimbingArea("Nalkkila slab")
ca3.add_route(ClimbingRoute("Small steps", 12, "6A+"))
ca3.add_route(ClimbingRoute("Smooth operator", 11, "7A"))
ca3.add_route(ClimbingRoute("Piggy not likey", 12 , "6B+"))
ca3.add_route(ClimbingRoute("Orchard", 8, "6A"))

list_areas = [ca1,ca2,ca3]

app = ClimbingApp(list_areas)
app.execute()
print()
print("Shutting Down...")
print("Goodbye!")