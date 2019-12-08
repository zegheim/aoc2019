def initialise(noun, verb):
    with open("inputs/day_2", "r") as f:
        memory = [int(i) for i in f.read().split(",")]

    memory[1] = noun
    memory[2] = verb

    return memory


def run_program(mem_init):
    memory = mem_init
    pointer = 0
    while pointer < len(memory):
        opcode = memory[pointer]
        if opcode == 99:
            break
        params = [memory[pointer + k] for k in range(1, 4)]
        if opcode == 1:
            memory[params[2]] = memory[params[0]] + memory[params[1]]
        elif opcode == 2:
            memory[params[2]] = memory[params[0]] * memory[params[1]]
        else:
            raise Exception(
                "Something went wrong at address = %d. Value at address = %d",
                pointer,
                memory[pointer],
            )
        pointer = pointer + len(params) + 1
    return memory


def main():
    mem_init = initialise(12, 2)
    memory = run_program(mem_init)
    print("Answer for part 1: {}".format(memory[0]))

    import numpy as np

    outputs_n = np.array([run_program(initialise(noun, 0))[0] for noun in range(0, 10)])
    print(outputs_n)
    print(np.diff(outputs_n))  # output = 368640n + f(v) + C

    outputs_v = np.array([run_program(initialise(0, verb))[0] for verb in range(0, 10)])
    print(outputs_v)
    print(np.diff(outputs_v))  # output = 368640n + v + 152702

    print("Noun: {}".format((19690720 - 152702) // 368640))  # 53
    print("Verb: {}".format((19690720 - 152702) % 368640))  # 98

    print("Answer for part 2: {}".format(53 * 100 + 98))


if __name__ == "__main__":
    main()
