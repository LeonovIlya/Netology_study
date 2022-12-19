import application.db.people as PPL
from application.salary import calculate_salary as CS
from datetime import datetime

if __name__ == '__main__':
    print(datetime.now())
    PPL.get_employees()
    CS()
