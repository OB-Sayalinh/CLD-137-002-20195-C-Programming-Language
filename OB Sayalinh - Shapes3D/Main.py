import FileParser

solver = FileParser.Solver()

enable = True

if enable:
    print(round(solver.solve("exampleInput.csv"), 2))
else:
    print(round(solver.solve(input("What file would you like to use?: ")), 2))

