from MSmodel import MSModel
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

folder_path = os.path.join(os.getcwd(), "tests")
folder_path = os.path.join(folder_path, "no-hip")
test_path = os.path.join(folder_path, "general")
folder_name = os.path.join(test_path, "test_results")


def read_chosen(filename):
    df = pd.read_csv(os.path.join(folder_name, filename))
    list = df['test'].to_list()
    return list


def create_combinations(proliferation, health, dmg):
    proliferation = ["P" + s for s in proliferation]
    health = ["H" + s for s in health]
    dmg = ["D" + s for s in dmg]

    # proliferation = proliferation[: 4]
    # health = health[: 4]
    # dmg = dmg[: 4]

    combinations = []
    for p in proliferation:
        for h in health:
            for d in dmg:
                c = [p, h, d]
                if c not in combinations:
                    combinations.append(c)
    # print(len(combinations))
    # print(combinations[0])
    return combinations


def conduct_tests(combinations, steps):
    test_path = os.path.join(folder_path, "mixed")
    folder_name = os.path.join(test_path, "tests")
    # Conducting tests
    i = 0
    for combination in combinations:
        print("Conducting test {} of {}".format(i, len(combinations)))
        test_name = ' '.join([str(elem) for elem in combination])
        file_name = os.path.join(folder_name, test_name+".csv")
        comb = [s[1:] for s in combination]
        proliferation = comb[0].split('-')
        health = comb[1].split('-')
        dmg = comb[2].split('-')
        j = 0
        for key in Proliferation_rate:
            Proliferation_rate[key] = int(proliferation[j])
            Health[key] = int(health[j])
            Dmg_factor[key] = int(dmg[j])
            j += 1
        model = MSModel(Cell_numbers, Proliferation_rate, Health, Dmg_factor)
        for s in range(0, steps):
            model.step()
        data = model.datacollector.get_model_vars_dataframe()
        data.to_csv(file_name, encoding='utf-8', index=False)
        i += 1


proliferation = read_chosen("proliferation_chosen.csv")
health = read_chosen("health_chosen.csv")
dmg = read_chosen("dmg_chosen.csv")

combinations = create_combinations(proliferation, health, dmg)
#conduct_tests(combinations, 200)
