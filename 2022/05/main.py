from collections import defaultdict

class Crate_Mover_9000:
    orders = None
    crates = None
    result = None

    def __init__(self,text_file):
        self.crates = self.board_cranes()
        self.text_file = text_file
        self.orders = self.read_text_file(self.text_file)

    def board_cranes(self):
        crates = defaultdict(dict)
        crates[1] = ['D','B','J','V']
        crates[2] = ['P','V','B','W','R','D','F']
        crates[3] = ['R','G','F','L','D','C','W','Q']
        crates[4] = ['W','J','P','M','L','N','D','B']
        crates[5] = ['H','N','B','P','C','S','Q']
        crates[6] = ['R','D','B','S','N','G']
        crates[7] = ['Z','B','P','M','Q','F','S','H']
        crates[8] = ['W','L','F']
        crates[9] = ['S','V','F','M','R']
        return crates

    def read_text_file(self,text_file):
        with open(text_file) as file_in:
            lines = []
            for line in file_in:
                lines.append(line[:-1])
        orders = [self.get_orders(line) for line in lines]
        return orders

    def get_orders(self,text):
        text_list = text.split(' ')
        res = [int(elem) for elem in text_list if elem.isdigit()]
        return res

    def move(self,order):
        quantity = order[0]
        source = order[1]
        destination = order[2]

        while quantity:
            box = self.crates[source].pop()
            self.crates[destination].append(box)
            quantity -= 1

    def visualise(self):
        for counter in range(1,len(self.crates.keys())+1):
            print(f'crate {counter}: ')
            print(self.crates[counter])

    def do_work(self):
        for order in self.orders:
            self.move(order)

    def get_result(self):
        res = []
        for crate in self.crates.keys():
            res.append(self.crates[crate].pop())
        return "".join(letter for letter in res)


class Crate_Mover_9001:
    orders = None
    crates = None
    result = None

    def __init__(self,text_file):
        self.crates = self.board_cranes()
        self.text_file = text_file
        self.orders = self.read_text_file(self.text_file)

    def board_cranes(self):
        crates = defaultdict(dict)
        crates[1] = ['D','B','J','V']
        crates[2] = ['P','V','B','W','R','D','F']
        crates[3] = ['R','G','F','L','D','C','W','Q']
        crates[4] = ['W','J','P','M','L','N','D','B']
        crates[5] = ['H','N','B','P','C','S','Q']
        crates[6] = ['R','D','B','S','N','G']
        crates[7] = ['Z','B','P','M','Q','F','S','H']
        crates[8] = ['W','L','F']
        crates[9] = ['S','V','F','M','R']
        return crates

    def read_text_file(self,text_file):
        with open(text_file) as file_in:
            lines = []
            for line in file_in:
                lines.append(line[:-1])
        orders = [self.get_orders(line) for line in lines]
        return orders

    def get_orders(self,text):
        text_list = text.split(' ')
        res = [int(elem) for elem in text_list if elem.isdigit()]
        return res

    def move(self,order):
        quantity = order[0]
        source = order[1]
        destination = order[2]

        moving_block = []
        while quantity:
            box = self.crates[source].pop()
            moving_block.append((box))
            # self.crates[destination].append(box)
            quantity -= 1
        moving_block.reverse()
        self.crates[destination] += moving_block

    def visualise(self):
        for counter in range(1,len(self.crates.keys())+1):
            print(f'crate {counter}: ')
            print(self.crates[counter])

    def do_work(self):
        for order in self.orders:
            self.move(order)

    def get_result(self):
        res = []
        for crate in self.crates.keys():
            res.append(self.crates[crate].pop())
        return "".join(letter for letter in res)


x = Crate_Mover_9001('input.txt')
x.visualise()
x.do_work()
x.visualise()

res = x.get_result()
print(res)
