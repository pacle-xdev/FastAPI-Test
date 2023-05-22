import numpy as np

def get_list():
    a = input("Enter list without brackets and seperated by commas")
    print(a)
    c = a.split(",")
    print(c)
    b = [int(x) for x in c]
    print(b)
    return b
X = []
#place your list here
input_matrix= [11, 12.21, 13.42, 12.74, 15.64, 18.43, 20.43, 18.3,19.2,11.65]
#or uncomment this and type it:
#input_matrix = get_list()
n=len(input_matrix)
for i in range(n):
    X.append([])
    for j in range(n):
        X[i].append((i+1)**j)
#we are assumin the relationship is like this:
#for the first number 11 = a_0 + a_1 * 1^1 + a_2 *1^2 + a_3 * 1^3 +..+a_n * 1^n
# for the second number 12.21 = a_0 + a_1*2^1 + a_2 * 2^2 + a_3 * 2^3 +..+a_n* 2^n
#and in general for the x number y= sigma(a_i * x^i)
# now we find tha a_0 to a_n 
mat_x = np.array(X)


mat_y = np.array(input_matrix)[np.newaxis]

mat_a = np.linalg.solve(mat_x,mat_y.T)
#mat_a has a_0 to a_n
print('a_i is: ', mat_a.T)

mat_1 = np.matmul(mat_x,mat_a)
#mat_1 should be the same as the input list with a little error
print('Your numbers are: ', mat_1.T)
X_2 =[]
for i in range(n):
    X_2.append([])
    for j in range(n):
        X_2[i].append((i+1+30)**j) #we added 30 to i

mat_x2 = np.array(X_2)
mat_new = np.matmul(mat_x2,mat_a)
#mat new has 30 new numbers in it's last 30 entries
#The code will not work if the number of inputs are less than 170
print('new numbers are:', mat_new.T[0][-30:])
    