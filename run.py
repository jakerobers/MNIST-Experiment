import numpy as np  
import struct
from mnist import MNIST
from collections import deque
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

def shape_data(features, labels, num_of_images):
  features = deque(features)
  labels = deque(labels)
  feature_data = []
  label_data = []

  for n in range(0, num_of_images):
    feature_data.append(features.popleft())
    label_data.append(labels.popleft())
  #END for

  return (feature_data, label_data)
#END shape_data

mndata = MNIST('./')
loaded_images, loaded_labels = mndata.load_training()
loaded_tests, loaded_actuals = mndata.load_testing()

features, labels = shape_data(loaded_images, loaded_labels, 10000)
test_features, test_labels = shape_data(loaded_tests, loaded_actuals, 500)

clf = SVC(kernel='poly', degree=2)
#clf = GaussianNB()
clf.fit(np.array(features), np.array(labels))
print(clf.score(np.array(test_features), np.array(test_labels)))
