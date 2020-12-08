import numpy as np


def determinant_recursive(A, total=0):
    indices = list(range(len(A)))

    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val

    for fc in indices:
        As = A[:]
        As = As[1:]
        height = len(As)

        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc + 1:]

        sign = (-1) ** (fc % 2)
        sub_det = determinant_recursive(As)
        total += sign * A[0][fc] * sub_det

    return total


class Matrix:
    def __init__(self):
        self.play = True

    def loop(self):
        while self.play:
            self.initial()

    def initial(self):
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6: Inverse matrix")
        print("0. Exit")
        user = input("Your choice:")
        if user == "1":
            self.add_mat()
        elif user == "2":
            self.mul_by_con()
        elif user == "3":
            self.multiply()
        elif user == "4":
            self.transpose()
        elif user == "5":
            self.determinant()
        elif user == "6":
            self.inverse()
        else:
            self.exit()

    def add_mat(self):
        user = input("Enter size of first matrix:").split()
        print("Enter first matrix:")
        mat1 = [input().split() for i in range(int(user[0]))]
        user2 = input("Enter size of second matrix:").split()
        print("Enter second matrix:")
        mat2 = [input().split() for i in range(int(user2[0]))]

        if user == user2:
            final_matrix = [[float(mat1[i][j]) + float(mat2[i][j]) if "." in mat1[i][j] or "." in mat2[i][j] else int(
                mat1[i][j]) + int(mat2[i][j]) for j in range(int(user[1]))] for i in range(int(user[0]))]
            print("The result is:")
            for i in final_matrix:
                print(*i)
        else:
            print("This operation cannot be performed")
        print()

        return self.initial()

    def mul_by_con(self):
        user = input("Enter size of matrix:").split()
        print("Enter matrix:")
        mat = [input().split() for i in range(int(user[0]))]
        scalar = input("Enter constant:")
        matrix = [[float(mat[i][j]) * float(scalar) if "." in mat[i][j] or "." in scalar else int(
            mat[i][j]) * int(scalar) for j in range(int(user[1]))] for i in range(int(user[0]))]
        print("The result is:")
        for i in matrix:
            print(*i)
        print()
        return self.initial()

    def multiply(self):
        user = input("Enter size of first matrix:").split()
        print("Enter first matrix:")
        matA = [input().split() for i in range(int(user[0]))]
        user2 = input("Enter size of second matrix:").split()
        print("Enter second matrix:")
        matB = [input().split() for i in range(int(user2[0]))]
        # user = ["1", "3"]
        # matA = [["5", "5", "10"]]
        # user2 = ["3", "4"]
        # matB = [["5", "4", "6", "5"], ["7", "5", "3", "6"], ["15", "20", "25", "20"]]
        if user[1] == user2[0]:
            final = []
            try:
                for i in range(int(user[1])):  # picks list default user[1]
                    temp = []
                    # picks values in list default user[1]
                    for j in range(int(user[0])):
                        # if j == i + 1:
                        for k in range(int(user2[1])):
                            first = matA[j][i]
                            second = matB[i][k]  # default user2[1]
                            if "." in first or "." in second:
                                temp.append(float(first) * float(second))
                            else:
                                temp.append(int(first) * int(second))
                    final.append(temp)

                # prints = list(zip(*final))
                name = []
                for i in list(zip(*final)):
                    name.append(sum(i))
                h = []
                for i in range(int(user[0])):
                    h.append(name[:int(user2[1])])
                    del name[:int(user2[1])]
                print("The result is:")
                for i in h:
                    print(*i)
            except IndexError:
                print("This operation cannot be performed")

        else:
            print("This operation cannot be performed")
        print()
        return self.initial()

    def transpose(self):
        print()
        print("1. Main diagonal", "2. Side diagonal",
              "3. Vertical line", "4. Horizontal line", sep="\n")
        choice = input("Your choice:")
        user = input("Enter matrix size:").split()
        print("Enter matrix:")
        mat = [input().split() for i in range(int(user[0]))]
        if choice == "1":
            finale = []
            for i in range(len(mat[0])):
                temp = []
                for j in range(len(mat)):
                    temp.append(mat[j][i])
                finale.append(temp)
            print('The result is:')
            for i in finale:
                print(*i)
        elif choice == "2":
            new = []
            for i in reversed(mat):
                new.append(list(i))
            final = []
            for i in range(len(new), 0, -1):
                temp = []
                for j in range(len(new[0])):
                    temp.append(new[j][i - 1])
                final.append(temp)
            print("The result is:")
            for i in final:
                print(*i)
        elif choice == "3":
            print("The result is:")
            for i in mat:
                print(*list((reversed(i))))
        elif choice == "4":
            print("The result is:")
            for i in reversed(mat):
                print(*i)
        print()
        return self.initial()

    def determinant(self):
        user = input("Enter matrix size:").split()
        print("Enter matrix:")
        mat = [input().split() for i in range(int(user[0]))]
        if user[0] != user[1]:
            print("This operation cannot be performed")
        elif user[0] == "1":
            print(mat[0][0])
        else:
            new = [list(map(float, mat[i])) for i in range(len(mat))]
            result = determinant_recursive(new)
            print("The result is:")
            print(result)
            print()
        return self.initial()

    def inverse(self):
        user = input("Enter matrix size:").split()
        print("Enter matrix:")
        mat = [input().split() for i in range(int(user[0]))]
        if user[0] != user[1]:
            print("Inverse doesn't exist")
        else:
            new = [list(map(float, mat[i])) for i in range(len(mat))]
            result = determinant_recursive(new)
            if not result:
                A = np.array(mat)
                inver = np.linalg.inv(A)
                print("The result is:")
                for i in inver:
                    print(*i)
        return self.initial()

    def exit(self):
        self.play = False


def main():
    matrix = Matrix()
    matrix.loop()


if __name__ == "__main__":
    main()
