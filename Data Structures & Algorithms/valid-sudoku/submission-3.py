class Solution:
    def checkforduplicates (self, row:List) -> bool:
        frequency={}
        for i in row:
            if i in frequency:
                frequency[i]+=1
                if frequency[i] == 2 and i!= '.':
                    return True #Returns True if there are duplicates 

            else:
                frequency[i] =1 
        return False #Return False if there are no duplicates
        
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Row Check
        for i in board:
            if (self.checkforduplicates(i)) == True:
                print("Duplicate row"+str(i))
                return False #Definitely not a valid sudoku board
        #Column Check
        for i in range(9):
            checking_array=[0]*9
            for j in range(9):
                checking_array[j]= (board[j][i])
            if (self.checkforduplicates(checking_array)) == True:
                print("Duplicate Column"+ str(checking_array))
                return False

        #Square Check:
        for x in range(3):
            row_offset = x*3
            print("Row"+ str(row_offset))
            for i in range(3): #This loop is for entire row
                col_offset= i*3
                print("col"+ str(col_offset))
                
                checking_arr=[0]*9 #To store the values of what to calculate
                increment=0
                for j in range(row_offset,(row_offset+3)): #Obtain the correct rows per square
                    for t in range(col_offset,col_offset+3):
                        checking_arr[increment] = board[j][t]
                        increment+=1
                if (self.checkforduplicates(checking_arr)) == True:
                    print("Duplicate square" + str(checking_arr))
                    return False
        
        return True
