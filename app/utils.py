def get_population(country_data):
    country_population = {
        '1970': int(country_data['1970 Population']),
        '1980': int(country_data['1980 Population']),
        '1990': int(country_data['1990 Population']),
        '2000': int(country_data['2000 Population']),
        '2010': int(country_data['2010 Population']),
        '2015': int(country_data['2015 Population']),
        '2020': int(country_data['2020 Population']),
        '2022': int(country_data['2022 Population'])
    }
    
    labels = country_population.keys()
    values = country_population.values()
    return labels, values


def country_data(data, country):
    return list(filter(lambda item: item['Country/Territory'] == country, data))

def get_mundial_population_percentages_of_continent(df, continent):
    # data = list(filter(lambda country: country['Continent'] == 'South America', data))
    # mundial_population = { country['Country/Territory']: country['World Population Percentage'] for country in data }
    # labels = mundial_population.keys()
    # values = mundial_population.values()

    df = df[df['Continent'] == continent]

    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values

    
    return countries, percentages
