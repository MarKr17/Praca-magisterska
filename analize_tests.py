import pandas as pd
import os

folder_path = os.path.join(os.getcwd(), "tests")
folder_path = os.path.join(folder_path, "no-hip")
test_path = os.path.join(folder_path, "general")
folder_name = os.path.join(test_path, "proliferation_test")


def analize(folder_name):
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
    print(df_list)


analize(folder_name)
