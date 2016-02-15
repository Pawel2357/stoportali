import numpy as np

import csv
file_data = self.request.get('file_in')
file_data_list = file_data.split('\n')
file_Reader = csv.reader(file_data_list)
for fields in file_Reader:
    print row