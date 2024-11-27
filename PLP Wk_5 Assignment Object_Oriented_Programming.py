class warship:
    def __init__(self, category, name):
        self.category = category
        self.__name = name
        
class operational(warship):
    def __init__(self, category, name):
     super().__init__(category, name)
    
    def print_categories(self):
        print("Number of categories:", 2)
  
warship1 = operational("Aircraft Carrier", "HMS Indomitable")
warship2 = operational("Battleship", "HMS Vanguard")   
       
warship1.print_categories()
warship2.print_categories()