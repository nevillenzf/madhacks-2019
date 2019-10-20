from __future__ import absolute_import, division, print_function, unicode_literals

import pathlib2

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import tensorflow as tf
import csv

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import model_from_json, load_model

PATH = "./models"
def norm(x):
  return (x - train_stats['mean']) / train_stats['std']

def build_model():
    model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[len(train_dataset.keys())]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
    ])

    optimizer = tf.keras.optimizers.RMSprop(0.001)

    model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])
    return model

def plot_history(history):
  hist = pd.DataFrame(history.history)
  hist['epoch'] = history.epoch

  plt.figure()
  plt.xlabel('Epoch')
  plt.ylabel('Mean Abs Error [Score]')
  plt.plot(hist['epoch'], hist['mean_absolute_error'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mean_absolute_error'],
           label = 'Val Error')
  plt.ylim([0,5])
  plt.legend()

  plt.figure()
  plt.xlabel('Epoch')
  plt.ylabel('Mean Square Error [$Score^2$]')
  plt.plot(hist['epoch'], hist['mean_squared_error'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mean_squared_error'],
           label = 'Val Error')
  plt.ylim([0,20])
  plt.legend()
  plt.show()

class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0:
        print('Epoch {}'.format(epoch))
        print('')

    print('.', end='')

print("Loaded matplotlib, pandas, seaborn and tensorflow successfully.")

file_found = False
try:
    f = open('{}/model.json'.format(PATH), 'r')
    file_found = True
except:
    file_found = False


dataset_path = "./new_file.csv"
my_dict = []

column_names = ["Company_Name" ,"Account_Number","Country" ,"Reporting_Year","Ticker Symbol" ,
                "ISIN" ,"Disclosure_Score","Performance_Band", "Parent_Account" , "Permission",
                "Response_Status", "Scope_1", "Scope_2","Country_Location","Region","Score"]

raw_dataset = pd.read_csv(dataset_path, names=column_names,
                      na_values = "?", comment='\t',
                      sep=",", skipinitialspace=True)

dataset = raw_dataset.copy()
dataset = dataset.drop([0], axis=0)

#remove irrelevant data
acc_num = dataset.pop('Account_Number')
country = dataset.pop("Country")
report_year = dataset.pop("Reporting_Year")
ticker_sym = dataset.pop("Ticker Symbol")
isin = dataset.pop("ISIN")
perf_band = dataset.pop("Performance_Band")
parent_acc = dataset.pop("Parent_Account")
permission = dataset.pop("Permission")
res_sts = dataset.pop("Response_Status")
location = dataset.pop("Country_Location")
region = dataset.pop("Region")
name = dataset.pop("Company_Name")

#drop empty rows
dataset = dataset.dropna()

dataset['Disclosure_Score'] = dataset['Disclosure_Score'].astype(float)
dataset['Scope_1'] = dataset['Scope_1'].astype(float)
dataset['Scope_2'] = dataset['Scope_2'].astype(float)
dataset['Score'] = dataset['Score'].astype(float)

# 70 : 30 --- train : test split
train_dataset = dataset.sample(frac=0.7,random_state=0)
test_dataset = dataset.drop(train_dataset.index)

#sns.pairplot(train_dataset[["Disclosure_Score", "Scope_1", "Scope_2", "Score"]], diag_kind="kde")

train_stats = train_dataset.describe(include = 'all')
train_stats.pop("Score")
train_stats = train_stats.transpose()
print(train_stats)

train_labels = train_dataset.pop('Score')
test_labels = test_dataset.pop('Score')

normed_train_data = norm(train_dataset)
normed_test_data = norm(test_dataset)


if file_found is False:

    model = build_model()

    print(model.summary())

    example_batch = normed_train_data[:10]
    example_result = model.predict(example_batch)
    print(example_result)

    EPOCHS = 1000

    history = model.fit(
      normed_train_data, train_labels,
      epochs=EPOCHS, validation_split = 0.2, verbose=0,
      callbacks=[PrintDot()])

    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch

    #plot_history(history)
else:
    print("Loaded trained model. ")
    with open('{}/model.json'.format(PATH), 'r') as f:
        model = model_from_json(f.read())
    model.load_weights('{}/model.h5'.format(PATH))

optimizer = tf.keras.optimizers.RMSprop(0.001)

model.compile(loss='mse',
            optimizer=optimizer,
            metrics=['mae', 'mse'])

loss, mae, mse = model.evaluate(normed_test_data, test_labels, verbose=2)

print("Testing set Mean Abs Error: {:5.2f} Score".format(mae))

test_predictions = model.predict(normed_test_data).flatten()

plt.scatter(test_labels, test_predictions)
plt.xlabel('True Values [Score]')
plt.ylabel('Predictions [Score]')
plt.axis('equal')
plt.axis('square')
plt.xlim([0,plt.xlim()[1]])
plt.ylim([0,plt.ylim()[1]])
plt.plot([-100, 100], [-100, 100])
#plt.show()

error = test_predictions - test_labels
plt.hist(error, bins = 25)
plt.xlabel("Prediction Error [Score]")
plt.ylabel("Count")
#plt.show()

model.save_weights('{}/model.h5'.format(PATH))
# Save the model architecture
with open('{}/model.json'.format(PATH), 'w') as f:
    f.write(model.to_json())
