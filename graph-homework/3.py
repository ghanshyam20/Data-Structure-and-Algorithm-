class MachineNetwork:

    def __init__(self):
        # this will  store machines and links
        self.machine_links = {}

    def add_link(self, m1, m2):
        #  its check m1 exist or not
        if m1 not in self.machine_links:
            self.machine_links[m1] = []

        #  tis check m2 exist or not
        if m2 not in self.machine_links:
            self.machine_links[m2] = []

        #  it will add connection both side
        if m2 not in self.machine_links[m1]:
            self.machine_links[m1].append(m2)

        if m1 not in self.machine_links[m2]:
            self.machine_links[m2].append(m1)

    def dfs(self, start):
        # it check machine exist or not
        if start not in self.machine_links:
            print("Machine not found")
            return []

        visited = []   #  thsi will store visited
        stack = []     # this is stack

        # put first machine in stack
        stack.append(start)

        # loop till stack not empty
        while len(stack) > 0:

            current = stack.pop()   # take last item

            # if not visited then process
            if current not in visited:
                visited.append(current)

                #  tjhsi will go to all connected machines
                for m in self.machine_links[current]:

                    # check not visited
                    if m not in visited:
                        stack.append(m)

        return visited


net = MachineNetwork()

# adding links
net.add_link("Machine_A", "Machine_B")
net.add_link("Machine_A", "Machine_C")
net.add_link("Machine_B", "Machine_D")
net.add_link("Machine_C", "Machine_D")
net.add_link("Machine_C", "Machine_E")

# call dfs
print(net.dfs("Machine_A"))