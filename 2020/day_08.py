data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

with open('./data/day_08.txt') as fd:
    data = fd.read()


class Console:
    def __init__(self, boot_text: str):
        self.init_comms = boot_text.split('\n')
        self.ERROR = False
        self.boot_generator = self.fix_boot_text()

    def acc(self, num: int):
        self.accumulator += num
        self.line += 1

    def nop(self, _):
        self.line += 1

    def jmp(self, num: int):
        self.line += num

    def run(self, comm_line: str):
        if self.line in self.used_lines:
            print(f"LOOP DETECTED! Acc = {self.accumulator}")
            # print(self.used_lines)
            self.ERROR = True
            return
        self.used_lines += [self.line]
        comm, arg = comm_line.split()
        getattr(self, comm)(int(arg))

    def fix_boot_text(self):
        i = 0
        while i < len(self.init_comms):
            if self.init_comms[i][:3] in ('nop', 'jmp'):
                # print(f"\tTry to fix {i}-th line: {self.init_comms[i]}")
                test_boot = self.init_comms[:i]
                if self.init_comms[i][:3] == 'nop':
                    test_boot += ['jmp' + self.init_comms[i][3:]]
                else:
                    test_boot += ['nop' + self.init_comms[i][3:]]
                test_boot += self.init_comms[i+1:]
                yield test_boot
            i += 1

    def boot(self, boot_set=None):
        self.accumulator = 0
        self.line = 0
        self.used_lines = []
        self.ERROR = False
        if not boot_set:
            boot_set = self.init_comms
        while not self.ERROR:
            try:
                self.run(boot_set[self.line])
            except IndexError:
                print(f"Booted. Acc = {self.accumulator}")
                return
        while self.ERROR:
            self.boot(next(self.boot_generator))


if __name__ == "__main__":
    C = Console(data)
    C.boot()
