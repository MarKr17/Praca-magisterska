from itertools import permutations
from itertools import product
import os
import pandas as pd

Cell_numbers = {"T-cell": 20,
                "Th-cell": 20,
                "B-cell": 20,
                "APC": 20,
                "Virus": 50}
Proliferation_rate = {"T-cell": 2,
                      "Th-cell": 2,
                      "B-cell": 2,
                      "APC": 2,
                      "Virus": 2}
Health = {"T-cell": 50,
          "Th-cell": 50,
          "B-cell": 50,
          "APC": 50,
          "Virus": 50}

Dmg_factor = {"T-cell": 1,
              "Th-cell": 1,
              "B-cell": 1,
              "APC": 1,
              "Virus": 1}
# creates a list from 5 to 50, with a step of 5 [5, 10,...]

prolieration = [1, 1, 1, 2, 3]
health = []
dmg = []

folder_path = os.path.join(os.getcwd(), "tests")
folder_path = os.path.join(folder_path, "no-hip")
test_path = os.path.join(folder_path, "general")
folder_name = os.path.join(test_path, "test_results")


def read_chosen(filename):
    df = pd.read_csv(os.path.join(folder_name, filename))
    list = df['test'].to_list()
    return list


proliferation = read_chosen("proliferation_chosen.csv")
health = read_chosen("health_chosen.csv")
dmg = read_chosen("dmg_chosen.csv")

print(len(proliferation))
print(len(health))
print(len(dmg))

max_len = max(len(proliferation), len(health), len(dmg))
'''
if len(proliferation) == max_len:
    proliferation_comb = list(permutations(proliferation, r=max_len))
    health_comb = list(product(health, repeat=max_len))
    dmg_comb = list(product(dmg, repeat=max_len))
elif len(health) == max_len:
    proliferation_comb = list(product(proliferation, repeat=max_len))
    health_comb = list(permutations(health, r=max_len))
    dmg_comb = list(product(dmg, repeat=max_len))
elif len(dmg) == max_len:
    proliferation_comb = list(product(proliferation, repeat=max_len))
    health_comb = list(product(health, repeat=max_len))
    dmg_comb = list(permutations(dmg, r=max_len))

print(len(proliferation_comb))
print(len(health_comb))
print(len(dmg_comb))
'''