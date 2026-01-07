import random
import simpy

RANDOM_SEED = 42
SIM_TIME = 480          # minutes (8 hours)
ARRIVAL_RATE = 1 / 3    # average arrival every 3 minutes
CHATBOT_RATE = 1 / 2    # average chatbot service time = 2 minutes
HUMAN_RATE = 1 / 5      # average human service time = 5 minutes
CHATBOT_ADOPTION = 0.6  # 60% of customers routed to chatbot

random.seed(RANDOM_SEED)

def customer(env, name, chatbot, human):
    arrival_time = env.now

    if random.random() < CHATBOT_ADOPTION:
        with chatbot.request() as request:
            yield request
            service_time = random.expovariate(CHATBOT_RATE)
            yield env.timeout(service_time)
    else:
        with human.request() as request:
            yield request
            service_time = random.expovariate(HUMAN_RATE)
            yield env.timeout(service_time)

def arrival_process(env, chatbot, human):
    i = 0
    while True:
        yield env.timeout(random.expovariate(ARRIVAL_RATE))
        i += 1
        env.process(customer(env, f"Customer {i}", chatbot, human))

env = simpy.Environment()
chatbot = simpy.Resource(env, capacity=5)
human = simpy.Resource(env, capacity=2)

env.process(arrival_process(env, chatbot, human))
env.run(until=SIM_TIME)

print("Simulation completed.")
