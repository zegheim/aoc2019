with open("inputs/day_2", "r") as f:
    intcode = [int(i) for i in f.read().split(",")]

intcode[1] = 12
intcode[2] = 2

for i in range(0, len(intcode), 4):
    if intcode[i] == 99:
        print(intcode[0])
        break
    input_1 = intcode[intcode[i + 1]]
    input_2 = intcode[intcode[i + 2]]
    if intcode[i] == 1:
        intcode[intcode[i + 3]] = input_1 + input_2
    elif intcode[i] == 2:
        intcode[intcode[i + 3]] = input_1 * input_2
    else:
        raise Exception("Something went wrong.")
