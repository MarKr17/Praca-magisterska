import pandas as pd
import os
import math
folder_path = os.path.join(os.getcwd(), "tests")
folder_path = os.path.join(folder_path, "no-hip")
test_path = os.path.join(folder_path, "general")


def create_df_list(folder_name):
    file_list = os.listdir(folder_name)
    df_list = []
    for file in file_list:
        df = pd.read_csv(os.path.join(folder_name, file))
        df.drop(df.columns.difference(['T-cell population',
                                       'Th-cell population',
                                       'B-cell population',
                                       'APC population',
                                       'Virus population']), axis=1,
                inplace=True)
        df['test'] = file.split('.')[0]
        df_list.append(df)
    return df_list


def avg_cells_df(df_list):
    dfc = pd.DataFrame(columns=["T-cell", "Th-cell", "B-cell", "APC", "Virus",
                                "test"])
    for df in df_list:
        avgs = {"T-cell": df.loc[:, 'T-cell population'].mean(),
                "Th-cell": df.loc[:, 'Th-cell population'].mean(),
                "B-cell": df.loc[:, 'B-cell population'].mean(),
                "APC": df.loc[:, 'APC population'].mean(),
                "Virus": df.loc[:, 'Virus population'].mean(),
                "test": df['test'].iloc[0]}
        dfc = dfc._append(avgs, ignore_index=True)
        dfc["mean"] = dfc.mean(axis=1)
        dfc["min"] = dfc.min(axis=1)
        dfc["max"] = dfc.max(axis=1)
    return dfc


folder_name = os.path.join(test_path, "proliferation_test")
proliferation_list = create_df_list(folder_name)
proliferation_avg = avg_cells_df(proliferation_list)

folder_name = os.path.join(test_path, "health_test")
health_list = create_df_list(folder_name)
health_avg = avg_cells_df(health_list)

folder_name = os.path.join(test_path, "dmg_test")
dmg_list = create_df_list(folder_name)
dmg_avg = avg_cells_df(dmg_list)

folder_name = os.path.join(test_path, "test_results")

proliferation_avg.to_csv(os.path.join(folder_name, "Average_proliferation.csv"),
                         index=False)
health_avg.to_csv(os.path.join(folder_name, "Average_health.csv"), index=False)
dmg_avg.to_csv(os.path.join(folder_name, "Average_dmg.csv"), index=False)

proliferation_chosen = proliferation_avg.loc[math.isclose(
    proliferation_avg['mean'], 20, rel_tol=5) and
    proliferation_avg[min] > 10
    and proliferation_avg[max] < 40]

health_chosen = health_avg.loc[math.isclose(
    health_avg['mean'], 20, rel_tol=5) and
    health_avg[min] > 10
    and health_avg[max] < 40]

dmg_chosen = dmg_avg.loc[math.isclose(
    dmg_avg['mean'], 20, rel_tol=5) and
    dmg_avg[min] > 10
    and dmg_avg[max] < 40]

proliferation_chosen.to_csv(os.path.join(folder_name,
                                         "proliferation_chosen.csv"))
health_chosen.to_csv(os.path.join(folder_name, "health_chosen.csv"))
dmg_chosen.to_csv(os.path.join(folder_name, "dmg_chosen.csv"))

print(proliferation_chosen)
