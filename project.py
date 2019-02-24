import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# New Antecedent/Consequent objects hold universe variables and membership
# functions

personalChar = ctrl.Antecedent(np.arange(0, 11, 1), 'personalChar')
ageDiff = ctrl.Antecedent(np.arange(0, 101, 1), 'ageDiff')
education = ctrl.Antecedent(np.arange(0, 11, 1), 'education')

marriage = ctrl.Consequent(np.arange(0, 101, 1), 'marriage')

# Auto-membership function population is possible with .automf(3, 5, or 7)
personalChar.automf(3)
education.automf(3)
ageDiff.automf(3)

# Custom membership functions can be built interactively with a familiar,
# Pythonic API
marriage['low'] = fuzz.trimf(marriage.universe, [0, 0, 30])
marriage['medium'] = fuzz.trimf(marriage.universe, [20, 45, 70])
marriage['high'] = fuzz.trimf(marriage.universe, [60, 100, 100])

ageDiff['low'] = fuzz.trimf(ageDiff.universe, [0, 0, 5])
ageDiff['medium'] = fuzz.trimf(ageDiff.universe, [5, 7.5, 10])
ageDiff['high'] = fuzz.trimf(ageDiff.universe, [10, 100, 100])

# Add fuzzy rules (to be changed)
rule1A = ctrl.Rule(personalChar['good'], marriage['high'])
rule1B = ctrl.Rule(personalChar['average'], marriage['medium'])
rule1C = ctrl.Rule(personalChar['poor'], marriage['low'])

rule2A = ctrl.Rule(ageDiff['low'], marriage['high'])
rule2B = ctrl.Rule(ageDiff['medium'], marriage['medium'])
rule2C = ctrl.Rule(ageDiff['high'], marriage['low'])

# create control system
marriage_ctrl = ctrl.ControlSystem([rule1A, rule1B, rule1C, rule2A, rule2B, rule2C])
marriage_sim = ctrl.ControlSystemSimulation(marriage_ctrl)

# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs at once, use .inputs(dict_of_data)

marriage_sim.input['personalChar'] = 7.5
marriage_sim.input['ageDiff'] = 0

# Crunch the numbers and view result
marriage_sim.compute()
print(marriage_sim.output['marriage'])
marriage.view(sim=marriage_sim)
plt.show()
