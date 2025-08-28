import praw
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import nltk

# Download VADER lexicon if not already
nltk.download('vader_lexicon')

# Initialize VADER
vader_analyzer = SentimentIntensityAnalyzer()

# Initialize PRAW
reddit = praw.Reddit(
    client_id="w0Q-WF5NgnMASZwEiK7hZw",
    client_secret="fCWMy_1VoV6VMhsCCDaQL9SILZI2_Q",
    user_agent="sentiment-analysis-script by u/SquareCheetah8787"
)

subreddit_name = "MachineLearning"  # change to your subreddit
subreddit = reddit.subreddit(subreddit_name)

# Store posts
posts = []

for submission in subreddit.new(limit=None):  # fetch up to API limit (~1000 posts)
    title = submission.title
    selftext = submission.selftext

    # Combine title and body for analysis
    content = title + " " + selftext

    # VADER sentiment
    vader_scores = vader_analyzer.polarity_scores(content)
    vader_compound = vader_scores['compound']

    # TextBlob sentiment
    blob = TextBlob(content)
    textblob_polarity = blob.polarity
    textblob_subjectivity = blob.subjectivity

    posts.append({
        "title": title,
        "selftext": selftext,
        "score": submission.score,
        "num_comments": submission.num_comments,
        "created": submission.created_utc,
        "author": str(submission.author),
        "vader_compound": vader_compound,
        "vader_positive": vader_scores['pos'],
        "vader_negative": vader_scores['neg'],
        "vader_neutral": vader_scores['neu'],
        "textblob_polarity": textblob_polarity,
        "textblob_subjectivity": textblob_subjectivity
    })

# Convert to DataFrame
df = pd.DataFrame(posts)
df.to_csv(f"{subreddit_name}_sentiment.csv", index=False)

print(f"Scraped and analyzed {len(posts)} posts from r/{subreddit_name}")

