class Solution:

    def binary_search(self, row: List[int], target:int )-> bool:
        right = len(row) - 1
        left = 0
        mid = right//2
        while right>=left:
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid+1
                mid = left + (right-left)//2
            elif row[mid] > target:
                right = mid-1
                mid = right//2
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        best_row = 0
        for i in range(row-1, -1,-1):
            if matrix[i][0] == target:
                return True
            elif matrix[i][0] > target:
                best_row = i -1
            elif matrix[i][0] < target:
                best_row = i
                break
            else:
                continue
        if self.binary_search(matrix[best_row], target) == True:
            return True
        else:
            return False


        