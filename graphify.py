def graphify(test, holes, test_data):

    import matplotlib.pyplot as plt
    
    strength = [20, 40, 75, 150]

    if test == "SPT":
        plt.xlabel("SPT N-value")

    if test == "SV":
        plt.xlabel("Shear Vane result $(kN/m^2)$")
        plt.gca().set_xlim(0, 300)
        [plt.axvline(x, linewidth=1, color='silver', linestyle=(0, (5, 5))) for x in strength]
        plt.figtext(0.13, 0.85, "V.soft", fontsize=7, color="gray")
        plt.figtext(0.19, 0.85, "Soft", fontsize=7, color="gray")
        plt.figtext(0.25, 0.85, "Firm", fontsize=7, color="gray")

    if test == "HP":
        plt.xlabel("Hand Penetrometer result $(kN/m^2)$")
        plt.gca().set_xlim(0, 300)
        [plt.axvline(x, linewidth=1, color='silver', linestyle=(0, (5, 5))) for x in strength]

    for i in range(len(test_data)):

        x = []
        y = []

        for j in range(len(test_data[i])):

            x.append(float(test_data[i][j][1]))
            y.append(test_data[i][j][0])

        plt.plot(x, y, linestyle="-", label=holes[i][0])
    
    plt.ylabel("Depth $(m)$")
    plt.gca().invert_yaxis()
    plt.legend()
    plt.show()

