import utils, read_csv, charts

def run():
    data = read_csv.read_csv('./world_population.csv')

    labels, values = utils.get_mundial_population(data)
    charts.generate_pie_chart(labels, values)

    country = input('Type Country: ')

    country_data = utils.country_data(data, country)

    if len(country_data) > 0:
        country_data = country_data[0]
        labels, values = utils.get_population(country_data)

        charts.generate_bar_chart(labels, values)


if __name__ == '__main__':
    run()

