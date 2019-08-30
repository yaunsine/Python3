import xlrd

def read_excel():
    f = xlrd.open_workbook('D:\\IPsave.xls')
    mysheet = f.sheets()
    mysheet1 = mysheet[0]
    mycol = mysheet1.col_values(0)
    mycol.pop(0)
    print(mycol)

if __name__ == '__main__':
    read_excel()
