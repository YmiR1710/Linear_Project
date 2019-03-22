class Matrix:

    @staticmethod
    def transpose_matrix(m):
        return map(list, zip(*m))

    @staticmethod
    def get_matrix_minor(m, i, j):
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    def get_matrix_determinant(self, m):
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        determinant = 0
        for c in range(len(m)):
            determinant += ((-1) ** c) * m[0][c] * self.get_matrix_determinant(self.get_matrix_minor(m, 0, c))
        return determinant

    def get_matrix_inverse(self, m):
        for i in m:
            if len(i) != len(m):
                return 0
        determinant = self.get_matrix_determinant(m)
        if len(m) == 2:
            return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                    [-1 * m[1][0] / determinant, m[0][0] / determinant]]
        cofactors = []
        for r in range(len(m)):
            cofactor_row = []
            for c in range(len(m)):
                minor = self.get_matrix_minor(m, r, c)
                cofactor_row.append(((-1) ** (r + c)) * self.get_matrix_determinant(minor))
            cofactors.append(cofactor_row)
        cofactors = self.transpose_matrix(cofactors)
        cofactors = list(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c] / determinant
        return cofactors

    @staticmethod
    def matrix_multiplication(a, b):
        result = []
        result1 = []
        while len(a) > 0:
            d = 0
            a1 = a[:1:]
            while d < len(a1):
                for x in b:
                    for x1 in x:
                        result.append(x1 * a1[0][d])
                    d = d + 1
            a.pop(0)
        result = [result[i:i + len(b[0])] for i in range(0, len(result), len(b[0]))]
        sum = 0
        while len(result) > 0:
            for X in range(len(result[0])):
                for Y in range(len(b)):
                    sum = sum + result[Y][X]
                result1.append(sum)
                sum = 0
            for s in range(len(b)):
                result.pop(0)
        result1 = [result1[i:i + len(b[0])] for i in range(0, len(result1), len(b[0]))]
        return result1

    def equation(self, A, b):
        return self.matrix_multiplication([b], self.get_matrix_inverse(A))
