# Evaluating NBA Box Statistics for Their Relevance to a Game's Outcome
While in the past I may have elected to predict a game's outcome using merely the final or 3rd-quarter score, over the course of this project I decided to investigate the correlation between these statistics. 
## Data Used
Refer to [this repository](https://github.com/Nathanlauga/nba-predictor) to access the data used for this project. 
## Working of the Code
As shown in main.py, the overall flow involves itself with the loading of the data as a pandas DataFrame, and the further plotting of the Pearson correlation matrix using matplotlib and seaborn. The following is the correlation matrix as plotted: 

## Evaluation 
The test data is scored 0.7 approximately using .score(). Prediction of other seasons using the same model yielded scores of around 0.65-0.73. One could use more 
than one season to fit the data, which could yield higher scores. However, one should beware of overfitting the data.
