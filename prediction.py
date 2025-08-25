import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv("featured_matches.csv")
features=["team1_encoded","team2_encoded","toss_winner_encoded","city_encoded","toss_decision_encoded",]
labels="winner_encoded"

encoder=LabelEncoder()
df['winner_encoded']=encoder.fit_transform(df['winner'])

X=df[features]
y=df[labels]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train,y_train)

test_predictions = model.predict(X_test)
train_predictions = model.predict(X_train)

test_accuracy = accuracy_score(y_test, test_predictions)
train_accuracy = accuracy_score(y_train, train_predictions)

print("train :",train_accuracy*100)
print("test: ",test_accuracy*100)

team_wins={}
for i in y:
    if i in team_wins:
        team_wins[i]+=1
    else:
        team_wins[i]=1
tot_match=len(y)
team_win_percent={}
for team_encoded,win in team_wins.items():
    team_win_percent[team_encoded]=(win/tot_match)*100

team_percent_name={}
for team_enco,perc in team_win_percent.items():
    team_name=encoder.inverse_transform([team_enco])[0]
    team_percent_name[team_name]=perc
for team,perc in team_percent_name.items():
    print(f"{team} : {perc:.2f}%")
