import pandas as pd
import os

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
    return dfc


folder_name = os.path.join(test_path, "proliferation_test")
proliferation_list = create_df_list(folder_name)
proliferation_avg = avg_cells_df(proliferation_list)
proliferation_avg.to_csv(os.path.join(folder_name, "Average"), index=False)

folder_name = os.path.join(test_path, "health_test")
health_list = create_df_list(folder_name)
health_avg = avg_cells_df(health_list)
health_avg.to_csv(os.path.join(folder_name, "Average"), index=False)

folder_name = os.path.join(test_path, "dmg_test")
dmg_list = create_df_list(folder_name)
dmg_avg = avg_cells_df(dmg_list)
dmg_avg.to_csv(os.path.join(folder_name, "Average"), index=False)
