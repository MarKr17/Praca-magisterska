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
dmg_range = [*range(1, 21, 1)]
folder_path = os.path.join(os.getcwd(), "tests")
folder_path = os.path.join(folder_path, "no-hip")


def proliferation_test(folder_path, steps):
    proliferation_rate = Proliferation_rate.copy()
    test_path = os.path.join(folder_path, "general")
    proliferation_range = [*range(1, 4, 1)]

    proliferation_comb = list(combinations_with_replacement(
                              proliferation_range, 5))

    folder_name = os.path.join(test_path, "proliferation_test")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    count = 1
    for comb in proliferation_comb:
        i = 0
        print("Conducting test number {}".format(count))
        for key in proliferation_rate:
            proliferation_rate[key] = comb[i]
            i += 1
        model = MSModel(Cell_numbers, proliferation_rate, Health, Dmg_factor)
        for s in range(0, steps):
            model.step()
        data = model.datacollector.get_model_vars_dataframe()
        file_name = os.path.join(folder_name, '-'.join(map(str, comb))+".csv")
        data.to_csv(file_name, encoding='utf-8', index=False)
        count += 1


def health_test(folder_path, steps):
    health = Health.copy()
    test_path = os.path.join(folder_path, "general")
    health_range = [*range(10, 71, 20)]
    health_comb = list(combinations_with_replacement(
                              health_range, 5))

    folder_name = os.path.join(test_path, "health_test")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    count = 1
    for comb in health_comb:
        i = 0
        print("Conducting test number {}".format(count))
        for key in health:
            health[key] = comb[i]
            i += 1
        model = MSModel(Cell_numbers, Proliferation_rate, health, Dmg_factor)
        for s in range(0, steps):
            model.step()
        data = model.datacollector.get_model_vars_dataframe()
        file_name = os.path.join(folder_name, '-'.join(map(str, comb))+".csv")
        data.to_csv(file_name, encoding='utf-8', index=False)
        count += 1


def dmg_test(folder_path, steps):
    dmg_factor = Dmg_factor.copy()
    test_path = os.path.join(folder_path, "general")
    dmg_range = [*range(1, 4, 1)]
    dmg_comb = list(combinations_with_replacement(
                              dmg_range, 5))

    folder_name = os.path.join(test_path, "dmg_test")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    count = 1
    for comb in dmg_comb:
        i = 0
        print("Conducting test number {}".format(count))
        for key in dmg_factor:
            dmg_factor[key] = comb[i]
            i += 1
        model = MSModel(Cell_numbers, Proliferation_rate, Health, dmg_factor)
        for s in range(0, steps):
            model.step()
        data = model.datacollector.get_model_vars_dataframe()
        file_name = os.path.join(folder_name, '-'.join(map(str, comb))+".csv")
        data.to_csv(file_name, encoding='utf-8', index=False)
        count += 1


# proliferation_test(folder_path, 200)
# health_test(folder_path, 200)
dmg_test(folder_path, 200)
