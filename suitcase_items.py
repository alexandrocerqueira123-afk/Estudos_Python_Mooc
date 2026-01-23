class Item:
    def __init__ (self, name: str, weight: int):
        self._name = name
        self._weight = weight

    @property
    def name(self):
        return self._name
    
    @property
    def weight(self):
        return self._weight

class Suitcase:
    def __init__ (self, max_weight):
        self._max_weight = max_weight
        self._suitcase = []
        self._current_weight = 0

    @property
    def current_weight(self):
        return self._current_weight

            

    def add_item (self, item: Item):
        if self._current_weight + item.weight > self._max_weight:
            raise ValueError("Maximum Weight Exceeded!")
        self._suitcase.append(item)
        self._current_weight = self._current_weight + item.weight


    def __str__ (self):
        if len(self._suitcase) == 1:
            return f"{len(self._suitcase)} item ({self._current_weight} kg)"
        
        return f"{len(self._suitcase)} items ({self._current_weight} kg)"
    
    def print_items(self):
        for element in self._suitcase:
            print(f"{element.name}: ({element.weight} kg)\n")

    def heaviest_item(self):
        if not self._suitcase:
            return "The Suitcase is Empty!"

        h_item = self._suitcase[0]

        for item in self._suitcase:
            if item.weight > h_item.weight:
                h_item = item
        return f"The Heaviest Item is: {h_item.name}: ({h_item.weight} kg)"

    def remove_item(self, item_name):
        for item in self._suitcase:
            if item.name.lower() == item_name.lower():
                self._current_weight = self._current_weight - item.weight
                self._suitcase.remove(item)
                return True
        return False

##PROGRAM

suitcase = Suitcase(10)

#Start
text_1 = "SUITCASE INTERFACE"
print("-"*len(text_1))
print(text_1)
print("-"*len(text_1))
print("\n\n")

#Menu

while True:
    print("__Menu Interface__")
    print("\n(1): Add Item")
    print("(2): Total Items/Weight")
    print("(3): List of Items")
    print("(4): Heaviest Item")
    print("(5): Remove Item")
    print("(0): Exit\n")
    try:
        op = int(input("Option:"))

        match op:

            case 0:
                break

            case 1:
                print()
                name = input("Name:")
                weight = int(input("Weight:"))
                new_item = Item(name,weight)

                try:
                    suitcase.add_item(new_item)
                    print("Item Saved!\n")
                    print("\n")
                    print()
                    continue

                except ValueError as erro:
                    print(f"Attention: {erro}")

            case 2:
                print()
                print(suitcase)
                print("\n")
                continue

            case 3:
                print()
                suitcase.print_items()
                print("\n")
                continue

            case 4:
                print()
                print(suitcase.heaviest_item())
                print("\n")
                continue

            case 5:
                item_name = input("Type Item to Remove:")
                if suitcase.remove_item(item_name):
                    print("Item Remove!\n")
                else:
                    print("Item Doesn't Exist!")
                continue

            case _:
                print("Invalid Number!")
                continue
    except ValueError:
        print("Write Numbers Only!")

print("Goodbye!")          


        

