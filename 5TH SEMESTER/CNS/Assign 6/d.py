class Router:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors  # List of (neighbor_name, cost)
        self.routing_table = {name: (0, name)}  # Distance to self is 0
        for neighbor, cost in neighbors:
            self.routing_table[neighbor] = (cost, neighbor)  # Initial distance to neighbors

    def update_routing_table(self, neighbor_router):
        updated = False
        for destination, (neighbor_distance, _) in neighbor_router.routing_table.items():
            if destination not in self.routing_table:
                self.routing_table[destination] = (neighbor_distance + self.routing_table[neighbor_router.name][0], neighbor_router.name)
                updated = True
            else:
                current_distance, next_hop = self.routing_table[destination]
                new_distance = neighbor_distance + self.routing_table[neighbor_router.name][0]
                if new_distance < current_distance:
                    self.routing_table[destination] = (new_distance, neighbor_router.name)
                    updated = True
        return updated

    def display_routing_table(self):
        print(f"Routing table for router {self.name}:")
        for destination, (distance, next_hop) in self.routing_table.items():
            print(f"Destination: {destination}, Distance: {distance}, Next hop: {next_hop}")
        print("\n")

# Simulation of network
def distance_vector_routing(routers):
    changes = True
    iteration = 0
    while changes:
        changes = False
        print(f"--- Iteration {iteration} ---")
        for router in routers:
            for neighbor_name, _ in router.neighbors:
                neighbor_router = next(r for r in routers if r.name == neighbor_name)
                if router.update_routing_table(neighbor_router):
                    changes = True
        iteration += 1
        for router in routers:
            router.display_routing_table()

# Creating routers and their neighbors
r1 = Router('A', [('B', 1), ('C', 4)])
r2 = Router('B', [('A', 1), ('C', 2), ('D', 7)])
r3 = Router('C', [('A', 4), ('B', 2), ('D', 3)])
r4 = Router('D', [('B', 7), ('C', 3)])

routers = [r1, r2, r3, r4]

# Perform distance vector routing
distance_vector_routing(routers)
