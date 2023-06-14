import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./images/{name}.png')


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig(f'./images/pie.png')
    # plt.savefig(f'./images/{name}.png')


if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [150, 200, 800]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)

