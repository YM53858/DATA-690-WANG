print("Please Enter 10 integer numbers")

num_list=[] # For storing the entered integer numbers.
i=True
c=0 # counter variable for storing the count of integers entered by user.

while i: # This while loop stops when the user enters all 10 integers
    try:
        num = int(input("Enter a integer number: "))
    except ValueError:
        print("Not an integer! Try again.")
    else:
        c+=1
        num_list.append(num)
    
    if c==10:
        i=False

        mean = sum(num_list) / len(num_list) # calculating mean
        
        variance = sum((i - mean) ** 2 for i in num_list) / len(num_list) # calculating variance using a list comprehension
        
        std_dev = variance**0.5 # calculating standard deviation    
        
        print("Entered integer numbers are: ",num_list)
        print("Minimum of Entered list of numbers is",min(num_list))
        print("Maximum of Entered list of numbers is",max(num_list))
        print("Range of Entered list of numbers is",(max(num_list)-min(num_list)))
        print("Standard Deviation of Entered list of numbers is",std_dev) 
        print("Variance of Entered list of numbers is",variance)
        print("Mean of Entered list of numbers is",mean)