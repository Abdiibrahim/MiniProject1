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
habitSim = ctrl.Antecedent(np.arange(0, 11, 1), 'habitSim')  # 8
hobbySim = ctrl.Antecedent(np.arange(0, 11, 1), 'hobbySim')  # 9
adventureSim = ctrl.Antecedent(np.arange(0, 11, 1), 'adventureSim')  # 9
uniqueness = ctrl.Antecedent(np.arange(0, 11, 1), 'uniqueness')  # 10
childAgreement = ctrl.Antecedent(np.arange(0, 11, 1), 'childAgreement')  # 11
familySupport = ctrl.Antecedent(np.arange(0, 11, 1), 'familySupport')  # 12
futurePlanSim = ctrl.Antecedent(np.arange(0, 11, 1), 'futurePlanSim')  # 13
religiousSim = ctrl.Antecedent(np.arange(0, 11, 1), 'religiousSim')  # 14
politicalSim = ctrl.Antecedent(np.arange(0, 11, 1), 'politicalSim')  # 15
love = ctrl.Antecedent(np.arange(0, 11, 1), 'love')  # 16
friendSupport = ctrl.Antecedent(np.arange(0, 11, 1), 'friendSupport')  # 17

marriage = ctrl.Consequent(np.arange(0, 101, 1), 'marriage')

# Auto-membership function population is possible with .automf(3, 5, or 7)
personalChar.automf(3)
educationLevelSim.automf(3)
educationFieldSim.automf(3)
sexualAttraction.automf(3)
incomeSim.automf(3)
careerSim.automf(3)
careerSat.automf(3)
habitSim.automf(3)
hobbySim.automf(3)
adventureSim.automf(3)
uniqueness.automf(3)
childAgreement.automf(3)
familySupport.automf(3)
futurePlanSim.automf(3)
religiousSim.automf(3)
politicalSim.automf(3)
love.automf(3)
friendSupport.automf(3)

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

rule8A = ctrl.Rule(habitSim['poor'], marriage['low'])
rule8B = ctrl.Rule(habitSim['average'], marriage['medium'])
rule8C = ctrl.Rule(habitSim['good'], marriage['high'])

rule9A = ctrl.Rule(hobbySim['poor'], marriage['low'])
rule9B = ctrl.Rule((hobbySim['average'] & adventureSim['poor']) |
                   (hobbySim['average'] & adventureSim['average']), marriage['medium'])
rule9C = ctrl.Rule(hobbySim['good'] | adventureSim['good'], marriage['high'])

rule10A = ctrl.Rule(uniqueness['poor'], marriage['low'])
rule10B = ctrl.Rule(uniqueness['average'], marriage['medium'])
rule10C = ctrl.Rule(uniqueness['good'], marriage['high'])

rule11A = ctrl.Rule(childAgreement['poor'], marriage['low'])
rule11B = ctrl.Rule(childAgreement['average'], marriage['medium'])
rule11C = ctrl.Rule(childAgreement['good'], marriage['high'])

rule12A = ctrl.Rule(familySupport['poor'], marriage['low'])
rule12B = ctrl.Rule(familySupport['average'], marriage['medium'])
rule12C = ctrl.Rule(familySupport['good'], marriage['high'])

rule13A = ctrl.Rule(futurePlanSim['poor'], marriage['low'])
rule13B = ctrl.Rule(futurePlanSim['average'], marriage['medium'])
rule13C = ctrl.Rule(futurePlanSim['good'], marriage['high'])

rule14A = ctrl.Rule(religiousSim['poor'], marriage['low'])
rule14B = ctrl.Rule(religiousSim['average'], marriage['medium'])
rule14C = ctrl.Rule(religiousSim['good'], marriage['high'])

rule15A = ctrl.Rule(politicalSim['poor'], marriage['low'])
rule15B = ctrl.Rule(politicalSim['average'], marriage['medium'])
rule15C = ctrl.Rule(politicalSim['good'], marriage['high'])

rule16A = ctrl.Rule(love['poor'], marriage['low'])
rule16B = ctrl.Rule(love['average'], marriage['medium'])
rule16C = ctrl.Rule(love['good'], marriage['high'])

rule17A = ctrl.Rule(friendSupport['poor'], marriage['low'])
rule17B = ctrl.Rule(friendSupport['average'], marriage['medium'])
rule17C = ctrl.Rule(friendSupport['good'], marriage['high'])

ruleSet = [
    rule1A, rule1B, rule1C,
    rule2A, rule2B, rule2C,
    rule3A, rule3B, rule3C,
    rule4A, rule4B, rule4C,
    rule5A, rule5B, rule5C,
    rule6A, rule6B, rule6C,
    rule7A, rule7B, rule7C,
    rule8A, rule8B, rule8C,
    rule9A, rule9B, rule9C,
    rule10A, rule10B, rule10C,
    rule11A, rule11B, rule11C,
    rule12A, rule12B, rule12C,
    rule13A, rule13B, rule13C,
    rule14A, rule14B, rule14C,
    rule15A, rule15B, rule15C,
    rule16A, rule16B, rule16C,
    rule17A, rule17B, rule17C
]

# create control system
marriage_ctrl = ctrl.ControlSystem(ruleSet)
marriage_sim = ctrl.ControlSystemSimulation(marriage_ctrl)

# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs at once, use .inputs(dict_of_data)
dataSet1 = {
    'personalChar': 6.7,
    'ageDiff': 3,
    'educationLevelSim': 7,
    'educationFieldSim': 5,
    'sexualAttraction': 8,
    'incomeSim': 6,
    'careerSim': 4,
    'careerSat': 2,
    'habitSim': 7,
    'hobbySim': 8,
    'adventureSim': 10,
    'uniqueness': 5,
    'childAgreement': 9,
    'familySupport': 6,
    'futurePlanSim': 4,
    'religiousSim': 8,
    'politicalSim': 4,
    'love': 9,
    'friendSupport': 8
}
marriage_sim.inputs(dataSet1)

# Crunch the numbers and view result
marriage_sim.compute()
print(marriage_sim.output['marriage'])
marriage.view(sim=marriage_sim)
plt.show()
