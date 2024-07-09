import pandas as pd
import os
folder_path = os.path.join(os.getcwd(), "tests")
folder_path = os.path.join(folder_path, "no-hip")
test_path = os.path.join(folder_path, "mixed")
folder_name = os.path.join(test_path, "tests")


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


def avg_cells_df(df_list, folder_name):
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
        dfc["mean"] = dfc.iloc[:, : 5].mean(axis=1)
        dfc["min"] = dfc.iloc[:, : 5].min(axis=1)
        dfc["max"] = dfc.iloc[:, : 5].max(axis=1)
    dfc.to_csv(os.path.join(folder_name, "Averages.csv"), index=False)
    return dfc


df_list = create_df_list(folder_name)
folder_name = os.path.join(test_path, "results")
if os.listdir(folder_name) == []:
    averages = avg_cells_df(df_list, folder_name)
else:
    averages = pd.read_csv(os.path.join(folder_name, "Averages.csv"))

avg_chosen = averages.loc[
    (averages['min'] >= 2)
    & (averages['max'] < 50)
    & (averages['mean'] > 15)]

print(len(avg_chosen))
avg_chosen.to_csv(os.path.join(folder_name, "Chosen.csv"), index=False)
