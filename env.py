import random

class TrafficEnv:

    def __init__(self, level="easy"):
        self.level = level
        self.reset()

    def reset(self):
        if self.level == "easy":
            self.state = [random.randint(1, 5) for _ in range(4)]
        elif self.level == "medium":
            self.state = [random.randint(5, 15) for _ in range(4)]
        else:
            self.state = [random.randint(10, 20) for _ in range(4)]

        self.time = 0
        return self.state

    def state_fn(self):
        return self.state

    def step(self, action):
        cleared = 0

        if action == 0:
            cleared = min(self.state[0], 4) + min(self.state[1], 4)
            self.state[0] -= min(self.state[0], 4)
            self.state[1] -= min(self.state[1], 4)
        else:
            cleared = min(self.state[2], 4) + min(self.state[2], 4)
            self.state[2] -= min(self.state[2], 4)
            self.state[3] -= min(self.state[3], 4)

        self.state = [max(0, x + random.randint(0, 3)) for x in self.state]

        if self.level == "hard" and random.random() < 0.2:
            cleared += 5

        reward = max(0, min(1, cleared / (sum(self.state) + 1)))

        self.time += 1
        done = self.time > 50

        return self.state, reward, done
