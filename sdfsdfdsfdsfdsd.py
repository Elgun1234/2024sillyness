def MaxScore(Puzzlename):
    f = open(f"{Puzzlename}.txt", "r")
    grid = f.readline(9)
    print(grid)

MaxScore("puzzle4")