class MachineNetwork:

    def __init__(self):
        # thiswill  store machines and links
        self.machine_links = {}

    def add_link(self, m1, m2):
        #  tjhsi will check m1 exist or not
        if m1 not in self.machine_links:
            self.machine_links[m1] = []

        #  tjhsi will check m2 exist or not
        if m2 not in self.machine_links:
            self.machine_links[m2] = []

        #  thsi will add connection both side
        if m2 not in self.machine_links[m1]:
            self.machine_links[m1].append(m2)

        if m1 not in self.machine_links[m2]:
            self.machine_links[m2].append(m1)

    def bfs(self, start):
        #  tjhsi swill check start machine present or not
        if start not in self.machine_links:
            print("Machine not found")
            return []

        visited = []   #  thsi si emplty listy store visited machines
        queue = []     # this is for  queue

        #  thsi will add first machine
        queue.append(start)
        visited.append(start)

        # run loop till queue not empty
        while len(queue) > 0:

            current = queue.pop(0)   # remove first element

            # go to all connected machines
            for m in self.machine_links[current]:

                # check if already visited or not
                if m not in visited:
                    visited.append(m)    # add to visited
                    queue.append(m)      # also add to queue

        return visited


net = MachineNetwork()

# adding links
net.add_link("Machine_A", "Machine_B")
net.add_link("Machine_A", "Machine_C")
net.add_link("Machine_B", "Machine_D")
net.add_link("Machine_C", "Machine_D")
net.add_link("Machine_C", "Machine_E")

# calling  bfs
print(net.bfs("Machine_A"))