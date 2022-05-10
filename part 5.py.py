# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1809916        
  
# Date: 10 / 12 / 2020

#Variables
#Creating the list to set the inputs
credit_list = [
    [120,0,0],
    [100,20,0],
    [100,0,20],
    [80,20,20],
    [60,40,20],
    [40,40,40],
    [20,40,60],
    [20,20,80],
    [20,0,100],
    [0,0,120]
]

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
    
    while True:
        # assigning the list to a alias where the sublist will be assigned.
        a = credit_list[0][0]
        b = credit_list[0][1]
        c = credit_list[0][2]
        if a == 120:
            print("Progress")
            p_count = p_count + 1
        elif a == 100:
            if a == 100 and b == 20 or c == 20:
                print("Progress(module trailer)")
                mt_count = mt_count + 1
        elif c >= 80:
            print('Exclude')
            e_count = e_count + 1
        else:
            print('Do not progress(module retriver)')
            mr_count = mr_count + 1
        
#---------------------------------------------------------
        a = credit_list[1][0]
        b = credit_list[1][1]
        c = credit_list[1][2]
        if a == 120:
            print("Progress")
            p_count = p_count + 1
        elif a == 100:
            if a == 100 and b == 20 or c == 20:
                print("Progress(module trailer)")
                mt_count = mt_count + 1
        elif c >= 80:
            print('Exclude')
            e_count = e_count + 1
        else:
            print('Do not progress(module retriver)')
            mr_count = mr_count + 1
#---------------------------------------------------------
        a = credit_list[2][0]
        b = credit_list[2][1]
        c = credit_list[2][2]
        if a == 120:
            print("Progress")
            p_count = p_count + 1
        elif a == 100:
            if a == 100 and b == 20 or c == 20:
                print("Progress(module trailer)")
                mt_count = mt_count + 1
        elif c >= 80:
            print('Exclude')
            e_count = e_count + 1
        else:
            print('Do not progress(module retriver)')
            mr_count = mr_count + 1
#---------------------------------------------------------
        a = credit_list[3][0]
        b = credit_list[3][1]
        c = credit_list[3][2]
        if a == 120:
            print("Progress")
            p_count = p_count + 1
        elif a == 100:
            if a == 100 and b == 20 or c == 20:
                print("Progress(module trailer)")
                mt_count = mt_count + 1
        elif c >= 80:
            print('Exclude')
            e_count = e_count + 1
        else:
            print('Do not progress(module retriver)')
            mr_count = mr_count + 1      
#---------------------------------------------------------
        a = credit_list[4][0]
        b = credit_list[4][1]
        c = credit_list[4][2]
        if a == 120:
            print("Progress")
            p_count = p_count + 1
        elif a == 100:
            if a == 100 and b == 20 or c == 20:
                print("Progress(module trailer)")
                mt_count = mt_count + 1
        elif c >= 80:
            print('Exclude')
            e_count = e_count + 1
        else:
            print('Do not progress(module retriver)')
            mr_count = mr_count + 1      
#---------------------------------------------------------
        a = credit_list[5][0]
        b = credit_list[5][1]
        c = credit_list[5][2]
        if a == 120:
            print("Progress")
            p_count = p_count + 1
        elif a == 100:
            if a == 100 and b == 20 or c == 20:
                print("Progress(module trailer)")
                mt_count = mt_count + 1
        elif c >= 80:
            print('Exclude')
            e_count = e_count + 1
        else:
            print('Do not progress(module retriver)')
            mr_count = mr_count + 1 
#---------------------------------------------------------
        a = credit_list[6][0]
        b = credit_list[6][1]
        c = credit_list[6][2]
        if a == 120:
            print("Progress")
            p_count = p_count + 1
        elif a == 100:
            if a == 100 and b == 20 or c == 20:
                print("Progress(module trailer)")
                mt_count = mt_count + 1
        elif c >= 80:
            print('Exclude')
            e_count = e_count + 1
        else:
            print('Do not progress(module retriver)')
            mr_count = mr_count + 1 
#---------------------------------------------------------
        a = credit_list[7][0]
        b = credit_list[7][1]
        c = credit_list[7][2]
        if a == 120:
            print("Progress")
            p_count = p_count + 1
        elif a == 100:
            if a == 100 and b == 20 or c == 20:
                print("Progress(module trailer)")
                mt_count = mt_count + 1
        elif c >= 80:
            print('Exclude')
            e_count = e_count + 1
        else:
            print('Do not progress(module retriver)')
            mr_count = mr_count + 1 
#---------------------------------------------------------
        a = credit_list[8][0]
        b = credit_list[8][1]
        c = credit_list[8][2]
        if a == 120:
            print("Progress")
            p_count = p_count + 1
        elif a == 100:
            if a == 100 and b == 20 or c == 20:
                print("Progress(module trailer)")
                mt_count = mt_count + 1
        elif c >= 80:
            print('Exclude')
            e_count = e_count + 1
        else:
            print('Do not progress(module retriver)')
            mr_count = mr_count + 1 
#---------------------------------------------------------
        a = credit_list[9][0]
        b = credit_list[9][1]
        c = credit_list[9][2]
        if a == 120:
            print("Progress")
            p_count = p_count + 1
        elif a == 100:
            if a == 100 and b == 20 or c == 20:
                print("Progress(module trailer)")
                mt_count = mt_count + 1
        elif c >= 80:
            print('Exclude')
            e_count = e_count + 1
        else:
            print('Do not progress(module retriver)')
            mr_count = mr_count + 1 
#---------------------------------------------------------
        
        break
       
def histrogram(outcome):
    # #assigning the variable of each count to an alias.
    p = int(p_count) 
    mt = int(mt_count) 
    mr = int(mr_count) 
    e = int(e_count)

    a = count_1
    b = count_2
    c = count_3
    d = count_4
    
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
    total_count = a + b + c + d    
    print(total_count,"outcomes in total")
 
outcome()
print()
histrogram(outcome)
