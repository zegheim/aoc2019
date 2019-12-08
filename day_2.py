def initialise(noun, verb):
    with open("inputs/day_2", "r") as f:
        memory = [int(i) for i in f.read().split(",")]

    memory[1] = noun
    memory[2] = verb

    return memory


def run_program(memory):
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


def main():
    mem_init = initialise(12, 2)
    run_program(mem_init)
    print(mem_init[0])


if __name__ == "__main__":
    main()
