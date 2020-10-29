import xlrd

class OpertionExcel:
    def __init__(self,path,sheet_name):
        self.workbook = xlrd.open_workbook(path)
        self.sheet=self.workbook.sheet_by_name(sheet_name)

    def get_row(self):
        return self.sheet.nrows

    def get_ncol(self):
        return self.sheet.ncols

    def get_cell(self,row,col):
        cell_v=self.sheet.cell_value(row,col)
        if cell_v== 'null':
            cell_v= ''
        return cell_v
#
#
# if __name__=='__main__':
#     opertion=OpertionExcel('D:\\11.xlsx','Sheet1')
#     print(opertion.get_cell(0,0))
# import yaml
# with open('test.yaml') as yaml_file:
#     data=yaml.load(yaml_file,yaml.FullLoader)
# print(data)
#
#


