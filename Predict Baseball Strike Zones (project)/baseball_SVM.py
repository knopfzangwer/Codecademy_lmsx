import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz
import seaborn as sns

# print(aaron_judge.columns)
# print(aaron_judge.description.unique())

# S = strike, B = ball, X = nenhum dos dois
print(aaron_judge.type.unique())

aaron_judge['type'] = aaron_judge['type'].map({'S':1, 'B':0})
print(aaron_judge.type.unique())

print(aaron_judge['plate_x'])

aaron_judge = aaron_judge.dropna(subset = ['type', 'plate_x', 'plate_z'])
print(aaron_judge.type.unique())

plt.scatter(aaron_judge['plate_x'], aaron_judge['plate_z'], c=aaron_judge['type'], cmap = plt.cm.coolwarm, alpha = 0.25)
plt.show()
plt.close()

training_set, validation_set = train_test_split(aaron_judge, random_state = 1)

training_data = training_set[['plate_x', 'plate_z']]
training_label = training_set['type']

classifier = SVC(kernel = 'rbf', gamma=10, C=1)
classifier.fit(training_data, training_label)

fig, ax = plt.subplots()
plt.scatter(aaron_judge['plate_x'], aaron_judge['plate_z'], c=aaron_judge['type'], cmap = plt.cm.coolwarm, alpha = 0.25)
draw_boundary(ax, classifier)
plt.show()

validation_data = validation_set[['plate_x', 'plate_z']]
validation_label = validation_set['type']

print(classifier.score(validation_data, validation_label))

print(david_ortiz['plate_x'])
print(david_ortiz['plate_z'])

def scatter(dataset1, dataset2, dataset3, palette, name):
  # Set up layout
  fig, axs = plt.subplots(1, 3, figsize=(18, 7))

  # Draw plots
  sns.scatterplot(x=dataset1.plate_x, y=dataset1.plate_z, hue=dataset1.type, palette=palette[0], alpha=0.5, legend='brief', s=60, ax=axs[0])
  sns.scatterplot(x=dataset2.plate_x, y=dataset2.plate_z, hue=dataset2.type, palette=palette[1], alpha=0.5, legend='brief', s=60, ax=axs[1])
  sns.scatterplot(x=dataset3.plate_x, y=dataset3.plate_z, hue=dataset3.type, palette=palette[2], alpha=0.5, legend='brief', s=60, ax=axs[2])

  # Set up titles
  axs[0].set_title(name[0] + 'Strikes and Balls Ratio', fontsize='large')
  axs[1].set_title(name[1] + 'Strikes and Balls Ratio', fontsize='large')
  axs[2].set_title(name[2] + 'Strikes and Balls Ratio', fontsize='large')

  # Set up legends
  for ax in axs:
      ax.legend(title='Pitch Type', labels=['Ball', 'Strike'])

  # Set up labels
  axs[0].set_xlabel(None)
  axs[1].set_xlabel('Plate X', fontsize='large')
  axs[2].set_xlabel(None)

  axs[0].set_ylabel('Plate Z', fontsize='large')
  axs[1].set_ylabel(None)
  axs[2].set_ylabel(None)

  fig.tight_layout()
  return plt.show()

scatter(
    aaron_judge,
    jose_altuve,
    david_ortiz,
    palette=['seismic', ['Green', 'Purple'], ['LimeGreen', 'HotPink']],
    name=['Aaron Judge\'s ', 'Jose Altuve\'s ', 'David Ortiz\'s ']
)
