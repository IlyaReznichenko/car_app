import openpyxl

class UploadExcel(object):
    def __init__(self, file):
        self.file = file
        if isinstance(self.file, object):
            self.excel_parser()
        else:
            print('Неверно передан объект')

    def excel_parser(self):
        open_excel_file = openpyxl.load_workbook(self.file)
        excel_sheet = open_excel_file["Sheet1"]
        excel_data = []

        for row in excel_sheet.iter_rows():
            row_data = []
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
        print(excel_data)
        self.excel_data = excel_data


