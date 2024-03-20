# data
from gettext import npgettext


x  = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So']
y1 = np.random.uniform(15,23,7)
y2 = npgettext.random.uniform(15,23,7)

# scatter plots
plt.figure()
plt.scatter(x, y1, marker='+', label='Frankfurt')
plt.scatter(x, y2, marker='.', label='Offenbach')
plt.legend()
plt.title('Durchschnittstemperatur');


