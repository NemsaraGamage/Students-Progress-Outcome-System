# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1809916         
  
# Date: 10 / 12 / 2020

#Variables
p_credit = int(input("Please enter your credits at pass: "))
defer = int(input("Please enter your credit at defer: "))
fail = int(input("Please enter your credit at fail: "))

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
# if none of the conditions is true then the program will automatically display.
else:
    print('Do not progress(module retriver)')

