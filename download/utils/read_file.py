import pandas as pd


def read_excel_file(file, sheet_name=None):
    """
    Чтение Excel файла и запись всех данных в список
    """
    if sheet_name is None:
        data = pd.read_excel(file)
    else:
        data = pd.read_excel(file, sheet_name=sheet_name)

    return data.values.tolist()