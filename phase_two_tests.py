from itertools import combinations_with_replacement
import os
from MSmodel import MSModel

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
