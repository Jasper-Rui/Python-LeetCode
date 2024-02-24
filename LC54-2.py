class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        length = len(matrix[0])
        height = len(matrix)

        if height == 0 or length == 0:
            return []

        result = [0] * (length * height)
        cycle = height if height < length else length

        start = 0
        index = 0

        if length == 1:
            for i in range(height):
                result[index] = matrix[i][0]
                index += 1
            return result

        while start < cycle:

            if index >= len(result): break
            for i in range(start, length - start):
                result[index] = (matrix[0 + start])[i]
                index += 1

            if index >= len(result): break

            for i in range(start + 1, height - start - 1):
                result[index] = (matrix[i])[length - start - 1]
                index += 1

            if index >= len(result): break

            for i in range(length - start - 1, start - 1, -1):
                result[index] = (matrix[height - start - 1])[i]
                index += 1

            if index >= len(result): break

            for i in range(height - start - 2, start, -1):
                result[index] = (matrix[i])[start]
                index += 1
            start += 1

        return result




