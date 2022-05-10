# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1809916        
  
# Date: 10 / 12 / 2020


#variables
p_count = 0
mt_count = 0
mr_count = 0
e_count = 0

count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0

def outcome():
    global p_count 
    global mt_count 
    global mr_count 
    global e_count
    
    #if the total is valid it will go to displaying the program
    if total == 120:
        # if the credit is equal then the output will be progress.
        if p_credit == 120:
            print("Progress")
            p_count = p_count + 1
        # if the p_credit is equal to 100 then there only 2 possible outcomes
        elif p_credit == 100:
            if p_credit == 100 and defer == 20 or fail == 20:
                print("Progress(module trailer)")
                mt_count = mt_count + 1
        # if the fail is greater than 80 then the outocm eis fail.
        elif fail >= 80:
            print('Exclude')
            e_count = e_count + 1
        else:
            # if none of the conditions is true then the program will automatically display
            print('Do not progress(module retriver)')
            mr_count = mr_count + 1
            
    #if not it will display that the total dose not mathc wich means that the toal is inoccrect.                         
    elif total != 120:
        print("Total Incorrect")
    print()

def histrogram(outcome):
    #assigning the variable of each count to an alias.
    p = int(p_count) 
    mt = int(mt_count) 
    mr = int(mr_count) 
    e = int(e_count)
    
    a = int(count_1)
    b = int(count_2)
    c = int(count_3)
    d = int(count_4)
    
    print("Horizontal histogram")
    print()
   # printing the histogram for progress and displaying the count in "*". 
    print('progress',p,':', end = "")       
    while a < p:
        print("*",end = "")
        a = a + 1
    print()
   # printing the histogram for progress(module trailer) and displaying the count in "*". 
    print('Trailer ',mt,':',end = "")       
    while b < mt:
        print("*",end = "")
        b = b + 1
    print()
    # printing the histogram for progress(module retriver) and displaying the count in "*".  
    print('Retriver',mr,':',end = "")
    while c < mr:       
        print("*",end = "")
        c = c + 1
    print()
    # printing the histogram for Exclude and displaying the count in "*". 
    print('Exclude ',e,':',end = "")
    while d < e:
        print("*",end = "")
        d = d + 1
    print()
   # adding the total of the all the outputs to give the number of outcome.
    total_count = p + mt + mr + e
    print(total_count,"outcomes in total")
    
    
while True:
    #using a try and except fucntion to insure that the user dosnt enter a sting.
    try:
        #the range in a tuple so no changes can occur to the fixed range.
        order = (0,20,40,60,80,100,120)
        
        p_credit = int(input("Please enter your credits at pass: "))
        #using an if not conditon to check that if the number that was given form the user is within the range.
        if p_credit not in order:
            print("Out of Range")
            print()
            continue
            
        defer = int(input("Please enter your credit at defer: "))
        if defer not in order:
            print("Out of Range")
            print()
            continue
        
        fail = int(input("Please enter your credit at fail: "))
        if fail not in order:
            print("Out of Range")
            print()
            continue
        
        #Getting the total of all three inputs.
        total = p_credit + defer + fail
        
        # calling the user defined function   
        outcome()
        
    except ValueError:
        print("Requires a vaild integer")
        print()


    option = str(input('''Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: '''))


    if option == 'y':
        print()
        continue
    elif option == 'q':
        print()
        break
    else:
        print("Invalid option")
        print()
        break
   
#calling the hsitrogram function
histrogram(outcome)
        
    

        

        
        

        

        
        
        
