import random

class Bird:
    def __init__(self, name):
        self.name = name
        self.location = random.randint(1, 100)
        self.direction = random.choice([-1, 1])

    def move(self):
        # Simulate bird movement
        self.location += self.direction * random.randint(1, 10)

    def report(self):
        # Print bird's status
        print(f"{self.name} is at location {self.location}.")

def simulate_migration(birds, iterations):
    for _ in range(iterations):
        for bird in birds:
            bird.move()
            bird.report()

if __name__ == "__main__":
    # Create a flock of migrating birds
    bird_names = ["Robin", "Sparrow", "Swan", "Pigeon", "Eagle"]
    flock = [Bird(name) for name in bird_names]

    # Simulate the migration for 5 iterations
    simulate_migration(flock, iterations=5)
