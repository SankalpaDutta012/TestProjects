import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('mail_data.csv')
print(df)

# Handle missing values
data = df.where(pd.notnull(df), '')

# Display basic information about the dataset
data.head()
data.info()
data.shape

# Encode the Category column
data.loc[data['Category'] == 'spam', 'Category'] = 0
data.loc[data['Category'] == 'ham', 'Category'] = 1

# Split the dataset into features and labels
X = data['Message']
y = data['Category']
print(X)
print(y)

# Split the dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(X.shape)
print(X_train.shape)
print(X_test.shape)
print(y.shape)
print(Y_train.shape)
print(Y_test.shape)

# Feature extraction
feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
X_train_feature = feature_extraction.fit_transform(X_train)
X_test_feature = feature_extraction.transform(X_test)

# Convert the labels to integers
Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

print(X_train)
print(X_train_feature)

# Create and train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train_feature, Y_train)

# Make predictions on the training set
train_predictions = model.predict(X_train_feature)
train_accuracy = accuracy_score(Y_train, train_predictions)
print(f'Training Accuracy: {train_accuracy}')

# Make predictions on the test set
test_predictions = model.predict(X_test_feature)
test_accuracy = accuracy_score(Y_test, test_predictions)
print(f'Test Accuracy: {test_accuracy}')


# Input data
input_your_mail = [
    """
    Dear Sir/Madam,

    Greetings from the SIH team!

    We are excited to announce the Smart India Hackathon (SIH) 2024 Social Media Contest, offering a fantastic opportunity to showcase your journey, engage with a national audience, and win exciting rewards!

    What to Post?
    Share your activities, experiences, preparations, and learnings through:
    - Photos
    - Videos/Reels/Shorts
    - Creative posters, banners, and infographics

    Where to Post?
    On Platform X (Twitter), Facebook, Instagram, and LinkedIn.

    Who to Tag?
    @narendramodi, @PMOIndia, @EduMinOfIndia, @dpradhanbjp, @PIBHRD, @SITHARAMtg, @abhayjere, @MS_AICTE, @SIH2024_MIC.
    Acknowledge and tag our partners:
    - Official Partner: Godrej Appliances
    - Evaluation Partner: TCS
    - Media Partner: Doordarshan & Akashvani
    - Learning Partner: Tutorial Point
    - Platform Partner: Hack2Skills

    Hashtags to Use:
    - #SmartIndiaHackathon
    - #SIH2024
    - #PM_ModiAtSIH
    - #InnovationSeAtmanirbharBharat
    - #JaiAnusandhan

    Prizes and Awards:
    Weekly Prizes:
    - Week 1 (27th Nov - 3rd Dec): 20 prizes of INR 5,000 + 5 special prizes for PM interaction posts.
    - Week 2 (4th Dec - 10th Dec): 20 prizes of INR 5,000 + 5 special prizes for PM interaction posts.
    - Week 3 (11th Dec - 17th Dec): 20 prizes of INR 10,000 + 5 special prizes for PM interaction posts.
    Consistent Participants:
    - 15 special prizes of INR 10,000 for those posting exceptional content consistently across platforms.

    How to Participate?
    - Follow Ministry of Education's Innovation Cell on all platforms.
    - Post your content using the provided tags and hashtags.
    - Submit the direct link to your post via this Google Form.

    Winner Selection Criteria:
    Winners will be selected based on the reach of their posts (likes, reactions, retweets, and comments) and the number of posts made following the contest guidelines.

    For more details, refer to the attached PDF containing the complete guidelines.

    Let’s create a buzz and make SIH 2024 a grand success!

    PFA: [Guidelines PDF](https://drive.google.com/file/d/15ayRmJh35rwfLCyb3MzfZDRYFQV8fjd5/view?usp=sharing)

    Regards,
    Smart India Hackathon Team
    Contact Us: +91 112958-1239/1240/1235
    For more details visit www.sih.gov.in 
    Follow us on Instagram: SIH, Twitter: SIH
    For details on other initiatives of AICTE visit: https://www.aicte-india.org/Initiatives
    For details on other initiatives of MIC visit: https://mic.gov.in/mic/
    """
]
# input_your_mail = ["We’re celebrating Christmas this year by giving you some major upgrades to your SEO.AI account. Watch the video here:Here are the new features you can try out today:1) Analytics: Monitor specific groups of pagesTry the new Analytics dashboard, which provides a super simple overview of your site’s clicks, impressions, and rankings on Google.It’s like Google Search Console, but with the option to set filters based on URL slugs (e.g. /category/), making it easy to track different sections of your site.You can also view performance grouped by weeks and months. 2) Pages: Spot low-hanging fruit The new “Pages” feature makes it easy to identify opportunities for improving your pages’ rankings.For example, filter by pages where your primary keyword currently ranks between positions 10 and 20 on Google, and see which pages (the low-hanging fruit) you should optimize to move them higher up. 3) Easier access to the editor and AI draftsPreviously, you had to set a target keyword before opening the editor. Now you can open a blank editor with a single click. Once inside, you can set a target keyword, import content from an existing URL, and run an AI Draft. 4) Simplified navigationWe’ve updated the entire menu structure: Open editor (previously 'Create new') Analytics (new feature) Pages (new feature) Documents (previously 'Created content') Keyword Research (previously 'Keywords') Settings (contains Configuration, Brand voice, Templates, Connections, etc.) If you’re looking for the 'Rank tracking' feature, we’re currently developing an improved version. Until it’s ready, the current version can be found under 'Analytics' in the top-right corner. Try your new SEO.AI now. We have extra support available today If you’re having trouble navigating, have questions, or need assistance, feel free to reply to this email. We have additional support staff available today, so we can give you the extra help you need. Merry Christmas Best regards, Torbjørn--Torbjørn Flensted Co-founder SEO.AI - The Easiest Way to Generate Ranking SEO Copy"]
input_data_feature = feature_extraction.transform(input_your_mail)
predictions = model.predict(input_data_feature)

print(f'Prediction for input email: {predictions}')

if (predictions[0] == 1):
    print("Ham Mail")
else:
    print("Spam Mail")
