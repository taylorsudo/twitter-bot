# Twitter Bot

A Twitter bot that posts a random quote from a text file during peak hours, using Python and GitHub Actions.

## Setup

1. Create a Twitter/X account for your bot. 
2. Go to **Settings and privacy** > **Account information** > **Automation**, and follow the instructions.
3. Go to https://developer.twitter.com/ and fill out the form to access the Twitter API.
4. In the **Developer Portal**, find your project app under **Default project** and click **App settings**.
5. In the **User authentication settings** area, click on **Set up**. Set **App permissions** to **Write and Read**, **Type of App** to **Web App** and for **App info** insert your bot’s Twitter profile as the callback URL and website link.
6. Copy your project's **API Key**, **API Key Secret**, **Access Token**, and **Access Token Secret**, and store them somewhere safe.
7. Clone this repository, click on **Settings**, and on the sidebar go to **Secrets and variables** > **Actions**.
8. Add four repository secrets and paste their respective values: 
  - `CONSUMER KEY`: Your API Key 
  - `CONSUMER SECRET`: Your API Key Secret 
  - `ACCESS TOKEN`: Your Access Token 
  - `ACCESS SECRET`: Your Access Token Secret 
9. In your GitHub repository, create a `.github/workflows` directory.
10. Inside your workflows directory, create a file called `action.yml` with the following:

```yaml
name: Schedule Tweet

on:
  schedule:
    - cron: '0 14,2 * * *' # Runs at 9:00 AM and 9:00 PM EST
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Check Out Repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: 3.12

      - name: Install Dependencies
        run: pip install -r requirements.txt

      - name: Run Python Script
        env:
            ACCESS_TOKEN: ${{ secrets.ACCESS_TOKEN }}
            ACCESS_TOKEN_SECRET: ${{ secrets.ACCESS_TOKEN_SECRET }}
            CONSUMER_TOKEN: ${{ secrets.CONSUMER_TOKEN }}
            CONSUMER_SECRET: ${{ secrets.CONSUMER_SECRET }}
        run: python main.py
```

Finally, test your bot by going to **Actions** > **Schedule Tweet** > **Run workflow**.
