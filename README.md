# Evaluating NBA Box Statistics for Their Relevance to a Game's Outcome
While in the past I may have elected to predict a game's outcome using merely the final or 3rd-quarter score, over the course of this project I decided to investigate the correlation between these statistics. 
## Data Used
Refer to [this repository](https://github.com/Nathanlauga/nba-predictor) to access the data used for this project. 
## Working of the Code
As shown in main.py, the overall flow involves itself with the loading of the data as a pandas DataFrame, and the further plotting of the Pearson correlation matrix using matplotlib and seaborn. The following is the correlation matrix as plotted: 
![relevant_stats_corr_matrix](https://user-images.githubusercontent.com/77375209/112657999-fa361480-8e78-11eb-8915-7e0d80ceaff6.png)
## Evaluation 
Among the stats which are highly correlated, is of field-goal percentage and total points (for both home and away, as would be intuitive). Their correlation stands at 0.67. Secondly, we have assists and total points - which have a corr. matrix of 0.59 and 0.57 for home and away respectively. Consequently, assists and field-goal percentage have a correlation of 0.55 and 0.52 for home and away. 
