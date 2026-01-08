Project Description
Retail banks increasingly use AI chatbots to handle routine customer enquiries. However, the effect of chatbot adoption on service performance is not always clear.
This simulation models a bank customer service system where customers are routed to either AI chatbots or human agents based on a predefined adoption rate.

The model focuses on evaluating:
Customer waiting times
Resource utilisation
Customer satisfaction (proxy measure)


Methodology
Approach: Quantitative simulation-based analysis
Technique: Discrete Event Simulation
Language: Python
Library: SimPy


Key assumptions:
Customer arrivals follow a Poisson process
Service times follow exponential distributions
Customers are probabilistically routed to chatbots or human agents
Customer satisfaction is estimated using a proxy based on waiting time


Simulation Parameters
Simulation time: 8 hours (480 minutes)
Chatbot adoption rate: 60%
Average arrival rate: 1 customer every 3 minutes
Average chatbot service time: 2 minutes
Average human service time: 5 minutes


Performance Measures

The simulation outputs the following metrics:

Average customer waiting time

Chatbot utilisation (proxy)

Human agent utilisation (proxy)
Average customer satisfaction score (out of 10)

How to Run the Simulation
Install dependencies:
pip install simpy
Run the simulation:
python simulation.py
The results will be printed directly to the console.

Reproducibility
All key parameters are defined at the top of the script and can be easily modified to test alternative scenarios.
