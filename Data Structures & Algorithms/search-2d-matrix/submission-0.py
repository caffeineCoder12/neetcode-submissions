class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        for r in range(row):
            if matrix[r][col-1] < target:
                print(matrix[r][col-1] ,"<", target)
                continue
            elif matrix[r][col-1] > target:
                print(matrix[r][col-1] ,">", target)
                print("r=",r,"col-1=",col)
                for i in range(col-1):
                    print("for stmt -", matrix[r][i], "and target" ,target)
                    if matrix[r][i] == target:
                        return True
            else:
                return True
        return False