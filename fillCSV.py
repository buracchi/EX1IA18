

def FillCSV(numeroElementi, time, filename):      # ascissa, ordinata, "nomeFile"
    file = open(filename + ".csv", "a")
    file.write(numeroElementi + ",\t" + time + "\n")
    file.close()
