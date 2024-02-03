import os
import random
import tweepy

# Retrieve Twitter API credentials from environment variables
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

# Function to read tweets from a file
def read_tweets(file_path):
    with open(file_path, "r") as file:
        tweets = [line.strip() for line in file.readlines() if line.strip()]
    return tweets

# Path to the file containing tweets
tweets_file_path = "tweets.txt"

def post_random_tweet():
    if not (consumer_key and consumer_secret and access_token and access_token_secret):
        print("Please set the environment variables for API credentials.")
        return

    # Authenticate with the Twitter API
    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    # Read tweets from the file
    tweets = read_tweets(tweets_file_path)

    if not tweets:
        print("No tweets found in the file.")
        return

    # Choose a random tweet
    random_tweet = random.choice(tweets)

    try:
        # Post the random tweet to Twitter
        client.create_tweet(text=random_tweet)
        print("Tweeted: ", random_tweet)
    except AttributeError as e:
        print("Error: ", e)

if __name__ == "__main__":
    post_random_tweet()
