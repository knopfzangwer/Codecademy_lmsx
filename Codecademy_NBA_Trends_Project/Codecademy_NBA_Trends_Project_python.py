#!/usr/bin/env python
# coding: utf-8

# # Codecademy [NBA Trends Project](https://www.codecademy.com/projects/practice/nba-trends)
# 
# *Analyze National Basketball Association (NBA) data to look at associations between teams, win-rates, playoff appearances, and more.*

# In this project, you'll analyze data from the NBA (National Basketball Association) and explore possible associations. 
# 
# This data was originally sourced from 538's Analysis of the [Complete History Of The NBA](http://fivethirtyeight.com/interactives/the-complete-history-of-every-nba-team-by-elo) and contains the original, unmodified data from [Basketball Reference](http://www.basketball-reference.com/) as well as several additional variables 538 added to perform their own analysis. 
# 
# You can read more about the data and how it's being used by 538 [here](https://github.com/fivethirtyeight/data/tree/master/nba-elo). For this project we've limited the data to just 5 teams and 10 columns (plus one constructed column, `point_diff`, the difference between `pts` and `opp_pts`).
# 
# You will create several charts and tables in this project, so you'll need to use `plt.clf()` between plots in your code so that the plots don't layer on top of one another.
# 

# In[25]:


import pandas as pd
import numpy as np
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns


# In[26]:


#to make the output look nicer
np.set_printoptions(suppress=True, precision = 2)


# In[27]:


nba = pd.read_csv('nba_games.csv')
nba.head()


# In[28]:


# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]


# ### Task 1
# The data has been subset for you into two smaller datasets: games from 2010 (named nba_2010) and games from 2014 (named nba_2014). To start, let’s focus on the 2010 data.
# 
# Suppose you want to compare the knicks to the nets with respect to points earned per game. Using the pts column from the nba_2010 DataFrame, create two series named knicks_pts (fran_id = "Knicks") and nets_pts(fran_id = "Nets") that represent the points each team has scored in their games.
# 

# In[29]:


knicks_pts_10 = nba_2010[nba_2010.fran_id == "Knicks"]
nets_pts_10 = nba_2010[nba_2010.fran_id == "Nets"]

print("A média de pontos dos Knicks na temporada de 2010 foi de {:.1f} pontos".format(knicks_pts_10.pts.mean()))
print("A média de pontos dos Nets na temporada de 2010 foi de {:.1f} pontos\n".format(nets_pts_10.pts.mean()))

print("A maior pontuação dos Knicks na temporada de 2010 foi de {} pontos".format(knicks_pts_10.pts.max()))
print("A maior pontuação dos Nets na temporada de 2010 foi de {} pontos\n".format(nets_pts_10.pts.max()))

print(knicks_pts_10.describe())
print("\n")
print(nets_pts_10.describe())
display(knicks_pts_10)


# ### Task 2
# 
# Calculate the difference between the two teams’ average points scored and save the result as diff_means_2010. Based on this value, do you think fran_id and pts are associated? Why or why not?
# 

# In[30]:


diff_means_2010 = knicks_pts_10.pts.mean() - nets_pts_10.pts.mean()
print(diff_means_2010)


# ### Task 3
# Rather than comparing means, it’s useful look at the full distribution of values to understand whether a difference in means is meaningful. Create a set of overlapping histograms that can be used to compare the points scored for the Knicks compared to the Nets. Use the series you created in the previous step (1) and the code below to create the plot. Do the distributions appear to be the same?
# 

# In[31]:


plt.hist(knicks_pts_10.pts , color="blue", label="Knicks Points in 2010", density=True, alpha=0.5)
plt.hist(nets_pts_10.pts , color="red", label="Nets Points in 2010", density=True, alpha=0.5)
plt.legend()
plt.show()


# ### Task 4
# Now, let’s compare the 2010 games to 2014. Replicate the steps from Tasks 2 and 3 using `nba_2014`. First, calculate the mean difference between the two teams points scored. Save and print the value as `diff_means_2014`. Did the difference in points get larger or smaller in 2014? Then, plot the overlapping histograms. Does the mean difference you calculated make sense?
# 

# In[34]:


knicks_pts_14 = nba_2014[nba_2014.fran_id == "Knicks"]
nets_pts_14 = nba_2014[nba_2014.fran_id == "Nets"]

print(knicks_pts_14.describe())
print("\n")
print(nets_pts_14.describe())

plt.hist(knicks_pts_14.pts, color="blue", label="Knicks Points in 2014", density=True, alpha=0.5)
plt.hist(nets_pts_14.pts, color="red", label="Nets Points in 2014", density=True, alpha=0.5)
plt.legend()
plt.show()


# ### Task 5
# For the remainder of this project, we’ll focus on data from 2010. Let’s now include all teams in the dataset and investigate the relationship between franchise and points scored per game.
# 
# Using nba_2010, generate side-by-side boxplots with points scored (pts) on the y-axis and team (fran_id) on the x-axis. Is there any overlap between the boxes? Does this chart suggest that fran_id and pts are associated? Which pairs of teams, if any, earn different average scores per game?
# 

# In[37]:


nba_2010 = nba[nba.year_id == 2010]
display(nba_2010)
sns.boxplot(data = nba_2010, x = "fran_id", y = "pts")
plt.show()


# ### Task 6
# We'd like to know if teams tend to win more games at home compared to away.
# 
# The variable, `game_result`, indicates whether a team won a particular game ('W' stands for “win” and 'L' stands for “loss”). The variable, `game_location`, indicates whether a team was playing at home or away ('H' stands for “home” and 'A' stands for “away”). 
# 
# Data scientists will often calculate a contingency table of frequencies to help them determine if categorical variables are associated. Calculate a table of frequencies that shows the counts of game_result and game_location.
# 
# Save your result as `location_result_freq` and print your result. Based on this table, do you think the variables are associated?`
# 

# In[38]:


location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
print(location_result_freq)


# ### Task 7
# 
# Convert this table of frequencies to a table of proportions and save the result as `location_result_proportions`.

# In[39]:


location_result_proportions = location_result_freq/len(nba_2010)
print(location_result_proportions)


# ### Task 8
# Using the contingency table created above (Task 6), calculate the expected contingency table (if there were no association) and the Chi-Square statistic.
# 
# Does the actual contingency table look similar to the expected table — or different? Based on this output, do you think there is an association between these variables?
# 

# In[40]:


chi2, pval, dof, expected = chi2_contingency(location_result_freq)
print(expected)
print(chi2)


# *For a 2x2 table, Chi-squared greater than about 4 indicates an association. We're not there*

# ### Task 9
# 
# For each game, 538 has calculated the probability that each team will win the game. We want to know if teams with a higher probability of winning (according to 538) also tend to win games by more points. 
# 
# In the data, 538's prediction is saved as `forecast`. The `point_diff` column gives the margin of victory/defeat for each team (positive values mean that the team won; negative values mean that they lost). 
# 
# Using `nba_2010`, calculate the covariance between `forecast` (538's projected win probability) and `point_diff` (the margin of victory/defeat) in the dataset. Save and print your result. Looking at the matrix, what is the covariance between these two variables?
# 

# In[41]:


cov_forecast_point_diff = np.cov(nba_2010.forecast, nba_2010.point_diff)
print(cov_forecast_point_diff)


# ### Task 10
# 
# Because 538’s forecast variable is reported as a probability (not a binary), we can calculate the strength of the correlation.
# 
# Using nba_2010, calculate the correlation between `forecast` and `point_diff`. Call this `point_diff_forecast_corr`. Save and print your result. Does this value suggest an association between the two variables?
# 

# In[44]:


point_diff_forecast_corr = pearsonr(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_corr)


# ### Task 11
# 
# Generate a scatter plot of `forecast` (on the x-axis) and `point_diff` (on the y-axis). Does the correlation value make sense?

# In[46]:


plt.scatter(nba_2010.forecast, nba_2010.point_diff)
plt.xlabel('Forecasted Win Prob.')
plt.ylabel('Point Differential')
plt.show()


# In[32]:




