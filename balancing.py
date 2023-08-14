import numpy as np
import scipy.linalg as la
import sys

# Balancing chemical equations using linear algebra
def main():
    # Get the chemical equation
    equation = input("Enter the chemical equation: ")
    equation = equation.split(" = ")
    reactants = equation[0].split(" + ")
    products = equation[1].split(" + ")

    # Get the elements
    elements = []
    for i in reactants:
        for j in i:
            if j.isalpha() == True and j.islower() == False:
                elements.append(j)
    for i in products:
        for j in i:
            if j.isalpha() == True and j.islower() == False:
                elements.append(j)
    elements = list(set(elements))
    elements.sort()

    # Get the coefficients
    coefficients = []
    for i in reactants:
        coefficients.append(i.split(" "))
    for i in products:
        coefficients.append(i.split(" "))
    for i in range(len(coefficients)):
        for j in range(len(coefficients[i])):
            if coefficients[i][j].isalpha() == True:
                coefficients[i][j] = 1
            else:
                coefficients[i][j] = int(coefficients[i][j])
    coefficients = np.array(coefficients)

    # Get the matrix
    matrix = np.zeros((len(elements), len(coefficients)))
    for i in range(len(elements)):
        for j in range(len(coefficients)):
            if elements[i] in coefficients[j]:
                matrix[i][j] = coefficients[j][coefficients[j].index(elements[i])+1]
    matrix = matrix.astype(int)

    # Get the null space
    nullSpace = la.null_space(matrix)

    # Get the coefficients
    coefficients = []
    for i in nullSpace:
        coefficients.append(i[0])
    coefficients = [int(i) for i in coefficients]

    # Print the balanced equation
    balancedEquation = ""
    for i in range(len(reactants)):
        balancedEquation += str(coefficients[i]) + reactants[i] + " + "
    balancedEquation = balancedEquation[:-3] + " = "
    for i in range(len(reactants), len(coefficients)):
        balancedEquation += str(coefficients[i]) + products[i-len(reactants)] + " + "
    balancedEquation = balancedEquation[:-3]
    print(balancedEquation)
    

main()