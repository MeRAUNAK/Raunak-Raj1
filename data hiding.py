class student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def display_info(self):
        print(f"Name: {self.__name},Age:{self.__age}")

    def get_name(self):
        return self.__name
    
    def set_name(self,new_name):
        if len(new_name) > 0:
            self.__name = new_name
        else:
            print("Invalid name!")


#Creating an instance of the student class
student1=student("Raunak",20)

#Accessing public method to display information
student1.display_info()

#Accessing private attribute using getter method
print(f"student name:{student1.get_name()}")

#Modifying private attribute using setter method
student1.set_name("Alice")

#Displaying updated information
student1.display_info()
            