import re
def f(dates):
    date_list = dates.split(',')
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return [d for d in date_list if re.match(pattern,d)]

if __name__ == "__main__":
    dates = "2021-1-3,05/12/2024,1998-12-11,9 maj 2007,2001-12-07,15-09-2011"
    print(f(dates))