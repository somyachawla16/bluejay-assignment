from max_work import max_work
from shift_diff import shift_diff
from consecutive import get_consecutive_days



if __name__ == '__main__':

    print(f"Task 1: Who has worked for 7 consecutive days")
    data = get_consecutive_days()
    for key, value in data.items():
        print(f"{key} : {value}")

    print(f"Task 2: Who have less than 10 hours of time between shifts but greater than 1 hour")
    data = shift_diff()
    for key, value in data.items():
        print(f"{key} : {value}")

    print(f"Task 3: Who has worked for more than 14 hours in a single shift")
    data = max_work()
    for d in data:
        for key, value in d.items():
            print(f"{key}: {value}") 