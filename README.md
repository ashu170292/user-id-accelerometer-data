# user-id-accelerometer-data

This is the repository for user identification using accelerometer data 
obtained from the [UCI Repository](https://archive.ics.uci.edu/ml/datasets/User+Identification+From+Walking+Activity).

The data looks like:

| Column Name        | Data Type           | 
| ------------- |:-------------:| 
|timestamp   | timestamp |
| x_acceleration      | float      | 
| y_acceleration | float      |
|z_acceleration | float |

There are 22 csv files corresponding to 22 persons, and the distribution looks 
like follows:

![logo]


[logo]: https://github.com/ashu170292/user-id-accelerometer-data/blob/main/graphs/dist.png "Logo Title Text 2"

It is evident from the above graph that we have less data corresponding to person id 3, 5,16 and 19.

**Feature Extraction:** 

Features were built in time domain as well as frequency domain
Features are calculated by taking a window of length of 100 samples and an overlap of 50%.
The time domain features are as follows:

|Features	|Count|
| ------------- |:-------------:|
Means of x component, y component and z component of acceleration| 	3
Min values of x component, y component and z component of accelaration|	3
Max values of x component, y component and z component of accelaration|	3
Mean of magnitude of accelearation|	1
Min of magnitude of acceleration|	1
Max of magnitude of acceleration|	1
Median of magnitude of acceleration|	1
Ratio of mean of x component and mean of z component|	1
Ratio of mean of y component and mean of z component|	1
Average of time difference between consecutive readings |       	1

The frequency domain features are as follows:

|Features|	Count|
| ------------- |:-------------:|
Mean of x component of FFT|	1
Mean of y component of FFT|	1
Mean of z component of FFT|	1
Median of x component of FFT|	1
Median of y component of FFT|	1
Median of z component of FFT|	1
Spectral Centroid of x component of FFT|	1
Spectral Centroid of y component of FFT|	1
Spectral Centroid of z component of FFT|	1

Thus overall, 25 time and frequency domain features were extracted.
Spectral centroid of an axis is the dot product between time domain acceleration vector and frequency domain FFT vector divided by the length of the vector

**Modeling:**

*Train-test split:* The feature data along with labels 
is split into 70/30 ratio into train data and
test data

*Base Model:*
A logistic regression model is chosen as a base 
model with features average acceleration and average 
time between observations. The accuracy of the model 
is 17%. The AUC of the model is 67%

*Training:*
Next, logistic regression was tried on all the 
time domain and frequency domain features. The 
performance of the base model motivates us to 
try models that would not necessarily separate 
classes by a linear boundary, hence random forest, 
AdaBoost and SVM were tried.

*Cross Validation:* – K fold cross validation 
technique was used for hyperparameter tuning, 
where k =3. This is so because this ensures 
lesser variance in the loss metric and helps in 
more robust choice of hyperparameters. Such a 
small value of K was chosen because of computational 
constraints.

Since this is a multi-class classification 
problem with 22 classes, one vs rest classifiers 
were built, meaning for each algorithm that was 
tried, 22 estimators were built for each class.

_Logistic regression:_ Logistic regression tries to separate classes through linear boundaries and the simplicity of the model motivates to put all the features in the logistic regression model. The L-BFGS technique was used as an optimization technique to reach convergence.

_Random Forest Model:_ Random Forest model with following hyperparameters were trained:
```
No of estimators: [20, 40, 60, 80, 100]
 Max features: ['auto', 'sqrt']
 Max depth: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, None]
 Min samples split: [2, 5, 10, 15, 25]
 Min samples leaf': [1, 2, 4, 6, 8, 10]
 Bootstrap: [True, False]
```
 


_AdaBoost Model:_ AdaBoost algorithm was used with base estimator as a decision tree classifier with max depth =2. A simple model is used as base estimator because boosting reduces bias of a model by learning from weak classifiers

_SVM:_ Support vector machine with linear support kernel is trained 

_Evaluation:_ The model is evaluated on precision, recall, accuracy and AUC. Overall model performance for the 4 models is as follows:

Model	|Precision	|Recall	|F1 score	|AUC	|Accuracy
| ------------- |:-------------:| :-------------:| :-------------:| :-------------:| :-------------:| 
Logistic	|0.67	|0.67	|0.66	|0.67	|0.67
SVM	|0.45	|0.36	|0.28	|-	|0.36
Random Forest	|0.86	|0.86	|0.86	|0.99	|0.86
AdaBoost	|0.86	|0.85	|0.85	|0.96	|0.85

The AUC for random forest suggests that the model is promising and its threshold can be tweaked to achieve better precision.

**Final Model:**
Random Forest is chosen as the final model as 
it shows the best AUC, precision, recall and F1 score.
 Both time and frequency domain features are important
  in identifying persons based on accelerometer data 
  with median features showing most importance. The 
  precision, recall and F1 score numbers for all 
  persons for the random forest model are as follows:
  ```
  Labels   precision    recall  f1-score   # test data

           1       1.00      0.91      0.96        35
           2       1.00      0.88      0.93        16
           3       0.88      0.83      0.86        36
           4       1.00      0.83      0.91        29
           5       0.90      0.79      0.84        34
           6       1.00      0.93      0.97        76
           7       0.85      0.74      0.79        23
           8       1.00      0.45      0.62        11
           9       0.70      0.92      0.80       134
          10       0.77      0.90      0.83       135
          11       0.75      1.00      0.86         6
          12       0.82      0.41      0.55        22
          13       0.98      0.97      0.97        98
          14       0.87      0.72      0.79        18
          15       0.82      0.77      0.80        43
          16       0.80      1.00      0.89         4
          17       0.79      0.84      0.82        37
          18       1.00      0.57      0.73         7
          19       0.96      0.90      0.93        30
          20       1.00      0.70      0.82        20
          21       0.89      0.65      0.76        26
          22       0.84      0.78      0.81        46

    accuracy                           0.85       886
   macro avg       0.89      0.80      0.83       886
weighted avg       0.86      0.85      0.85       886
```
