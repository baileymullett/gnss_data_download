import numpy as np

file = open("authorization_code.txt")

line = file.read().replace("\n", " ")
file.close()

start_year = 2012
end_year = 2021

url = 'https://data-idm.unavco.org/archive/gnss/rinex/obs/{year}/{day}/gls1{day}0.{year_digits}d.Z --header {code}'
calls = []
command = 'curl -L -O -f '

years = np.arange(start_year, end_year + 1)

for n in years:
    days = np.arange(1,367)
    year = str(n)
    year_digits = year[2:]
    for i in days:
        day = f'{i:03d}'
        year = n
        call = command + url.format(year = year, day = day, year_digits = year_digits, code = line) 
        calls.append(call)

test_calls = calls

with open('test_calls.sh', 'w') as f:
    for i in test_calls:
        f.write(i)
        f.write('\n')

