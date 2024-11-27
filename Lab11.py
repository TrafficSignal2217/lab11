# top of your program
import matplotlib.pyplot as plt

# Wherever you want to display the graph
plt.hist(scores, bins=[0,25,50,75,100])
plt.show()

while True:
    print('1. Student grade')
    print('2. Assignment statistics')
    print('3. Assignment graph\n')

    option = input('Enter your selection:')

    match (option):
        case '1':
            name = input('What is the student\'s name:')

        case _:
            print('Invalid input!')
            break

