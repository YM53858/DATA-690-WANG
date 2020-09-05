import statistics # importing this library for calculating Standard deviation,Variance and Mean
print("Please Enter 10 integer numbers")
num_list=[]
i=True
c=0
while i: # This while loop stops when the user enters all 10 integers
    try:
        num = int(input("Enter a integer number: "))
    except ValueError:
        print("Not an integer! Please Try again.")
    else:
        c+=1
        num_list.append(num)
    if c==10:
        i=False
        print("Entered integer numbers are: ",num_list)
        print("Standard Deviation of Entered list of numbers is % s" %(statistics.stdev(num_list))) 
        print("Variance of Entered list of numbers is % s" %(statistics.variance(num_list)))
        print("Mean of Entered list of numbers is",statistics.mean(num_list))
        print("Minimum of Entered list of numbers is",min(num_list))
        print("Maximum of Entered list of numbers is",max(num_list))
        print("Range of Entered list of numbers is",(max(num_list)-min(num_list)))