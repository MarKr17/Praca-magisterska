from MSmodel import MSModel
# from visualisation import visualisation
from Visualisation import Visualisation
# from plots import create_plots
from Plots import Plots

model = MSModel()
visualisation = Visualisation(model)
visualisation.run()

plots = Plots(model.datacollector)
# plots.Plot_combined()
plots.Plot_cells_by_category("T_cells")
plots.Plot_cells_by_category("B_cells")
plots.Plot_cells_by_category("Th_cells")
plots.Plot_cells_by_category("Misc_cells")
