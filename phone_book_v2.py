           
class PhoneBook:
    def __init__(self):
        self.__persons = {}
        
    def add_number(self, name: str, number: str):    
        p= Person(name)
        if not name in self.__persons:
            
            self.__persons[name]= p
            
        self.__persons[name].add_number(number)
        
    def add_address(self,name:str, address:str):
        p= Person(name)
        if not name in self.__persons:
            self.__persons[name]= p
        self.__persons[name].add_address(address)

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None,None
        return self.__persons[name]._numbers,self.__persons[name]._address

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_entry(name)[0]
        address= self.__phonebook.get_entry(name)[1]
        if numbers == [] or numbers==None:
            print("number unknown") 
        
        else:
            for number in numbers:
                print(number) 
                
        if address==None:
            print("address unknown")

        else:
            print(address)
    def add_address(self):
        name= input("name: ")     
        address= input("address: ") 
        self.__phonebook.add_address(name, address)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command=="3":
                self.add_address()
            else:
                self.help()

class Person:
    def __init__(self,name:str) :
        self.__name=name
        self._numbers=[]
        self._address=None
    def name(self):
        return self.__name
    def numbers(self):
        return self._numbers
    def address(self):
        return self._address
    def add_number(self,number:str):
        self._numbers.append(number)
    def add_address(self,address:str):
        self._address=address

# when testing, no code should be outside application except the following:
x=PhoneBookApplication()
x.execute()
