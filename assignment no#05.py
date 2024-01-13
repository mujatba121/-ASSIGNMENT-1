#creat an empty list
pattern_list=[]
#genrate a pattern with multiplicative values
for i in range(1,6):
    for j in range(1,4):
        value=i*j
pattern_list.append(value)

#remove dublicate manually
final_list=[]
for num in pattern_list:
    if num not in final_list:
        final_list.append(num)
#print the final_list
print(final_list)



#q no 2
#two nested listsrepresenting matrices
matrix1=[
    [9,8,7],
    [6,5,4],
    [3,2,1]
]
matrix2=[
    [1,2,3]
    [4,5,6]
    [7,8,9]
]
#initialize an empty result matrix
result=[]
#perform matrix addition
for i in range(len(matrix1)):
    row=[]
    for j in range(len(matrix1[0])):
        row.append(matrix1[i]
[j] + matrix2[i][j])
    result.append(row)
#print the result matrix(matrix addition)
    for row in result:
        print(row)
