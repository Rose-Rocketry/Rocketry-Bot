# Rocketry-Bot
 A discord bot for administrative and notification purposes.

# Features
Features can be disabled individually
## Member Database
Creates and manages names and automatically assigns the aspiring member role once they have submitted their name and rose-hulman email address.

### Attendance Taking

Based on the Google Calendar (updated hourly) provided, it will create a message in channel to react to.
This will automatically mark down the hours worked log for an hour (default) or special by an admin.

This also manages the `Active` or `Aspiring` member status. If the member has not submitted attendance for a quarter they will be demoted to `Aspiring` member. This rule does not apply to admin.

## Launch Day Alerts
When a launch day is coming up or arrived, a generated report for drive time, weather, and other information will be sent in announcements. 

## USLI Project Alerts
Reminds us of upcoming due dates for USLI reports.

## Special Rocketry Commands
 - Motor class conversion. `;rocketry classconvert [newton-seconds]`
 - Fire cabinent explosive power. `;rocketry cabinent`
 
# Under the Hood
There are two main programs this bot needs to work correctly.
1. The database/web host
2. The bot system itself.

## Database and Webhost
This is what stores the member database and how we can more granularly manage the bot without having to resort to commands (useful for debugging). The front end does not matter much.

### Technologies expected to use:
* Django
* Redis
* PostgreSQL
* Docker

## Discord Bot System

### Technologies expected to use:
* Discord.py
* Asnycio

# Repository Management
This repository is built using Docker and Remote-Containers. This way the environment can be shipped to whatever computer we decide to host the project on.
## What Do I Need?
First you need to install Docker/Docker Desktop. Visit [Docker](https://www.docker.com/products/docker-desktop/) and follow the links to install.
Second, I would make sure that you have an up-to-date Visual Studio Code with the following extensions:
 - Remote Development (Pack)
 - Docker
 - Python (Pack)
Third to make source control easier, I use [GitHub Desktop](https://desktop.github.com/).

# FAQ
Questions I think I might be asked a lot, for now.
## How do I switch between working on the web service and the bot?
In .devcontainer, there is a devcontainer.json. In one of the fields, there is a field called `service`, which you can set to either `bot` and `app`.
## Why are there so many containers?
Having the bot separated from the platform that controls it, we can have more reliability. 
