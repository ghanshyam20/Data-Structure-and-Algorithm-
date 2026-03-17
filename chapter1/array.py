# # # this is array

# # from array import *

# # val=array('i', [1,2,3,4,5,6,7,8,9])

# # # # 0 will include but 6 will not included here
# # # for i in range(0,len(val)):
# # #     print(val[i], end=" ")

# # # print('\n')
# # # for x in val:
# # #     print(x, end=" ")


# # # print("\n")
# # # print(val.typecode)



# # # val.reverse()
# # # for i in range(0,len(val)):
# # #     print(val[i], end=" ")


# # # val.insert(1,50)
# # # val.append(100) # in append it will go into last of the array

# # # val[2]=200 # to override the value in the index



# # copyArray=array(val.typecode,(x*2 for x in val))

# # # copyArray.pop(3)
# # # copyArray.remove(18) # for a particular element to remove

# # # to slice an array , in slicing starting index elemtn will inlciude for end will not 

# # a=val[2 : 5]
# # b=val[2:-3]  # here in another example starting of index 2 will incloude and the last 3 elemetns will not include
# # c=val[::-1] # this will reverse 

# # print(a)
# # print(b)
# # print(c)

# # for i in range(0, len(a)):
# #     print(a[i], end=" ")


# # ask to user for number of inputs for making an array and then also ask to enter the value for it




# # from array import *

# # arr=array('i',[])

# # n=int(input("enter the number of input:"))


# # for i in range(0,n):
# #     arr.append(int(input("enter the values for aray:")))

# # for x in arr:
# #     print(x, end=" ")



# # from array import*

# # arr=array('i', [12,23,45,234,134,235])

# # i=arr.index(45)  # it will print the index of 45
# # print(i)



# # to create multidimensional array


# # import numpy as np



# # arr=np.array([1,2,3,4])



# # print(arr)

# students = {}  # "name": grade

# while True:
#     print("\n--- Student Grades Menu ---")
#     print("1. Add or update a grade")
#     print("2. Search student grade")
#     print("3. Print all students and grades")
#     print("0. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         name = input("Enter student name: ")
#         grade = input("Enter grade: ")
#         students[name] = grade  # add or update
#         print(f"Saved: {name}: {grade}")

#     elif choice == 2:
#         name = input("Enter student name to search: ")
#         if name in students:
#             print(f"{name}: {students[name]}")
#         else:
#             print("Student not found.")

#     elif choice == 3:
#         if not students:
#             print("No students in the list.")
#         else:
#             for name, grade in students.items():
#                 print(f"{name}: {grade}")

#     elif choice == 0:
#         print("Exiting...")
#         break

#     else:
#         print("Invalid choice, try again.")



# students={}


# while True:
#       print("\n--- Student Grades Menu ---")
#       print("1. Add or update a grade")
#       print("2. Search student grade")
#       print("3. Print all students and grades")
#       print("0. Exit")




#       choice=int(input("enter your choice"))

#       if choice==1:
#             name=input("enter name of student:")
#             grade=int(input("enter grade"))

#             students[name]=grade








       
















