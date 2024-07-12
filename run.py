from MSmodel import MSModel
# from visualisation import visualisation
from Visualisation import Visualisation
# from plots import create_plots
from Plots import Plots
import os
Cell_numbers = {"T-cell": 30,
                "Th-cell": 30,
                "B-cell": 50,
                "APC": 40,
                "Virus": 100}
Proliferation_rate = {"T-cell": 1,
                      "Th-cell": 1,
                      "B-cell": 1,
                      "APC": 2,
                      "Virus": 2}
Health = {"T-cell": 20,
          "Th-cell": 20,
          "B-cell": 20,
          "APC": 100,
          "Virus": 20}

Dmg_factor = {"T-cell": 1,
              "Th-cell": 1,
              "B-cell": 1,
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


parameters_from_test(["P2-2-2-2-50", "H20-100-20-70-20", "D2-5-1-10-2"])

model = MSModel(Cell_numbers, Proliferation_rate, Health, Dmg_factor)
visualisation = Visualisation(model)
visualisation.run()

folder_name = os.path.join("test", model.hypothesis)
plots = Plots(model.datacollector, folder_name)
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
