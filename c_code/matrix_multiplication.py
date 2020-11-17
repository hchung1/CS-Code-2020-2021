class math_class():
    def matmul(self, matrix1, matrix2): # 2D Matrix Multiplication
        if len(matrix1[0]) == len(matrix2):
            temp=[]
            matrix2=self.transpose(matrix2)
            counter=0
            for i in matrix1:
                temp.append([])
                for j in matrix2:
                    temp[counter].append(sum([i[x]*j[x] for x in range(len(i))]))
            counter +=1
            return temp
        else:
            print ("Error: Dimension mismatch, K-size is different. (n?,k),(k,m?)->(n?,m?)")
    def transpose(self, data): # 2D Transpose
        try:
            temp = []
            for i in range(len(data[0])):
                temp.append([])
                for j in range(len(data)):
                    temp[i].append(data[j][i])
            return temp
        except:
            print ("Error: %s is not a 2D array." % str(data))
            return data

