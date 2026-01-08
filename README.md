# Bank Customer Service Chatbot Simulation

This repository contains a Python-based Discrete Event Simulation (DES) model developed as part of a Master's dissertation. The simulation evaluates the impact of AI chatbot adoption on customer service performance in a retail banking environment.

---

## Project Description

Retail banks increasingly use AI chatbots to handle routine customer enquiries. This simulation models a bank customer service system where customers are routed to either AI chatbots or human agents based on a predefined adoption rate. The objective is to assess how chatbot adoption affects waiting time, resource utilisation, and customer satisfaction.

---

## Methodology

This study adopts a quantitative, simulation-based approach using Discrete Event Simulation. The model is implemented in Python using the SimPy library.

Key assumptions include:

* Customer arrivals follow a Poisson process
* Service times follow exponential distributions
* Customers are probabilistically routed to chatbots or human agents
* Customer satisfaction is estimated using a proxy based on waiting time

---

## Simulation Parameters

* Simulation duration: 480 minutes (8 hours)
* Chatbot adoption rate: 60%
* Average arrival rate: 1 customer every 3 minutes
* Average chatbot service time: 2 minutes
* Average human service time: 5 minutes
* Resources: 5 chatbots and 2 human agents

---

## Performance Measures

The simulation reports:

* Average customer waiting time
* Chatbot utilisation (proxy)
* Human agent utilisation (proxy)
* Average customer satisfaction score

---

## How to Run

1. Install SimPy:

```bash
pip install simpy
```

2. Run the simulation:

```bash
python simulation.py
```

Results are printed to the console.

---

## Reproducibility

All key parameters are defined at the top of the script and can be modified to test different scenarios.




