# array is the collection of 
# array==list
# array of list==nested list
# array of set==[{}]
# array of tuple==[()]

import os
def clear():
    os.system("clear")






employ_management=[]




def add_employ():
    clear()
    
    employee_id = int(input("Enter The Employee ID:"))
    name=input("Enter The Name Of The Employee:")
    age=int(input("Enter The Age Of The Employee:"))
    position=input("Enter The Position Of The Employee:")
    
    
    
    employee={
        "employee_id":employee_id,
        "name":name,
        "age":age,
        "position":position
        }
    
    

    employ_management.append(employee)
    for i in employ_management:
        print("employee added succesffully")
    
    
    
    
    
def display_employ():
    clear()
    for i in employ_management:
            print("the employee details are:")
            print(f"employee ID:{i['employee_id']}   \n employee name:{i['name']}\n employee age:{i['age']}\n employee position:{i['position']}\n")
            
    
      
def remove_employ():
    clear() 

    rememp=int(input("Enter The ID To Remove:"))
    for i in employ_management:
        if i['employee_id']==rememp:
            employ_management.remove(i)
            print("Employee Removed Successfully!")
        else:
            print("Employee Not Found")
        

    
    
    
    
def search_employ():
    clear() 

    searchkey=int(input("Enter The ID You Wanted To Searched:"))
    for i in employ_management:
        if i['employee_id']==searchkey:
            print(f"employ found --\n name:{i['name']}\n age:{i['age']}\n position:{i['position']}\n")

        else:
            print("Employee Not Found")




def main():
    while True:
        print(" Welcome To Employ Management System")
        print("1.Add Employ")
        print("2.Display Employ")
        print("3.Remove Contact")
        print("4.Search Employ")
        print("5.Quit")
        
        
        choice=input("Please Enter Your Choice:")
        
        if choice=="1":
            add_employ()
        elif choice=="2":
            display_employ()
        elif choice=="3":
            remove_employ()
        elif choice=="4":
            search_employ()
        elif choice=="5":
            clear()
            print("Have A Nice Day!")
            break
        else:
            print("Error Found,Enter Again:")
        
    

    
if __name__=="__main__":
    main()


















