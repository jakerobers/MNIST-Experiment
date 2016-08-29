import numpy as np  
import struct
from sklearn.svm import SVC

class ImageRecognition:

  def __init__(self):
    self.TRAIN_CHUNK = 1
    self.LABEL_CHUNK = 1
  #END __init__


  def predict(self, test_file, label_file):
    test_data = []
    label_data = []
    num_of_images = 5000
    num_of_rows = 28
    num_of_columns = 28

    # Remove header
    magic = test_file.read(32)
    label_file.read(16)

    for n in range(0, num_of_images):
      image = []
      for i in range(0, num_of_rows):
        for j in range(0, num_of_columns):
          images.append(struct.unpack("h", test.read(self.TRAIN_CHUNK)))
        #END for
      #END for

      test_data.append(image)
      label_data.append(struct.unpack("h", label_file.read(self.LABEL_CHUNK)))
    #END for

    return self.clf.score(np.array(test_data), np.array(label_data))

  #END predict

  def train(self, train_file, label_file):
    train_data = []
    label_data = []
    num_of_images = 60000
    num_of_rows = 28
    num_of_columns = 28

    # Remove header
    print("Reading train_file header: " + struct.unpack("h", train_file.read(32)))
    print("Reading label_file header: " + struct.unpack("h", label_file.read(16)))

    for n in range(0, num_of_images):
      image = []
      for i in range(0, num_of_rows):
        for j in range(0, num_of_columns):
          chunk = struct.unpack("h", train_file.read(self.TRAIN_CHUNK))
          print(chunk)
          image.append(chunk)
        #END for
      #END for

      train_data.append(image)
      label_data.append(struct.unpack("h", label_file.read(self.LABEL_CHUNK)))
    #END for

    self.clf = SVC()
    self.clf.fit(np.array(train_data), np.array(label_data))
    return
  #END train
#END ImageRecognition



train_file_object       = open('train-images-idx3-ubyte', 'rb')
label_file_object       = open('train-labels-idx1-ubyte', 'rb')
test_file_object        = open('t10k-images-idx3-ubyte', 'rb')
verify_file_object      = open('t10k-labels-idx1-ubyte', 'rb')

predictor = ImageRecognition()
predictor.train(train_file_object, label_file_object)
results = predictor.predict(test_file_object, verify_file_obkect)

train_file_object.close()
label_file_object.close()
test_file_object.close()
verify_file_object.close()

print(results)

