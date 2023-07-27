from model import MoneyModel
from visualisation import visualisation
from plots import create_plots


model = MoneyModel(20, 10, 10)
visualisation(model)
create_plots(model)
