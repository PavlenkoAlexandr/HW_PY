from application.salary import calculate_salary
from application.db.people import get_employees
import datetime


def get_time():
    print(datetime.datetime.date(datetime.datetime.now()))


if __name__ == '__main__':

    get_time()
    calculate_salary()
    get_employees()
