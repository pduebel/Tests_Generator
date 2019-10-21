def graphify(holes, test_data):

    import matplotlib.pyplot as plt


    for i in range(len(test_data)):

        x = []
        y = []

        for j in range(len(test_data[i])):

            x.append(test_data[i][j][1])
            y.append(test_data[i][j][0])

        plt.plot(x, y, linestyle="-", label=holes[i][0])
    
    plt.legend()
    plt.show()

