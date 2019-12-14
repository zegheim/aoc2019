class IntcodeComputer(object):
    def __init__(self):
        with open("inputs/day_5", "r") as f:
            self.memory = [i for i in f.read().split(",")]
        self.opcode_config = {"1": 3, "2": 3, "3": 1, "4": 1, "99": 0}
        self.pointer = 0

    def increase_pointer(self, val):
        self.pointer = self.pointer + val

    def parse_opcode_str(self, opcode_str):
        if opcode_str in self.opcode_config:
            return opcode_str, (0,) * self.opcode_config[opcode_str]

        opcode, param_modes = opcode_str[-2:].lstrip("0"), opcode_str[:-2]
        param_modes = tuple(
            int(m) for m in param_modes.zfill(self.opcode_config[opcode])[::-1]
        )

        return opcode, param_modes

    def run_instruction(self, opcode, params, param_modes):
        if opcode == "99":
            return False

        moded_params = [
            param if mode else int(self.memory[param])
            for param, mode in zip(params, param_modes)
        ]

        if opcode == "1":
            self.memory[params[-1]] = str(moded_params[0] + moded_params[1])
        elif opcode == "2":
            self.memory[params[-1]] = str(moded_params[0] * moded_params[1])
        elif opcode == "3":
            program_input = input("Please provide an integer: ")
            self.memory[params[0]] = program_input
        elif opcode == "4":
            print("Output: {}".format(moded_params[0]))
        else:
            raise NotImplementedError("Something went wrong.")

        return True

    def run_program(self):
        while self.pointer < len(self.memory):
            opcode_str = self.memory[self.pointer]
            opcode, param_modes = self.parse_opcode_str(opcode_str)
            param_length = self.opcode_config[opcode]
            params = [
                int(self.memory[self.pointer + i]) for i in range(1, param_length + 1)
            ]
            if not self.run_instruction(opcode, params, param_modes):
                break
            self.increase_pointer(param_length + 1)


def main():
    print("Part 1\n------")

    ic = IntcodeComputer()

    ic.run_program()

    print("\nPart 2\n------")
    print("Answer for part 2: {}\n".format(None))


if __name__ == "__main__":
    main()
