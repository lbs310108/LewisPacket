import openpyxl


# input excel filename, first_item, end_item, sheet_name,return a list
def xl_list(filename, first_item, end_item, sheet_name):
    wb = openpyxl.load_workbook(filename)
    ws = wb[sheet_name]
    list_cell = []
    for row in ws[first_item:end_item]:
        for cell in row:
            list_cell.append(cell.value)

    return list_cell







