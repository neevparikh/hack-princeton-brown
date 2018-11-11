import pandas as pd
import numpy as np
from sklearn import preprocessing as pp
from sklearn.neural_network import MLPClassifier as mlc
from sklearn.model_selection import train_test_split
import pickle


def preprocess_and_train():
    df = pd.read_csv("train_feat_df.csv").dropna()
    del df["Unnamed: 0"]
    del df["Bachelor's Degree"]

    df["label"] = pd.Series(np.ones((df["population"].count(),), dtype=int))

    fake = pd.read_csv("fakefuck.csv")
    del fake["Unnamed: 0"]
    fake["label"] = pd.Series(
        np.zeros((fake["population"].count(),), dtype=int))

    merged = pd.concat([df, fake], sort=False).reset_index()
    del merged["index"]

    t_df = merged[list(merged.columns)[26:68]]

    l = list(merged.columns)[0:25]
    l.extend(list(merged.columns)[69:-1])

    s_df = merged[l]

    labels = merged["label"]

    s_x = pp.scale(s_df.values)
    X = np.concatenate((s_x, t_df.values), axis=1)

    y = labels.values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=5)

    clf = mlc(
        hidden_layer_sizes=(10,),
        activation="relu",
        solver="adam",
        alpha=0.0001,
        batch_size="auto"
    )

    print("Training...")
    
    trained_clf = clf.fit(X_train, y_train)
    y_prob = clf.predict_proba(X_test)
    y_pred = clf.predict(X_test)
    
    score = trained_clf.score(X_test, y_test)
    
    print("Score: ", score)
    print("Pickling...")
    pickle.dump(trained_clf, open("model.pkl", "wb"))


preprocess_and_train()
