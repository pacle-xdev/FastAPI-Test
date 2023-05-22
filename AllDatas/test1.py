import scipy
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
#input_matrix= [11, 12.21, 13.42, 12.74, 15.64, 18.43, 20.43, 18.3]
#or uncomment this and type it:
#input_matrix = get_list()
n=len(input_matrix)
for i in range(n):
    X.append([])
    for j in range(n):
        X[i].append((i+1)**j)
mat_x = np.array(X)
x_inverse = np.linalg.inv(mat_x)
print('X= ', mat_x)
print(x_inverse)
mat_y = np.array(input_matrix)
mat_a = np.matmul(mat_y , x_inverse)
print('your numbers were: ', mat_a)

mat_1 = np.matmul(mat_a,mat_x)
print(mat_1)
X_2 =[]
for i in range(n):
    X_2.append([])
    for j in range(n):
        X_2[i].append((i+1+30)**j) #we added 30 to i

mat_2 = np.array(X_2)
mat_new = np.matmul(mat_a,mat_2)
print('new numbers are:', mat_new)
    