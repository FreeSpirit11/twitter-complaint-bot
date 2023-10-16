# Twitter Complaint Bot

The Twitter Complaint Bot automates the process of checking your internet speed and tweeting your service provider when your actual speed falls below the promised level. It helps you hold your provider accountable for the quality of service you're receiving.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Acknowledgement](#acknowledgement)
- [Author](#author)

## Prerequisites

To use this bot, you need to have the following:

- Python 3.x installed on your system.
- The Selenium library and a Chrome WebDriver installed. You can install Selenium using `pip install selenium` and download the WebDriver from the [official website](https://sites.google.com/a/chromium.org/chromedriver/downloads).
- A Twitter account for posting complaints.
- Your Twitter email and password (set as environment variables for security).

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/FreeSpirit11/twitter-complaint-bot.git
    ```

2. Navigate to the project folder:

    ```bash
    cd twitter-complaint-bot
    ```

3. Install the required Python libraries (Selenium):

    ```bash
    pip install selenium
    ```

4. Download the Chrome WebDriver and add its path to the system environment variables.

5. Set your Twitter email and password as environment variables. Replace `YOUR_EMAIL` and `YOUR_PASSWORD` with your actual credentials:

    ```bash
    export TWITTER_EMAIL=YOUR_EMAIL
    export TWITTER_PASSWORD=YOUR_PASSWORD
    ```

## Usage

1. Run the script:

    ```bash
    python main.py
    ```

2. The bot will perform a speed test and tweet your internet provider if your actual speed falls below the promised speed.

## How It Works

The Twitter Complaint Bot uses Selenium to automate the following tasks:

1. Conducts a speed test on [Speedtest.net](https://www.speedtest.net/).
2. Retrieves the download and upload speeds.
3. Logs into your Twitter account.
4. Composes a tweet to your service provider, mentioning the actual and promised speeds.
5. Posts the tweet.

Please note that using this bot may violate the terms of service of the websites it interacts with. Use it responsibly and in accordance with the laws and regulations of your country.


## Acknowledgement

This project is a part of the "100 Days of Code" challenge by Angela Yu.

## Author
- [Mansi Yadav](https://github.com/FreeSpirit11/twitter-complaint-bot)
