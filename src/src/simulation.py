import random
import simpy

# Parameters
RANDOM_SEED = 42
SIM_TIME = 480          # minutes (8 hours)
ARRIVAL_RATE = 1 / 3    # average arrival every 3 minutes
CHATBOT_RATE = 1 / 2    # average chatbot service time = 2 minutes
HUMAN_RATE = 1 / 5      # average human service time = 5 minutes
CHATBOT_ADOPTION = 0.6  # 60% of customers routed to chatbot

random.seed(RANDOM_SEED)

# Customer Process
def customer(env, name, chatbot, human, wait_times, satisfaction_scores):
    arrival_time = env.now

    # Routing to Chatbot or Human Agent
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

    # Track waiting time
    wait_times.append(env.now - arrival_time)

    # Model Customer Satisfaction (Simple model based on wait time)
    satisfaction = max(0, 10 - (env.now - arrival_time) / 10)  # Max satisfaction is 10, scales with wait time
    satisfaction_scores.append(satisfaction)

# Arrival Process (Customers Arriving)
def arrival_process(env, chatbot, human, wait_times, satisfaction_scores):
    i = 0
    while True:
        yield env.timeout(random.expovariate(ARRIVAL_RATE))
        i += 1
        env.process(customer(env, f"Customer {i}", chatbot, human, wait_times, satisfaction_scores))

# Simulation Environment Setup
env = simpy.Environment()
chatbot = simpy.Resource(env, capacity=5)  # 5 Chatbots available
human = simpy.Resource(env, capacity=2)    # 2 Human agents available

wait_times = []  # List to track all waiting times
satisfaction_scores = []  # List to track customer satisfaction scores

# Start the customer arrival process
env.process(arrival_process(env, chatbot, human, wait_times, satisfaction_scores))

# Run the Simulation
env.run(until=SIM_TIME)

# Calculate Average Waiting Time
average_wait_time = sum(wait_times) / len(wait_times) if wait_times else 0

# Calculate Agent Utilization
chatbot_utilization = sum(1 for _ in wait_times if random.random() < CHATBOT_ADOPTION) / len(wait_times) if wait_times else 0
human_utilization = sum(1 for _ in wait_times if random.random() >= CHATBOT_ADOPTION) / len(wait_times) if wait_times else 0

# Calculate Average Customer Satisfaction
average_satisfaction = sum(satisfaction_scores) / len(satisfaction_scores) if satisfaction_scores else 0

# Print the results
print(f"Simulation completed.")
print(f"Average Waiting Time: {average_wait_time:.2f} minutes")
print(f"Chatbot Utilization: {chatbot_utilization * 100:.2f}%")
print(f"Human Agent Utilization: {human_utilization * 100:.2f}%")
print(f"Average Customer Satisfaction: {average_satisfaction:.2f} out of 10")
