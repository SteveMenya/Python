from dotenv import load_dotenv

from DBConnection.data_utilities import get_all_employees

load_dotenv()

employees = get_all_employees()

for employee in employees:
    print(employee)
