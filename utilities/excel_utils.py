import openpyxl

def read_excel_data(file_path, sheet_name="Sheet1"):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]

    # Read headers from first row
    headers = [str(cell.value).strip() for cell in sheet[1]]

    # Store each row as dict {header: value}
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if any(row):  # skip empty rows
            data.append(dict(zip(headers, row)))

    return data
