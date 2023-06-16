import utils, read_csv, charts
import pandas as pd

def run():
    df = pd.read_csv('./app/world_population.csv')


    continent = input('Type continent: ').title()
    labels, values = utils.get_mundial_population_percentages_of_continent(df, continent)
    charts.generate_pie_chart(labels, values)


    data = read_csv.read_csv('./app/world_population.csv')
    country = input('Type Country: ').title()
    country_data = utils.country_data(data, country)

    if len(country_data) > 0:
        country_data = country_data[0]
        labels, values = utils.get_population(country_data)

        charts.generate_bar_chart(country, labels, values)


if __name__ == '__main__':
    run()

