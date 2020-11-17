# Checking Library
import numpy as np

class math_class():
    def transpose(self, data):
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


# Variables
test1 = [[1,2,3,4,5,6]] # Test 1, 1x6 Vector
test2 = [[1,2],[3,4]] # Test 2, 2x2 Matrix

# Call Class
tester = math_class()

# Run Transpose Function
result1 = tester.transpose(test1) # Result Answer, 6x1 Vector
result2 = tester.transpose(test2) # Result Answer, 2x2 Matrix

# Create Checking Model (Numpy)
check1 = np.array(test1).T # Check Answer, 6x1 Vector
check2 = np.array(test2).T # Check Answer, 2x2 Matrix

# Output Result and Check
print ("My Result")
print (result1)
print ("\nNumpy Result")
print (check1)
print ("\n\nMy Result")
print (result2)
print ("\nNumpy Result")
print (check2)
