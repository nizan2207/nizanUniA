import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.cross_validation import KFold  # For K-fold cross validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import metrics

df = pd.read_csv("C:/Users/USER/Downloads//train_Loan.csv")
print(df)
for col in df:
    print(df[col].value_counts(), '\n')
print(df.dtypes)
df[pd.notnull(df["Gender"])]
def binning(col, cut_points, labels=None):
    minval = col.min()
    maxval = col.max()    # create list by adding min and max to cut_points
    break_points = [minval] + cut_points + [maxval]# if no labels provided, use default labels 0 ... (n-1)
    if not labels:
        labels = range(len(cut_points)+1)
    colBin = pd.cut(col, bins=break_points, labels=labels, include_lowest=True)
    return colBin
bins = [100, 200, 300]
group_names = ['Low', 'Medium', 'High', 'Extreme']
df["LoanAmount_Bin"] = binning(df["LoanAmount"], bins, group_names)
print (pd.value_counts(df["LoanAmount_Bin"], sort=False))
print(df)
# Keep only the ones that are within +3 to -3 standard deviations in the column 'LoanAmount'.
print(df[(np.abs(df.LoanAmount-df.LoanAmount.mean()) <= (3*df.LoanAmount.std()))])
df['Normalized_Income'] = df['ApplicantIncome'].apply((lambda x: 0.5*np.sqrt(x)))
print(df['Education'])
df_Education = pd.get_dummies(df['Education'])
df = df.join(df_Education)
#print(df['Graduate'],df['Not Graduate'])
for i in df.columns:
    if df[i].dtype == object:
        a = pd.get_dummies(df[i])
        df[i] = a

#print(df)


def classification_model(model, data, predictors, outcome):
    # Fit the model:
    model.fit(data[predictors], data[outcome])
    # Make predictions on training set:
    predictions = model.predict(data[predictors])
    # Print accuracy
    accuracy = metrics.accuracy_score(predictions, data[outcome])
    print("Accuracy : %s" % "{0:.3%}".format(accuracy))
    # Perform k-fold cross-validation with 5 folds
    kf = KFold(data.shape[0], n_folds=5)
    error = []
    for train, test in kf:
        # Filter training data
        train_predictors = (data[predictors].iloc[train, :])
        # The target we're using to train the algorithm.
        train_target = data[outcome].iloc[train]
        # Training the algorithm using the predictors and target.
        model.fit(train_predictors, train_target)
        # Record error from each cross-validation run
        error.append(model.score(data[predictors].iloc[test, :], data[outcome].iloc[test]))
    print("Cross-Validation Score : %s" % "{0:.3%}".format(np.mean(error)))
    # Fit the model again so that it can be refered outside the function:
    model.fit(data[predictors], data[outcome])
myModel = DecisionTreeClassifier()
predictor_var = df.columns
predictor_var.remove('Loan_Status')
outcome_var = 'Loan_Status'
classification_model(myModel,df,predictor_var,outcome_var)
def visualize_tree(tree, feature_names):
    """Create tree png using graphviz.
        Args    ----    tree -- scikit-learn DecisionTree.    feature_names -- list of feature names.    """
    with open("dt.dot", 'w') as f:
        export_graphviz(tree, out_file=f,feature_names=feature_names, class_names=['No', 'Yes'])
        command = ['dot', '-Tpng', 'dt.dot', '-o', 'dt.png']
        try:
            subprocess.check_call(command)
        except:
            exit("Could not run dot, ie graphviz, to ""produce visualization")
visualize_tree(model, predictors)
df.to_csv(r'C:\Users\USER\Desktop\ניצן אוניברסיטה שנה א\מבוא להנדסת נתונים\train_Loan_uptaded.csv')