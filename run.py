from MSmodel import MSModel
# from visualisation import visualisation
from Visualisation import Visualisation
# from plots import create_plots
from Plots import Plots

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


model = MSModel(Cell_numbers, Proliferation_rate, Health, Dmg_factor)
visualisation = Visualisation(model)
visualisation.run()

plots = Plots(model.datacollector)
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
