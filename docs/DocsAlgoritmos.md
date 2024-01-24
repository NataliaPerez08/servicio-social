# Bayes Ingenuo
https://www.datacamp.com/tutorial/naive-bayes-scikit-learn

Naive Bayes classifier calculates the probability of an event in the following steps:

Step 1: Calculate the prior probability for given class labels

Step 2: Find Likelihood probability with each attribute for each class

Step 3: Put these value in Bayes Formula and calculate posterior probability.

Step 4: See which class has a higher probability, given the input belongs to the higher probability class.

# Regresion lineal
https://www.geeksforgeeks.org/ml-linear-regression/
Linear regression is a type of supervised machine learning algorithm that computes the linear relationship between a dependent variable and one or more independent features. The goal of the algorithm is to find the best linear equation that can predict the value of the dependent variable based on the independent variables. The equation provides a straight line that represents the relationship between the dependent and independent variables. The slope of the line indicates how much the dependent variable changes for a unit change in the independent variable(s).


# Regresion Logistica
https://es.wikipedia.org/wiki/Regresi%C3%B3n_log%C3%ADstica
https://en.wikipedia.org/wiki/Logistic_regression

En estadística, la regresión logística es un tipo de análisis de regresión utilizado para predecir el resultado de una variable categórica (una variable que puede adoptar un número limitado de categorías) en función de las variables independientes o predictoras. Es útil para modelar la probabilidad de un evento ocurriendo en función de otros factores.

# Perceptron

Perceptron is an algorithm for supervised learning of binary classifiers that was introduced by Frank Rosenblatt in 1957.1 It is a linear classification algorithm that learns a decision boundary that separates two classes using a line in the feature space.0 During training, the weights and biases of the perceptron are adjusted to minimize the error between the predicted output and the true output for a given set of training examples.


# SVM Support Vector Machine / C-Support Vector Classification.
In machine learning, support vector machines (SVMs, also support vector networks) are supervised max-margin models with associated learning algorithms that analyze data for classification and regression analysis. 
The implementation (sklearn) is based on libsvm.
LIBSVM implements the sequential minimal optimization (SMO) algorithm for kernelized support vector machines (SVMs), supporting classification and regression.LIBLINEAR implements linear SVMs and logistic regression models trained using a coordinate descent algorithm.
References
1 LIBSVM: A Library for Support Vector Machines <http://www.csie.ntu.edu.tw/~cjlin/papers/libsvm.pdf>
2 Platt, John (1999). "Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods <https://citeseerx.ist.psu.edu/doc_view/pid/42e5ed832d4310ce4378c44d05570439df28a393>

# Random Forest Classifier
Random forests or random decision forests is an ensemble learning method for classification, regression and other tasks that operates by constructing a multitude of decision trees at training time. For classification tasks, the output of the random forest is the class selected by most trees. For regression tasks, the mean or average prediction of the individual trees is returned. Random decision forests correct for decision trees' habit of overfitting to their training set.
## Decision tree learning
Decision tree learning is a supervised learning approach used in statistics, data mining and machine learning. In this formalism, a classification or regression decision tree is used as a predictive model to draw conclusions about a set of observations.

Tree models where the target variable can take a discrete set of values are called classification trees; in these tree structures, leaves represent class labels and branches represent conjunctions of features that lead to those class labels. Decision trees where the target variable can take continuous values (typically real numbers) are called regression trees. More generally, the concept of regression tree can be extended to any kind of object equipped with pairwise dissimilarities such as categorical sequences.