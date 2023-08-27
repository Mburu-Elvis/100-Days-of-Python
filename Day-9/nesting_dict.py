capitals = {
    'France': 'Paris',
    'Germany': 'Berlin',
}

# nesting dictionaries inside dictionaries
travel_log = {
    'France': {'cities': ['Paris', 'Lille', 'Dijon'], "total_visits": 12},
    'Germany': {'cities': ['Berlin', 'Hamburg']}
}

# print(travel_log['France']['cities'][0])

# nesting dictionaries inside lists

travel_log1 = [
    {
        "Country": 'France', 
        'cities': ['Paris', 'Lille', 'Dijon'], "total_visits": 12
    },
    {
        "Country": 'Germany', 
        'cities': ['Berlin', 'Hamburg']
    },
]

print(travel_log1[0]["Country"])