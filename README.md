# Cyber News - A simple web crawler
The News Bot for Discord is a valuable addition to any server seeking to provide curated news content, fostering an informed and engaged community.

<details>
  <summary>read more</summary>

  <p>
    The News Bot for Discord is a reliable and responsible bot that brings the latest news updates directly to your Discord server. It utilizes a web crawler mechanism to collect information from RSS feeds of various websites at user-defined intervals. The bot captures essential details such as news headlines, image links, and additional information, and seamlessly publishes them to a designated announcements channel using a configured webhook.
  </p>
  <p>
    With its automated functionality, the bot ensures that your community stays informed about the latest news and developments. The announcements channel acts as a centralized hub for sharing news, allowing users to engage in discussions and stay up-to-date with relevant information. The bot's design promotes trust and reliability by consistently delivering timely and accurate news updates.
  </p>
</details>


## technologies
 - [discord.py](https://github.com/Rapptz/discord.py)
 - [requests](https://github.com/psf/requests)
 - [xmltodict](https://github.com/martinblech/xmltodict)


## installation

1. clone the repository:

  ```bash
  git clone https://github.com/luan-gsm/cybernews
  cd cybernews
  ```


2. set up a virtual environment (optional but recommended):

  ```bash
  python -m venv venv
  source venv/bin/activate
  ```


3. install the requirements:

  ```bash
  pip install -r requirements.txt
  ```


4. configure the environment:

  ```bash
  cp .env.example .env
  ```

modify the contents of .env as specified.


## usage 

1. change to the `src` directory:

  ```bash
  cd ./src
  ```


2. run the program

  ```bash
  python ./main.py
  ```

The bot will start fetching news updates and publishing them to the designated announcements channel on your Discord server.
