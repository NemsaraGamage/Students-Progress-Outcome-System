# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1809916        
  
# Date: 10 / 12 / 2020


def outcome():
    #if the total is valid it will go to displaying the program
        if total == 120:
            # if the credit is equal then the output will be progress.
            if p_credit == 120:
                print("Progress")
            # if the p_credit is equal to 100 then there only 2 possible outcomes
            elif p_credit == 100:
                    if p_credit == 100 and defer == 20 or fail == 20:
                            print("Progress(module trailer)")
            # if the fail is greater than 80 then the outocm eis fail.
            elif fail >= 80:
                print('Exclude')
            else:
                # if none of the conditions is true then the program will automatically display
                print('Do not progress(module retriver)')
                
        #if not it will display that the total dose not match, wich means that the total is inoccrect.                         
        elif total != 120:
            print("Total Incorrect")
        print()
        
    

while True:

            #using a try and except fucntion to insure that the user dosent enter a sting.
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
                
                # callin the uder defined function    
                outcome()
                
        except ValueError:
                print("Requires a vaild integer")
                print()
                continue
        break
                
