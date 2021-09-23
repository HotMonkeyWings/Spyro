<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/HotMonkeyWings/Spyro/">
    <img src="discord.jpg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Attendance Bot</h3>

  <p align="center">
    A discord bot for taking attendance with a single command.
    <br />
    <a href="https://github.com/HotMonkeyWings/Spyro/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://discord.com/api/oauth2/authorize?client_id=814474425662701588&permissions=2182417472&scope=bot">Invite the Bot</a>
    ·
    <a href="https://github.com/HotMonkeyWings/Spyro/issues">Report Bug</a>
    ·
    <a href="https://github.com/HotMonkeyWings/Spyro/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About the Project
This was made for the intentions of recording attendance in discord servers.

### Built With

* [Discord API](https://discordpy.readthedocs.io/en/latest/)

<!-- GETTING STARTED -->
## Getting Started

To deployyour own version of the bot, follow the steps below.

### Prerequisites

* Python 
  ```sh
  sudo pacman -S python
  ```

* Python Discord API library
  ```sh
  pip3 install discord
  ```
* Python Time Zone library
  ```sh
  pip3 install pytz
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/HotMonkeyWings/Spyro.git
   ```
   
2. Make a .env file in the following format
  ```sh
  API=<API-KEY>
  ```

3. Run the bot (Optional for those who want to host it with their own bot)
   ```sh
   python3 bot.py
   ```
  OR to run it as a 24/7 bot on your own server
     ```sh
    sudo nohup python3 bot.py >& log.txt &
    ```


<!-- USAGE EXAMPLES -->
## Usage

   ```sh
   -attend <Channel Name>:<Role Name>
   ```


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Dev Sony - [@hotmonkeywings](https://www.instagram.com/hotmonkeywings/) - devsony52@gmail.com

Project Link: [Spyro-The Attendance Bot](https://github.com/HotMonkeyWings/Spyro/)


