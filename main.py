import tweepy
import time
import os

# credentials to login to twitter api
api_key = ''
api_key_secret = ''
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
bearer_token=''
client_id=''
client_secret=''

client = tweepy.Client(bearer_token=bearer_token)

# Replace with your own search query
#replace place_country with the code of your country of interest or remove.
query = 'COVID19 place_country:GB'

# Starting time period YYYY-MM-DDTHH:MM:SSZ (max period back is March 2006)
start_time = '2018-01-01T00:00:00Z'

# Ending time period YYYY-MM-DDTHH:MM:SSZ
end_time = '2018-08-03T00:00:00Z'

#I'm getting the geo location of the tweet as well as the location of the user and setting the number of tweets returned to 10 (minimum) - Max is 100

tweets = client.search_all_tweets(query=query, tweet_fields=['context_annotations', 'created_at', 'geo'], place_fields=['place_type', 'geo'], user_fields=['location'], expansions='author_id,geo.place_id', start_time=start_time, end_time=end_time, max_results=10)




login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

# # os.chdir('models')

# # # iterates over pictures in models folder
# # for model_image in os.listdir('.'):
# #     api.update_with_media(model_image)
# #     time.sleep(3)

# # import tweepy


# # # client = tweepy.Client(bearer_token)
# client = tweepy.Client(
#     consumer_key=client_id, consumer_secret=client_secret,
#     # access_token=access_token, access_token_secret=access_token_secret
# )

# # # Get User's Followers

# # # This endpoint/method returns a list of users who are followers of the
# # # specified user ID

# user_id = 2244994945

# # # By default, only the ID, name, and username fields of each user will be
# # # returned
# # # Additional fields can be retrieved using the user_fields parameter
response = client.get_users_followers(
    user_id, user_fields=["profile_image_url"]
)

# # for user in response.data:
# #     print(user.username, user.profile_image_url)

# # # By default, this endpoint/method returns 100 results
# # # You can retrieve up to 1000 users by specifying max_results
# # # response = client.get_users_followers(user_id, max_results=1000)


# # client = tweepy.Client(bearer_token)
# # client = tweepy.Client(
# #     consumer_key=client_id, consumer_secret=client_secret,
# #     # access_token=access_token, access_token_secret=access_token_secret
# # )
# query = "Tweepy -is:retweet"

# # Granularity is what you want the timeseries count data to be grouped by
# # You can request minute, hour, or day granularity
# # The default granularity, if not specified is hour
# # response = client.get_recent_tweets_count(query, granularity="day")

# for count in response.data:
#     print(count)