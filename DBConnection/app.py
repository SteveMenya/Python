from dotenv import load_dotenv

from DBConnection.data_utilities import get_all_employees, create_employee_backup, drop_table, \
    insert_data_to_back_up_table

load_dotenv()

# Step1: drop table
drop_table()

# Step2: create table
table_name = create_employee_backup()

# Step3: Get All the data from employees table
employees = get_all_employees()

# Step4: insert all the data to the backup table
insert_data_to_back_up_table(table_name, employees)

for employee in employees:
    print(employee)
