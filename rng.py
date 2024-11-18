import numpy as np
import random
import time
import matplotlib.pyplot as plt

def random_rand():
    return np.random.rand()

def random_randn():
    return (np.random.randn() + 3) / 6

def system_random():
    return random.SystemRandom().random()

def random_power():
    return np.random.power(3)

def random_poisson():
    return np.random.poisson(3) / 10

random_generators = {
    "random_1": np.random.uniform,
    "random_2": random_rand,
    "random_3": random_randn,
    "random_4": system_random,
    "random_5": random_power,
    "random_6": random_poisson
}

def estimate_pi_fixed(n, generator, arg_based=False):
    inside_circle = 0
    start_time = time.time()
    
    for _ in range(n):
        if arg_based:
            x, y = generator(0, 1), generator(0, 1)
        else:
            x, y = generator(), generator()
            
        if x**2 + y**2 <= 1:
            inside_circle += 1
    
    pi_estimate = 4 * (inside_circle / n)
    elapsed_time = time.time() - start_time
    
    return pi_estimate, elapsed_time

def estimate_integral(N, generator, arg_based=False):
    sum_fx = 0
    start_time = time.time()
    
    for _ in range(N):
        if arg_based:
            x = generator(0, np.pi)
        else:
            x = generator() * np.pi
        
        sum_fx += np.sin(x)
    
    integral_estimate = (np.pi / N) * sum_fx
    elapsed_time = time.time() - start_time
    
    return integral_estimate, elapsed_time

def compare_generators_fixed(N):
    comparison_results = {}
    for name, generator in random_generators.items():
        if name == "random_1":
            pi_estimate, time_taken = estimate_pi_fixed(N, generator, arg_based=True)
        else:
            pi_estimate, time_taken = estimate_pi_fixed(N, generator)
        comparison_results[name] = (pi_estimate, time_taken)
    return comparison_results

def compare_integral_generators(N):
    comparison_results = {}
    for name, generator in random_generators.items():
        if name == "random_1":
            integral_estimate, time_taken = estimate_integral(N, generator, arg_based=True)
        else:
            integral_estimate, time_taken = estimate_integral(N, generator)
        comparison_results[name] = (integral_estimate, time_taken)
    return comparison_results

N = 10000
comparison_results_fixed = compare_generators_fixed(N)
comparison_results_integral = compare_integral_generators(N)

generators = list(comparison_results_fixed.keys())
pi_estimates = [result[0] for result in comparison_results_fixed.values()]
time_taken_pi = [result[1] for result in comparison_results_fixed.values()]

integral_estimates = [result[0] for result in comparison_results_integral.values()]
time_taken_integral = [result[1] for result in comparison_results_integral.values()]

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(generators, pi_estimates, color='skyblue')
plt.axhline(y=3.14159, color='r', linestyle='--', label='True Pi Value')
plt.title('Pi Estimates from Different Generators')
plt.ylabel('Estimated Pi Value')
plt.xlabel('Random Generators')
plt.legend()

plt.subplot(1, 2, 2)
plt.bar(generators, integral_estimates, color='lightblue')
plt.axhline(y=2, color='r', linestyle='--', label='True Integral Value')
plt.title('Integral Estimates from Different Generators')
plt.ylabel('Estimated Integral Value')
plt.xlabel('Random Generators')
plt.legend()

plt.tight_layout()
plt.show()
