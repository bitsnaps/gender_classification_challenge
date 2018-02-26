# Desicion tree example

# Dependencies:
# Scikit-learn (http://scikit-learn.org/stable/install.html)
# numpy (pip install numpy)
# scipy (pip install scipy)

from sklearn import tree
import random as r

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']
     
print("Size: %d" % len(X))

# Create a classifier
clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

# Generating random values
values = [r.randint(150,220), r.randint(50,130), r.randint(37,50)]
prediction = clf.predict([values])

print("Prediction for %s " % values)
print(prediction)
