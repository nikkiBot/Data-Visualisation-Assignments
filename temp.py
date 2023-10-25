import requests

url = "https://www.piday.org/wp-json/millionpi/v1/million?action=example_ajax_request&page={page}"

final_number = []
for page in range(1, 3):
    data = requests.get(url.format(page=page)).text
    final_number.append(data[1:-1])

final_number = "".join(final_number)
# print(final_number)

# Calculate sum of first n digits of final_number
n = 314159
sum = 0
for digit in final_number: 
    if digit.isdigit():
        sum += int(digit)
    if n == 0:
        break
    n -= 1
print(sum)
