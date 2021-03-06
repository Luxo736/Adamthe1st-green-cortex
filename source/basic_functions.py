# python 3.5.2

#package name (lib)
import openpyxl 

# fnction to read excel file and return a list of values in cell renage
# input: file_name is a string representing name of xls file to read e.g. 'ram.xlsx'
#        cell_range is a string representing range of cells to be read e.g. "A5:A10"
# output: data a list containing the values of the cells specified e.g. values of A5:A10

def read_file(file_name,cell_range):
    # check whether file_name,cell_range is empty or not
    if len (file_name) == 0:
        return None
    elif len(cell_range) == 0:
        return None   
    else :
        wb = openpyxl.load_workbook(file_name)    
        sheet=wb.active
        data = []
        for cell in sheet[cell_range]:  
            data.append(cell[0].value)
        return data

#data = read_file('ram.xlsx',"")    
#print(data)

