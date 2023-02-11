"""
	4 - Optuna

Optuna is a library to get the best parameters to train your model
"""
# df.corrwith(df['TARGET'])*100

from sklearn.metrics import precision_score, accuracy_score, recall_score
from sklearn.neighbors import KNeighborsClassifier
import optuna

# ---- MODEL ----
def knn_classifier_optuna (trial, x_train=x_train, x_test=x_test, y_train=y_train, y_test=y_test):
    # define parameters
    params = {
    'n_neighbors'     : trial.suggest_categorical('n_neighbors', [1,3,5,7]), 
    'weights'         : trial.suggest_categorical('weights', ['uniform','distance']),
    'algorithm'       : trial.suggest_categorical('algorithm',['auto','ball_tree','kd_tree','brute']),
    'leaf_size'       : trial.suggest_int('leaf_size', 30, 150),
    'p'               : trial.suggest_int('p', 2, 50),
    
    }
    
    # creat model anf pass parameters 
    model = KNeighborsClassifier(**params)
    model.fit(x_train, y_train) 
    predection = model.predict(x_test)
    acc = accuracy_score(y_test, predection)
    return acc

# ---- OPTUNA IMPROVEMENT AND STUDY ----
# Need to execute only once.
study = optuna.create_study(direction="minimize")

study.optimize(knn_classifier_optuna, n_trials=200)

print("Number of finished trials: ", len(study.trials))
print("Best trial:")

trial = study.best_trial

print("  Value: {}".format(trial.value))
print("  Params: ")


params = []

for key, value in trial.params.items():
    params.append(value)
    print("    {}: {}".format(key, value))

# ---- TRAINING PERFECT MODEL ----
knn_best = KNeighborsClassifier(n_neighbors=7,weights='uniform',algorithm='auto',leaf_size=32,p=27)

knn_best.fit(x_train,y_train)
y_pred_knn = knn_best.predict(x_test)
y_pred_train_knn   = knn_best.predict(x_train)

print("Percition   using KNN  on test  Data  : {:.2f} %".format(np.round(precision_score(y_test, y_pred_knn),4)*100))
print("Recall      using KNN  on test Data   : {:.2f} %".format(np.round(recall_score(y_test, y_pred_knn),4)*100))
print("Accurcy     using KNN  on test Data   : {:.2f} %".format(np.round(accuracy_score(y_test, y_pred_knn),4)*100))