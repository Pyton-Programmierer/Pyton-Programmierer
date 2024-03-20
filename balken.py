from matplotlib import pyplot as plt
import numpy as np


tiere = ('Katzen', 'Hunde', 'Kleintiere', 'Ziervögel')
anzahl = [15.7, 10.7, 5, 3.5]
 
y_pos = np.arange(len(tiere))
 
plt.bar(y_pos, anzahl, align='center')
plt.xticks(y_pos, tiere)
plt.ylabel('Anzahl in Millionen')
plt.title('Haustiere in Deutschland (2020)')
# Striche auf x-Achse ausschalten
plt.tick_params(
    axis='x',
    which='both', #major und minor ticks
    bottom=False  # ticks auf der x-Achse (unten)
)
plt.show()