import pandas as pd


def read_excel_file(file, sheet_name=None):
    """
    Чтение Excel файла и запись всех данных в список
    """
    if sheet_name is None:
        data = pd.read_excel(file)
    else:
        data = pd.read_excel(file, sheet_name=sheet_name)

    data_list = data.values.tolist()
    result = list()

    for line in data_list:
        if line[-1].isspace() or line[-1] == '-':
            result.append(line)
        else:
            line[-1] = 'Адрес: ' + line[-1]
            result.append(line)

    return result
