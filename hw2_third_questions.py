#HW2 Third Questions

## Question 7
def total_registered_cases (case_list,country_name):
    total=0
    if country_name in case_list:
        total = sum (case_list[country_name])
    return total

## Question 8
def total_registered_cases_per_country(case_list):
    total_cases_country = {}
    for country,cases in case_list.items():
        total_cases_country[country] = sum (cases)
    return total_cases_country

## Question 9
def country_with_most_cases(case_list):
    max_cases = 0
    for country,cases in case_list.items():
        total_cases = sum(cases)
        if total_cases > max_cases:
            max_cases = total_cases
            country_with_most_cases = country
    return country_with_most_cases