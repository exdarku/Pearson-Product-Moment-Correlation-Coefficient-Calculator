from columnar import columnar
from os import system
import math 
from scipy.stats import pearsonr
import numpy as np
import matplotlib.pyplot as plt

system("title Pearson Product Moment Correlation ^| Laurence Lesmoras")

def header():
    print("===================================================================")
    print("Pearson Product Moment Correlation Coefficient Calculator")
    print("Created by exdarku\n\nhttps://laurencelesmoras.dev")
    print("===================================================================")
    

def menu():
    list = []
    header()
    print("Type 'done' after inputting")
    def loop():
        number = 0
        x_list = []
        y_list = []
        while True:
            number = number + 1
            x = input("[X >>] ")
            if x == "done":
                calculate(number, x_list, y_list)
                break
            x_list.append(int(x))
            y = input("[Y >>] ")
            y_list.append(int(y))
            print(f"<< INPUT DONE - {number} >>")
    loop()

def calculate(number, x_list, y_list):
    system("cls")
    new_list = []
    xy = []
    xs = []
    ys = []
    number = 0
    legit_number = 1
    for i in x_list:
        
        new_list.append([legit_number, int(x_list[number]), int(y_list[number]), int(x_list[number]) * int(y_list[number]), int(x_list[number]) ** 2, int(y_list[number]) ** 2])

        xy.append(int(int(x_list[number]) * int(y_list[number])))
        xs.append(int(int(x_list[number]) ** 2))
        ys.append(int(int(y_list[number]) ** 2))
        number = number + 1
        legit_number = legit_number + 1

        

    header()
    print("\n")
        
    data = columnar(data=new_list, headers=["Child", "X", "Y", "XY", "x^2", "y^2"], no_borders=True) # Creating Table
    print(data)

    sum_x = sum(x_list)
    sum_y = sum(y_list)
    sum_xy = sum(xy)
    sum_xs = sum(xs)
    sum_ys = sum(ys)

    x_array = np.array(x_list)
    y_array = np.array(y_list)
    solve = pearsonr(x_list, y_list)[0]


    print(f"\nSummation of X: {sum_x}")
    print(f"Summation of Y: {sum_y}")
    print(f"Summation of XY: {sum_xy}")
    print(f"Summation of x^2: {sum_xs}")
    print(f"Summation of y^2: {sum_ys}")
    print(f"\nPearson Product Final Answer: {solve}")
    print(f"Pearson Product Rounded Answer: {round(solve, 4)}")
    print("\n\n")
    print("CLOSE PLOT WINDOW TO PROCEED")
    plt.figure(figsize=(8,6))
    plt.scatter(x_list,y_list)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    answer = input("Calculate again? [Y/N]: ")
    if answer.lower() == "y":
        system('cls')
        menu()
    else:
        system.exit()

menu()
