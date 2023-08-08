from MSmodel import MSModel
# from visualisation import visualisation
from Visualisation import Visualisation
# from plots import create_plots
from Plots import Plots

model = MSModel()
visualisation = Visualisation(model)
visualisation.run()
# plots = Plots(model.datacollector)
# plots.Plot()
