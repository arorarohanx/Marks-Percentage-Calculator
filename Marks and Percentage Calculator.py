import time
print("Percentage & Marks Calculator")
time.sleep(3)
print("In this Programme you have to just upload your Total Marks of each subject here out of 100 ")
time.sleep(3)
print("Loading..")
time.sleep(2)
a = int(input("Enter your Maths Marks :- "))
b = int(input("Enter your Science Marks :- "))
c = int(input("Enter your SST Marks :- "))
d = int(input("Enter your English Marks :- "))
e = int(input("Enter your Hindi/French/German/(any other language) Marks :- "))
time.sleep(2)
print("Calculating...")
time.sleep(2)
total_marks = a+b+c+d+e
percentage = float(total_marks/500 * 100)
print("Your Total Marks is :-", total_marks)
time.sleep(2)
print("Your Total Percentage including all Subject Marks is :-", percentage, "%" )
time.sleep(5)
exit()