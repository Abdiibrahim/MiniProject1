import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# New Antecedent/Consequent objects hold universe variables and membership
# functions
personalChar = ctrl.Antecedent(np.arange(0, 11, 1), 'personalChar')  # 1
ageDiff = ctrl.Antecedent(np.arange(0, 101, 1), 'ageDiff')  # 2
educationLevelSim = ctrl.Antecedent(np.arange(0, 11, 1), 'educationLevelSim')  # 3
educationFieldSim = ctrl.Antecedent(np.arange(0, 11, 1), 'educationFieldSim')  # 4
sexualAttraction = ctrl.Antecedent(np.arange(0, 11, 1), 'sexualAttraction')  # 5
incomeSim = ctrl.Antecedent(np.arange(0, 11, 1), 'incomeSim')  # 6
careerSim = ctrl.Antecedent(np.arange(0, 11, 1), 'careerSim')  # 7
careerSat = ctrl.Antecedent(np.arange(0, 11, 1), 'careerSat')  # 7

marriage = ctrl.Consequent(np.arange(0, 101, 1), 'marriage')

# Auto-membership function population is possible with .automf(3, 5, or 7)
personalChar.automf(3)
educationLevelSim.automf(3)
educationFieldSim.automf(3)
sexualAttraction.automf(3)
incomeSim.automf(3)
careerSim.automf(3)
careerSat.automf(3)

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

rule3A = ctrl.Rule(educationLevelSim['poor'], marriage['low'])
rule3B = ctrl.Rule(educationLevelSim['average'], marriage['medium'])
rule3C = ctrl.Rule(educationLevelSim['good'], marriage['high'])

rule4A = ctrl.Rule(educationFieldSim['poor'], marriage['low'])
rule4B = ctrl.Rule(educationFieldSim['average'], marriage['medium'])
rule4C = ctrl.Rule(educationFieldSim['good'], marriage['high'])

rule5A = ctrl.Rule(sexualAttraction['poor'], marriage['low'])
rule5B = ctrl.Rule(sexualAttraction['average'], marriage['medium'])
rule5C = ctrl.Rule(sexualAttraction['good'], marriage['high'])

rule6A = ctrl.Rule(incomeSim['poor'], marriage['low'])
rule6B = ctrl.Rule(incomeSim['average'], marriage['medium'])
rule6C = ctrl.Rule(incomeSim['good'], marriage['high'])

rule7A = ctrl.Rule(careerSat['poor'], marriage['low'])
rule7B = ctrl.Rule((careerSat['average'] & careerSim['poor']) |
                   (careerSat['average'] & careerSim['average']), marriage['medium'])
rule7C = ctrl.Rule(careerSat['good'], marriage['high'])

ruleSet = [
    rule1A, rule1B, rule1C,
    rule2A, rule2B, rule2C,
    rule3A, rule3B, rule3C,
    rule4A, rule4B, rule4C,
    rule5A, rule5B, rule5C,
    rule6A, rule6B, rule6C,
    rule7A, rule7B, rule7C
]

# create control system
marriage_ctrl = ctrl.ControlSystem(ruleSet)
marriage_sim = ctrl.ControlSystemSimulation(marriage_ctrl)

# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs at once, use .inputs(dict_of_data)

marriage_sim.input['personalChar'] = 6.7
marriage_sim.input['ageDiff'] = 3
marriage_sim.input['educationLevelSim'] = 7
marriage_sim.input['educationFieldSim'] = 5
marriage_sim.input['sexualAttraction'] = 8
marriage_sim.input['incomeSim'] = 6
marriage_sim.input['careerSim'] = 4
marriage_sim.input['careerSat'] = 2

# Crunch the numbers and view result
marriage_sim.compute()
print(marriage_sim.output['marriage'])
marriage.view(sim=marriage_sim)
plt.show()
