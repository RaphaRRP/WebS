import pandas as pd
import os

def converter():
    folder = "colombo\converter"
    output_folder = "colombo\convertido"
    for count, filename in enumerate(os.listdir(folder)):
        read_file = pd.read_excel(os.path.join(folder,filename))
        read_file.to_csv(os.path.join(output_folder,str('excel_file ') + str(count) + str('.csv')), index = None, header=True)

    print('convertido para csv')

