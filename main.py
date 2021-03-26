import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load data
game_data = pd.read_csv('games.csv')
game_data = game_data.drop(['GAME_DATE_EST', 'GAME_ID', 'GAME_STATUS_TEXT', 'HOME_TEAM_ID','VISITOR_TEAM_ID', 'SEASON',
                   'TEAM_ID_home', 'TEAM_ID_away'], axis=1)

#Using Pearson Correlation
plt.figure(figsize=(12,10))
cor = game_data.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.show()

