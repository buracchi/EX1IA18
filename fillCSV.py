

def FillCSV(ascissa, ordinata, filename):
    file = open(filename + ".csv", "a")
    file.write(ascissa + ",\t" + ordinata + "\n")
    file.close()
