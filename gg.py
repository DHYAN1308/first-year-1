print("hi me dhyan")
your_name = input("Enter your name: ")
your_age = input("enter your age: ")
your_marks = input("enter your marks: ")            
total_marks = 100       
your_percentage = (float(your_marks) / total_marks) * 100
print("note : your percentage required for admission is 95%")
if your_percentage >= 95:                             
       print("you are eligible for admssion")
else:
       print("sorry you are not elegible for admission")