import pandas as pd
from surprise import Reader

book_ratings = pd.read_csv('goodreads_ratings.csv')

#1. Print dataset size and examine column data types
# print(len(book_ratings))
print(book_ratings.head())
print(book_ratings.info())
#2. Distribution of ratings
print(book_ratings.rating.value_counts())
#3. Filter ratings that are out of range
book_ratings = book_ratings[book_ratings.rating != 0]
print(book_ratings.rating.value_counts())
#4. Prepare data for surprise: build a Suprise reader object
from surprise import Reader
reader = Reader(rating_scale=(1, 5))
#5. Load `book_ratings` into a Surprise Dataset
from surprise import Dataset
rec_data = Dataset.load_from_df(book_ratings[['user_id',
                                              'book_id',
                                              'rating']],
                                reader)
#6. Create a 80:20 train-test split and set the random state to 7
from surprise.model_selection import train_test_split
training_set, validation_set = train_test_split(rec_data, random_state=7, test_size=0.2)
#7. Use KNNBasice from Surprise to train a collaborative filter
from surprise import KNNBasic
recommender = KNNBasic()
recommender.fit(training_set)

#8. Evaluate the recommender system
from surprise import accuracy
predictions = recommender.test(validation_set)
accur = accuracy.rmse(predictions)
print(accur)
#9. Prediction on a user who gave the "The Three-Body Problem" a rating of 5
print(recommender.predict('8842281e1d1347389f2ab93d60773d4d', '18007564'))
print(recommender.predict('8842281e1d1347389f2ab93d60773d4d', '18007564').est)
