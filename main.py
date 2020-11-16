# Python Fibonacci Series program #

Number = int(input("\n Please Enter the Range Number:"))

# Initializing First and Second Values of Series we are Declaring three Interger Values #
i =0 # Declaring three Interger Values#
first_Value =0 # Declaring three Interger Values# 
Second_Value =1 # Declaring three Interger Values# 
 
# Find & Displaying Fibonacci Series

while(i < Number): #  loop starts from 0 #
    if (i<=10):
        Next = i
    else:
        Next = first_Value + Second_Value
        first_Value  = Second_Value
        Second_Value = Next
    print(Next)
    i =i+1
