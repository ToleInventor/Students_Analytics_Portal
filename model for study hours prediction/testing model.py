import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# loading the dataset
csv = pd.read_csv("Hours.csv")

# clean the data (inplace)
csv.dropna(inplace=True)

# drop all rows that have at least one zero value
csv = csv.loc[(csv != 0).all(axis=1)]

# setup the features target for each model
def mathe():
    return 7

def eng(data):
    df = csv.copy()
    df.drop(["KISW", "BIO", "RE", "PHY", "CHE", "HIST", "GEO", "COMP", "BUS", "MATH"], axis=1, inplace=True)
    X = df.drop("ENG", axis=1)
    y = df["ENG"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    data_df = pd.DataFrame(data, columns=X.columns)
    pred = model.predict(data_df)
    return math.trunc(pred[0])

def kisw(data):
    df = csv.copy()
    df.drop(["RE", "ENG", "BIO", "PHY", "CHE", "HIST", "GEO", "COMP", "BUS", "MATH"], axis=1, inplace=True)
    X = df.drop("KISW", axis=1)
    y = df["KISW"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    data_df = pd.DataFrame(data, columns=X.columns)
    pred = model.predict(data_df)
    return math.trunc(pred[0])

def bio(data):
    df = csv.copy()
    df.drop(["KISW", "ENG", "PHY", "CHE", "RE", "HIST", "GEO", "COMP", "BUS", "MATH"], axis=1, inplace=True)
    X = df.drop("BIO", axis=1)
    y = df["BIO"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    data_df = pd.DataFrame(data, columns=X.columns)
    pred = model.predict(data_df)
    return math.trunc(pred[0])

def phy(data):
    df = csv.copy()
    df.drop(["KISW", "BIO", "ENG", "CHE", "RE", "HIST", "GEO", "COMP", "BUS", "MATH"], axis=1, inplace=True)
    X = df.drop("PHY", axis=1)
    y = df["PHY"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    data_df = pd.DataFrame(data, columns=X.columns)
    pred = model.predict(data_df)
    return math.trunc(pred[0])

def che(data):
    df = csv.copy()
    df.drop(["KISW", "BIO", "PHY", "RE", "ENG", "HIST", "GEO", "COMP", "BUS", "MATH"], axis=1, inplace=True)
    X = df.drop("CHE", axis=1)
    y = df["CHE"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    data_df = pd.DataFrame(data, columns=X.columns)
    pred = model.predict(data_df)
    return math.trunc(pred[0])

def hist(data):
    df = csv.copy()
    df.drop(["RE", "KISW", "BIO", "PHY", "CHE", "ENG", "GEO", "COMP", "BUS", "MATH"], axis=1, inplace=True)
    X = df.drop("HIST", axis=1)
    y = df["HIST"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    data_df = pd.DataFrame(data, columns=X.columns)
    pred = model.predict(data_df)
    return math.trunc(pred[0])

def geo(data):
    df = csv.copy()
    df.drop(["RE", "KISW", "BIO", "PHY", "CHE", "HIST", "ENG", "COMP", "BUS", "MATH"], axis=1, inplace=True)
    X = df.drop("GEO", axis=1)
    y = df["GEO"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    data_df = pd.DataFrame(data, columns=X.columns)
    pred = model.predict(data_df)
    return math.trunc(pred[0])

def comp(data):
    df = csv.copy()
    df.drop(["KISW", "BIO", "PHY", "CHE", "HIST", "GEO", "ENG", "BUS", "MATH", "RE"], axis=1, inplace=True)
    X = df.drop("COMP", axis=1)
    y = df["COMP"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    data_df = pd.DataFrame(data, columns=X.columns)
    pred = model.predict(data_df)
    return math.trunc(pred[0])

def bus(data):
    df = csv.copy()
    df.drop(["KISW", "BIO", "PHY", "CHE", "HIST", "GEO", "COMP", "ENG", "MATH", "RE"], axis=1, inplace=True)
    X = df.drop("BUS", axis=1)
    y = df["BUS"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    data_df = pd.DataFrame(data, columns=X.columns)
    pred = model.predict(data_df)
    return math.trunc(pred[0])

def re(data):
    df = csv.copy()
    df.drop(["KISW", "BIO", "PHY", "CHE", "HIST", "GEO", "COMP", "BUS", "MATH", "ENG"], axis=1, inplace=True)
    X = df.drop("RE", axis=1)
    y = df["RE"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    data_df = pd.DataFrame(data, columns=X.columns)
    pred = model.predict(data_df)
    return math.trunc(pred[0])

def getPreds(MATHEMATICS, ENGLISH, KISWAHILI, BIOLOGY, PHYSICS, CHEMISTRY, HISTORY, GEOGRAPHY, COMPUTER, BUSINESS, CRE):
    total = ENGLISH + KISWAHILI + BIOLOGY + PHYSICS + CHEMISTRY + HISTORY + GEOGRAPHY + COMPUTER + BUSINESS + CRE
    feature_vector = [[MATHEMATICS, ENGLISH, KISWAHILI, BIOLOGY, PHYSICS, CHEMISTRY, HISTORY, GEOGRAPHY, COMPUTER, BUSINESS, CRE, total, 28]]  # example extended input
    
    print(f"here are the expected hours of study, math {mathe()}, \
eng {eng(feature_vector)}, kisw {kisw(feature_vector)}, bio {bio(feature_vector)}, phy {phy(feature_vector)}, \
chem {che(feature_vector)}, history {hist(feature_vector)}, geo {geo(feature_vector)}, comp {comp(feature_vector)}, \
business {bus(feature_vector)} and CRE {re(feature_vector)}, and the total was {total}")

getPreds(5, 54, 55, 54, 34, 45, 7, 8, 9, 5, 8)
