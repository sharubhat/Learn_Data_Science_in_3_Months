from sklearn import tree
from sklearn import naive_bayes
from sklearn import gaussian_process
from sklearn import neural_network

# ref : https://www.youtube.com/watch?v=T5pRlIbr6gg&index=1&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU

# get classifiers from http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html
# about classifiers : https://towardsdatascience.com/machine-learning-classifiers-a5cc4e1b0623
clf = tree.DecisionTreeClassifier()

# create 3 more classifiers
gnb = naive_bayes.GaussianNB()
gpc = gaussian_process.GaussianProcessClassifier()
mlcp = neural_network.MLPClassifier()

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

# CHALLENGE - ...and train them on our data
clf = clf.fit(X, Y)
gnb = gnb.fit(X, Y)
gpc = gpc.fit(X, Y)
mlcp = mlcp.fit(X, Y)

clf_prediction = clf.predict([[190, 70, 43]])
gnb_prediction = gnb.predict([[190, 70, 43]])
gpc_prediction = gpc.predict([[190, 70, 43]])
mlcp_prediction = mlcp.predict([[190, 70, 43]])

# CHALLENGE compare their results and print the best one!

print('Accuracy for DecisionTree: {}'.format(clf_prediction))
print('Accuracy for GaussianNB: {}'.format(gnb_prediction))
print('Accuracy for GaussianProcessClassifier: {}'.format(gpc_prediction))
print('Accuracy for MLPClassifier: {}'.format(mlcp_prediction))
