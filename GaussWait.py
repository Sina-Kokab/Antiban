import random, math

def select(container, weights):
    total_weight = float(sum(weights))
    rel_weight = [w / total_weight for w in weights]

    # Probability for each element
    probs = [sum(rel_weight[:i + 1]) for i in range(len(rel_weight))]

    slot = random.random()
    for (i, element) in enumerate(container):
        if slot <= probs[i]:
            break

    return element


def RandomWaits(min, max):
    list = []
    waittimes = []
    weightpercentages = []

    mean = (min+max)/2
    print("Mean - " + str(mean))

    SD1 = (min - mean)**2

    SD2 = (max - mean)**2
    print("SD1 " + str(SD1) + " SD2 " + str(SD2))

    standard_deviation = (math.sqrt(SD1) + math.sqrt(SD2))/2
    print("Standard Deviation: " + str(standard_deviation))

    # Code up to here calculates standard deviation

    totalprobability = 0
    totalprobabilityadjusted = 0
    x = min

    while (x <= max):

        probabilitydensityfunction = 1/math.sqrt(2*math.pi*standard_deviation**2) * math.e**-(((x - mean)**2)/(2*standard_deviation**2)) #Calculates f(x) of probability density function

        list.append(probabilitydensityfunction)
        waittimes.append(x)
        x += 1

        totalprobability += probabilitydensityfunction

        if (len(list) == (max - min + 1)):
            probabilitycoefficient = 1/totalprobability #Calculates a multiplier for the probabilities calculated; they don't add up to 1?
            print("Probability Coefficient " + str(probabilitycoefficient))

            i = 0

            while i < len(list):
                adjustedprobability = probabilitycoefficient * list[i]
                print("PDF " + str(i) + " is "  + str(adjustedprobability))
                weightpercentages.append(adjustedprobability * 100) #Converts probabilities to percentages
                totalprobabilityadjusted += (adjustedprobability)
                i += 1


    #print("Total Adjusted Probability = " + str(totalprobabilityadjusted))

    #print(weightpercentages)

    return (select(waittimes, weightpercentages))
