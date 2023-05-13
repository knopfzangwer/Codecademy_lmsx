from helper_functions import choose_statistic, population_distribution, sampling_distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import codecademylib3

# task 1: load in the spotify dataset
spotify_data = pd.read_csv("spotify_data.csv")
# task 2: preview the dataset
print(spotify_data.head())
# task 3: select the relevant column
song_tempos = spotify_data.tempo
# task 5: plot the population distribution with the mean labeled
population_distribution(song_tempos)
# task 6: sampling distribution of the sample mean
sampling_distribution(song_tempos, 30, "Mean")
# task 8: sampling distribution of the sample minimum
sampling_distribution(song_tempos, 30, "Minimum")
# task 10: sampling distribution of the sample variance
sampling_distribution(song_tempos, 30, "Variance")
# task 13: calculate the population mean and standard deviation
population_mean = choose_statistic(song_tempos, "Mean")
population_std = choose_statistic(song_tempos, "Standard Deviation")
print(population_mean, population_std)
# task 14: calculate the standard error
standard_error = (population_std)/(np.sqrt(30))
print(standard_error)
# task 15: calculate the probability of observing an average tempo of 140bpm or lower from a sample of 30 songs
less_140 = stats.norm.cdf(140, population_mean, standard_error)
print(less_140)
# task 16: calculate the probability of observing an average tempo of 150bpm or higher from a sample of 30 songs
more_than_150 = 1 - stats.norm.cdf(150, population_mean, standard_error)
print(more_than_150)
# EXTRA
def choose_statistic(x, sample_stat_text):
  # calculate mean if the text is "Mean"
  if sample_stat_text == "Mean":
    return np.mean(x)
  # calculate minimum if the text is "Minimum"
  elif sample_stat_text == "Minimum":
    return np.min(x)
  # calculate variance if the text is "Variance"
  elif sample_stat_text == "Variance":
    return np.var(x, ddof=1)
  # calcula o desvio padrão
  elif sample_stat_text == "Standard Deviation":
    return np.std(x)
  # calcula o mínimo ou máximo
  elif sample_stat_text == "Min":
    return np.min(x)
  elif sample_stat_text == "Max":
    return np.max(x)
  # raise error if sample_stat_text is not "Mean", "Minimum", or "Variance"
  else:
    raise Exception('Make sure to input "Mean", "Minimum", or "Variance"')
