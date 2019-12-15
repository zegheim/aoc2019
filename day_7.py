import itertools


class IntcodeComputer(object):
    def __init__(self, mem_init, debug=False):
        self.debug = debug
        self.mem_init = tuple(mem_init)
        self.memory = mem_init
        self.opcode_config = {
            "1": 3,
            "2": 3,
            "3": 1,
            "4": 1,
            "5": 2,
            "6": 2,
            "7": 3,
            "8": 3,
            "99": 0,
        }
        self.pointer = 0

    def parse_opcode_str(self, opcode_str):
        if opcode_str in self.opcode_config:
            return opcode_str, (0,) * self.opcode_config[opcode_str]

        opcode, param_modes = opcode_str[-2:].lstrip("0"), opcode_str[:-2]
        param_modes = tuple(
            int(m) for m in param_modes.zfill(self.opcode_config[opcode])[::-1]
        )

        return opcode, param_modes

    def reset(self):
        self.memory = list(self.mem_init)
        self.pointer = 0

    def run_instruction(self, opcode, params, param_modes):
        if self.debug:
            print(
                "[DEBUG] opcode={}, params={}, param_modes={}".format(
                    opcode, params, param_modes
                )
            )
        moded_params = [
            param if mode else int(self.memory[param])
            for param, mode in zip(params[:-1], param_modes[:-1])
        ]
        if opcode in ["4", "5", "6"]:
            moded_params.append(
                params[-1] if param_modes[-1] else int(self.memory[params[-1]])
            )

        if opcode == "1":
            self.memory[params[-1]] = str(moded_params[0] + moded_params[1])
        elif opcode == "2":
            self.memory[params[-1]] = str(moded_params[0] * moded_params[1])
        elif opcode == "3":
            program_input = input("Please provide an integer: ")
            self.memory[params[-1]] = program_input
        elif opcode == "4":
            print("Output: {}".format(moded_params[0]))
        elif opcode == "5":
            if moded_params[0]:
                self.pointer = moded_params[1]
                return True
        elif opcode == "6":
            if not moded_params[0]:
                self.pointer = moded_params[1]
                return True
        elif opcode == "7":
            if moded_params[0] < moded_params[1]:
                self.memory[params[-1]] = 1
            else:
                self.memory[params[-1]] = 0
        elif opcode == "8":
            if moded_params[0] == moded_params[1]:
                self.memory[params[-1]] = 1
            else:
                self.memory[params[-1]] = 0
        else:
            raise NotImplementedError("Something went wrong.")

        return False

    def run_program(self):
        while self.pointer < len(self.memory):
            if self.debug:
                print("[DEBUG] pointer={}".format(self.pointer))
            opcode_str = self.memory[self.pointer]
            opcode, param_modes = self.parse_opcode_str(opcode_str)
            if opcode == "99":
                print("Exiting program...")
                break
            param_length = self.opcode_config[opcode]
            params = [
                int(self.memory[self.pointer + i]) for i in range(1, param_length + 1)
            ]
            jumped = self.run_instruction(opcode, params, param_modes)
            if not jumped:
                self.pointer = self.pointer + param_length + 1


def test_case():
    mem_init = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0".split(",")
    ic = IntcodeComputer(mem_init)
    for _ in [4, 3, 2, 1, 0]:
        ic.reset()
        ic.run_program()


def main():
    print("Part 1\n------")
    phases = [
        lambda x: 4 * x + 6,
        lambda x: 8 * x + 42,
        lambda x: 5 * x,
        lambda x: 3 * x + 9,
        lambda x: 9 * x + 11,
    ]
    max_output = 0
    for perm in itertools.permutations(phases):
        arg = 0
        for phase in perm:
            arg = phase(arg)
        max_output = max(max_output, arg)
    print(max_output)
    print("\nPart 2\n------")


if __name__ == "__main__":
    main()
