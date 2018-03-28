import xlrd


def from_excel(excel_path):
    dict_config = dict()
    workbook = xlrd.open_workbook(excel_path)
    for sheet in workbook.sheets():
        list_row_values = list()
        title = sheet.row_values(0)
        for x in xrange(1, sheet.nrows):
            dict_row_value = dict()
            row_value = sheet.row_values(x)
            for key in title:
                dict_row_value[key] = row_value[title.index(key)]
            list_row_values.append(dict_row_value)
        dict_config[sheet.name] = list_row_values
    return dict_config
