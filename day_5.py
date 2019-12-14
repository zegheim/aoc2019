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


def run_tests():
    print("Test #1: Check if input equals 8 (position mode)")
    IntcodeComputer("3,9,8,9,10,9,4,9,99,-1,8".split(",")).run_program()
    print("Test #2: Check if input equals 7 (immediate mode)")
    IntcodeComputer("3,3,1107,-1,8,3,4,3,99".split(",")).run_program()
    print("Test #3: Check if input is non-zero (position mode)")
    IntcodeComputer("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9".split(",")).run_program()
    print("Test #4: Check if input is non-zero (immediate mode)")
    IntcodeComputer("3,3,1105,-1,9,1101,0,0,12,4,12,99,1".split(",")).run_program()
    print("Test #5.1: Check if input is below 8 (expected 999)")
    test_ic = IntcodeComputer(
        (
            "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,"
            "21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
        ).split(","),
        debug=True,
    )
    test_ic.run_program()
    print("Test #5.2: Check if input equals 8 (expected 1000)")
    test_ic.set_pointer(0)
    test_ic.run_program()
    print("Test #5.3: Check if input is above 8 (expected 1001)")
    test_ic.set_pointer(0)
    test_ic.run_program()


def main():
    with open("inputs/day_5", "r") as f:
        mem_init = f.read().split(",")
    ic = IntcodeComputer(mem_init)

    print("Part 1\n------")
    ic.run_program()
    print("\nPart 2\n------")
    ic.reset()
    ic.run_program()


if __name__ == "__main__":
    main()
