import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

#loading the dataset
csv = pd.read_csv("Hours.csv")

#clean our data 
csv.dropna()

#setup the features target for each model
def math():
    return 7

def eng():
    csv.drop(["KISW", "BIO", "PHY", "CHE", "HIST", "GEO", "COMP", "BUS", "RE", inplace=True)
    X = csv.drop("ENG", axis=1)
    y = csv.ENG
    
    #SPLIT THE DATA HERE
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #make our model
    model = LinearRegression()

    #Train our model here
    model.fit(X_train, y_train)

    #test our model now
    pred = model.predict(X_test)

    print(f"mean squared error for eng is {mean_squared_error(y_test, pred)} and r2 score is {r2_score(y_test, pred)}")
def kisw():
    csv.drop(["ENG", "BIO", "PHY", "CHE", "HIST", "GEO", "COMP", "BUS", "RE", inplace=True)
    X = csv.drop("KISW", axis=1)
    y = csv.KISW
    
    #SPLIT THE DATA HERE
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #make our model
    model = LinearRegression()

    #Train our model here
    model.fit(X_train, y_train)

    #test our model now
    pred = model.predict(X_test)

    print(f"mean squared error for kisw is {mean_squared_error(y_test, pred)} and r2 score is {r2_score(y_test, pred)}")    

def bio():
    csv.drop(["KISW", "ENG", "PHY", "CHE", "HIST", "GEO", "COMP", "BUS", "RE" inplace=True)
    X = csv.drop("BIO", axis=1)
    y = csv.BIO
    
    #SPLIT THE DATA HERE
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #make our model
    model = LinearRegression()

    #Train our model here
    model.fit(X_train, y_train)

    #test our model now
    pred = model.predict(X_test)

    print(f"mean squared error for bio is {mean_squared_error(y_test, pred)} and r2 score is {r2_score(y_test, pred)}")    

def phy():
    csv.drop(["KISW", "BIO", "ENG", "CHE", "HIST", "GEO", "COMP", "BUS", "RE", inplace=True)
    X = csv.drop("PHY", axis=1)
    y = csv.PHY
    
    #SPLIT THE DATA HERE
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #make our model
    model = LinearRegression()

    #Train our model here
    model.fit(X_train, y_train)

    #test our model now
    pred = model.predict(X_test)

    print(f"mean squared error for phy is {mean_squared_error(y_test, pred)} and r2 score is {r2_score(y_test, pred)}")    

def che():
    csv.drop(["KISW", "BIO", "PHY", "ENG", "HIST", "GEO", "COMP", "BUS", "RE", inplace=True)
    X = csv.drop("CHE", axis=1)
    y = csv.CHE
    
    #SPLIT THE DATA HERE
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #make our model
    model = LinearRegression()

    #Train our model here
    model.fit(X_train, y_train)

    #test our model now
    pred = model.predict(X_test)

    print(f"mean squared error for CHEM is {mean_squared_error(y_test, pred)} and r2 score is {r2_score(y_test, pred)}")    

def hist():
    csv.drop(["KISW", "BIO", "PHY", "CHE", "ENG", "GEO", "COMP", "BUS", "RE", inplace=True)
    X = csv.drop("HIST", axis=1)
    y = csv.HIST
    
    #SPLIT THE DATA HERE
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #make our model
    model = LinearRegression()

    #Train our model here
    model.fit(X_train, y_train)

    #test our model now
    pred = model.predict(X_test)

    print(f"mean squared error for HIST is {mean_squared_error(y_test, pred)} and r2 score is {r2_score(y_test, pred)}")    

def geo():
    csv.drop(["KISW", "BIO", "PHY", "CHE", "HIST", "ENG", "COMP", "BUS", "RE" inplace=True)
    X = csv.drop("GEO", axis=1)
    y = csv.GEO
    
    #SPLIT THE DATA HERE
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #make our model
    model = LinearRegression()

    #Train our model here
    model.fit(X_train, y_train)

    #test our model now
    pred = model.predict(X_test)

    print(f"mean squared error for geo is {mean_squared_error(y_test, pred)} and r2 score is {r2_score(y_test, pred)}")    

def comp():
    csv.drop(["KISW", "BIO", "PHY", "CHE", "HIST", "GEO", "ENG", "BUS", "RE" inplace=True)
    X = csv.drop("COMP", axis=1)
    y = csv.COMP
    
    #SPLIT THE DATA HERE
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #make our model
    model = LinearRegression()

    #Train our model here
    model.fit(X_train, y_train)

    #test our model now
    pred = model.predict(X_test)

    print(f"mean squared error for eng is {mean_squared_error(y_test, pred)} and r2 score is {r2_score(y_test, pred)}")    

def bus():
    csv.drop(["KISW", "BIO", "PHY", "CHE", "HIST", "GEO", "COMP", "ENG", "RE", inplace=True)
    X = csv.drop("BUS", axis=1)
    y = csv.BUS
    
    #SPLIT THE DATA HERE
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #make our model
    model = LinearRegression()

    #Train our model here
    model.fit(X_train, y_train)

    #test our model now
    pred = model.predict(X_test)

    print(f"mean squared error for eng is {mean_squared_error(y_test, pred)} and r2 score is {r2_score(y_test, pred)}")    

def re():
    csv.drop(["KISW", "BIO", "PHY", "CHE", "HIST", "GEO", "COMP", "BUS", "ENG", inplace=True)
    X = csv.drop("RE", axis=1)
    y = csv.RE
    
    #SPLIT THE DATA HERE
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #make our model
    model = LinearRegression()

    #Train our model here
    model.fit(X_train, y_train)

    #test our model now
    pred = model.predict(X_test)

    print(f"mean squared error for eng is {mean_squared_error(y_test, pred)} and r2 score is {r2_score(y_test, pred)}")    

def getPreds(MATH, ENG, KISW, BIO, PHY, CHE, HIST, GEO, COMP, BUS, RE):
    param 
    math()
    eng()
    kisw()
    bio()
    phy()
    che()
    hist()
    geo()
    comp()
    bus()
    re()
