calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return length, upper_case, lower_case


def is_contains(string, list_to_search):
    count_calls()
    lower_string = string.lower()
    lower_list = []
    for i in list_to_search:
        lower_list.append(i.lower())
    return lower_string in lower_list


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
