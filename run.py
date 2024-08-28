from MSmodel import MSModel
# from visualisation import visualisation
from Visualisation import Visualisation
# from plots import create_plots
from Plots import Plots
import os
Cell_numbers = {"T-cell": 30,
                "Th-cell": 30,
                "B-cell": 30,
                "APC": 40,
                "Virus": 100}
Proliferation_rate = {"T-cell": 3,
                      "Th-cell": 3,
                      "B-cell": 2,
                      "APC": 2,
                      "Virus": 50}
Health = {"T-cell": 30,
          "Th-cell": 30,
          "B-cell": 20,
          "APC": 50,
          "Virus": 10}

Dmg_factor = {"T-cell": 1,
              "Th-cell": 1,
              "B-cell": 2,
              "APC": 2,
              "Virus": 1}


def parameters_from_test(list):
    comb = [s[1:] for s in list]
    proliferation = comb[0].split('-')
    health = comb[1].split('-')
    dmg = comb[2].split('-')
    j = 0
    for key in Proliferation_rate:
        Proliferation_rate[key] = int(proliferation[j])
        Health[key] = int(health[j])
        Dmg_factor[key] = int(dmg[j])
        j += 1


def dicts_to_name():
    agents = ["T-cell", "Th-cell", "B-cell", "APC", "Virus"]
    cell_num = "C"
    proliferation = "P"
    health = "H"
    dmg = "D"
    for agent in agents:
        cell_num += '-' + str(Cell_numbers[agent])
        proliferation += '-' + str(Proliferation_rate[agent])
        health += '-' + str(Health[agent])
        dmg += '-' + str(Dmg_factor[agent])
    name = cell_num + proliferation + health + dmg
    print(name)
    return name


#parameters_from_test(["P2-2-2-2-50", "H20-100-20-70-20", "D2-5-1-10-2"])

name = dicts_to_name()
folder_name = os.path.join("test", name)
model = MSModel(Cell_numbers, Proliferation_rate, Health, Dmg_factor)
visualisation = Visualisation(model, folder_name)
visualisation.run()

if model.hypothesis == "":
    folder = os.path.join(folder_name, "base")
else:
    folder = os.path.join(folder_name, model.hypothesis)
plots = Plots(model.datacollector, folder)
# plots.Plot_combined()
plots.Plot_cells_by_category("T_cells")
plots.Plot_cells_by_category("B_cells")
plots.Plot_cells_by_category("Th_cells")
plots.Plot_cells_by_category("Misc_cells")
plots.Plot_cytokine_levels()
plots.Plot_protein_levels()
plots.Plot_multiple(["B cells latent", "B cells lytic", "B cells activated",
                     "B cells antigen presented", "APC antigen attached"])
plots.Plot_demyelination()
