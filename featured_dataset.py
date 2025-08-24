import pandas as pd
from  sklearn.preprocessing import LabelEncoder

df=pd.read_csv("cleaned_matches.csv")
output_file='featured_matches.csv'

if df is not None:
    categorical_cols = ['team1', 'team2', 'toss_winner', 'winner', 'city', 'toss_decision']
    encoder=LabelEncoder()
    for i in categorical_cols:
        df[i+'_encoded']=encoder.fit_transform(df[i])
        mapping=dict(zip(encoder.classes_,encoder.transform(encoder.classes_)))
        print(mapping)
preview_cols = ['team1', 'team1_encoded', 'team2', 'team2_encoded', 'winner', 'winner_encoded']
print(df[preview_cols].head())
df.to_csv(output_file, index=False)