#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
        #pass dialect as parameter for this function used to control how the csv parses or writes data 
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True) #empDialect removes any leading spaces while parsing CSV file
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
        #iterate over csv file and appen the dictionary to empty list
    employee_list = [] #initilize empty new list
    for data in employee_file:
       employee_list.append(data)
    return employee_list

employee_list = read_employees('file location here')

#grabs created employee list and processes that data into a new list
def process_data(employee_list):
    department_list = [] #initialize new list, iterate over employee_list and add only the departments into the department_list   
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_data):
        department_data[department_name] = department_list.count(department_name)
    return department_name

dictionary = process_data(employee_list)

def write_report(dictionary, report_file):
    with open(report_file, 'w+') as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
        f.close()

write_report(dictionary, 'dirpath/report.txt')