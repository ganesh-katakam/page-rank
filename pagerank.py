#Program To find Page Rank of a given web graph usng Matrix Multiplication
#Implemented in Python by Ganesh Katakam

#Function to display given matrix
def display(matrix, nodes):
  for i in range(nodes):
    for j in range(nodes):
      print("{: >10}".format(matrix[i][j]), end = " ")
    print("\n")

#Function to update the existing adjacency matrix
def updatedAdjacencyMatrix(adjacency_matrix,nodes,row_sum_vector):
  updated_matrix = []
  for i in range(nodes):
    temp = []
    for j in range(nodes):
      temp.append(round(adjacency_matrix[i][j]/row_sum_vector[i],2))
    updated_matrix.append(mat)
  return updated_matrix

#Function to retrieve transpose of a given matrix
def matrixTranspose(updatedMatrix,nodes):
  transpose_matrix =[[updatedMatrix[j][i] for j in range(nodes)] for i in range(nodes)]
  return transpose_matrix

#Function to perform matrix multiplication
def multiplyMatrix(transposeMatrix,column_vector,nodes):
  output_vector = []
  prev_check = False
  for i in range(nodes):
    s = 0
    for j in range(nodes):
      s+=(round(transposeMatrix[i][j]*column_vector[j],2))
    output_vector.append(s)
  if (column_vector == output_vector):
    prev_check = True
  return output_vector,prev_check

#Function to calculate Page Rank
def calculatePageRank(transposeMatrix, column_vector, nodes):
  k = 1
  while (True):
    data,check = multiplyMatrix(transposeMatrix, column_vector, nodes)
    print("Iteration :{} \n Previous Column Vector :{} and Current Column Vector :{}".format(k,column_vector,data))
    column_vector = data
    page_rank = {}
    if (check):
      count = 65
      for element in data:
        page_rank[chr(count)] = element
        count = count + 1
      print("\nOutput:\n Final Iteration K : {} and Final Column Vector:{}".format(k,data))
      page_rank = sorted(page_rank.items(), key=lambda x: x[1], reverse=True)
      break
    k = k + 1
  print("\nPage Ranking Order:\n")
  for data in page_rank:
    print("{} {}".format(data[0],data[1]))


#Input va;ue for total number of Nodes(Pages)
nodes = int(input("\nEnter Number of Nodes : "))

#Initializing variables
adjacency_matrix = []
row_sum_vector = []


#Input for filling the adjacency matrix
print("\nEnter either 1 if an edge is there between nodes or 0 if there is no edge : ")
for element in range(nodes):
  row = []
  for each in range(nodes):
    while (True):
      val = int(input("Edge ({},{}) = ".format(element,each)))
      if (val == 0 or val == 1):
        row.append(val)
        break
      else:
        print("Sorry, Please enter either 0 or 1")
  adjacency_matrix.append(row)
  row_sum_vector.append(sum(row))

#Input value for the damping factor
damping_factor = float(input("\nEnter damping factor : "))

#Initializing Co;umn Vector from damping factor
column_vector = [damping_factor for port in range(nodes)]

#Display Adjacency Matrix
print("\nAdjacency Matrix is\n")
display(adjacency_matrix,nodes)

#Display Updated Adjacency Matrix
updatedMatrix = updatedAdjacencyMatrix(adjacency_matrix,nodes,row_sum_vector)
print("\nUpdated Adjacency Matrix\n")
display(updatedMatrix,nodes)

#Display Transpose of Updated Adjacency Matrix
transposeMatrix = matrixTranspose(updatedMatrix,nodes)
print("\nMatrix Transpose of Updated Adjacency Matrix\n")
display(transposeMatrix,nodes)

#Display Column Vector
print("\nColumn Vector\n")
for ele in column_vector:
  print("{: >10}".format(ele))
print("\n")

#Calculate Page Rank
calculatePageRank(transposeMatrix, column_vector, nodes)







