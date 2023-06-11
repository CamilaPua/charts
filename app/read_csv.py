import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        
        for row in reader:
            iterable = zip(header, row)
            country_dict = { header:row for header, row in iterable }
            data.append(country_dict)
    
    return data


if __name__ == '__main__':
    data = read_csv('./world_population.csv')
    print(data)

# import csv

# def read_csv(path):
#    # Tu código aquí 👇
#    with open(path, 'r') as csvfile:
#         total = 0
#         total = sum(int(pair[1]) for pair in csv.reader(csvfile))
#         return total


# response = read_csv('./app/data.csv')
# print(response)

