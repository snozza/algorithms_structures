from itertools import product

class Sudoku:

    def solver(size, grid):

        Row, Col = size
        Total = Row * Col
        ProbSet = ([("row-col", row-col for row-col in product(range(Total), range(Total))] +
                    ["row-num", row-num for row-num in product(range(Total), range(Total))] +
                    ["col-num", col-num for col-num in product(range(Total), range(Total))] +
                    ["box-num", box-num for box-num in product(range(Total), range(Total))]
        Collection = dict()

        for(row, col, total in product(range(Total), range(Total), range(1, Total + 1)):
            box = (row // Row) * Row + (col // Col)
            print(box)