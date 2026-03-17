class MachineNetwork:

    def __init__(self):
        #  thsi wil store machines and their connections
        self.machine_links = {}

    def add_machine(self, machine):
        #  thsi will add machine if not already in dictionary
        if machine not in self.machine_links:
            self.machine_links[machine] = []

    def add_link(self, m1, m2):
        #  it s make sure both machine exist
        if m1 not in self.machine_links:
            self.machine_links[m1] = []
        if m2 not in self.machine_links:
            self.machine_links[m2] = []

        #  thsi will connect both ways
        if m2 not in self.machine_links[m1]:
            self.machine_links[m1].append(m2)

        if m1 not in self.machine_links[m2]:
            self.machine_links[m2].append(m1)

    def print_network(self):
        # it will print  all machines and links
        print("Machine Network:")
        for machine in self.machine_links:
            print(machine, "->", self.machine_links[machine])

    def print_connected_machines(self, machine):
        #  tjhis will print only connected machines
        if machine in self.machine_links:
            for m in self.machine_links[machine]:
                print(m)
        else:
            print("Machine not found")


net = MachineNetwork()

# adding links
net.add_link("Machine_A", "Machine_B")
net.add_link("Machine_A", "Machine_C")
net.add_link("Machine_B", "Machine_D")
net.add_link("Machine_C", "Machine_D")
net.add_link("Machine_C", "Machine_E")

net.print_network()

print()

#  thsi will check connections of one machine
net.print_connected_machines("Machine_C")