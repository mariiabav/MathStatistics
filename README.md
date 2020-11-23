# Telegram bot
## Purpose
Telegram bot sends memes and GIFs.
Application is used for visualization of server data.
## Requirements
- python 3.8.x or higher ([get at python.org](https://www.python.org/downloads/))
- additional packages (see in `requirements.txt`) 
## Installation
- Download these files from GitLab or clone this repository via https:
    ```
    git clone https://gitlab.com/mariiabav/telegram-bot.git
    cd telegram-bot
    git clone https://gitlab.com/mariiabav/r_shiny-django.git
    cd r_shiny-django
    ```
- Install dependencies for command line application:
   ```
   pip3 install requirements.txt
   ```
- Install [R](https://cran.r-project.org/) version 3.4.0 or later
- Install [Rstudio](https://www.rstudio.com/products/rstudio/download/) version 1.1.453 or later
## Usage
- Run program from the root folder of repository: `python src/main.py`
- Before starting the application, enter the command:
  ```r
  install.packages("shiny")
  ```
  In Rstudio you can open and start app through the `File -> Open File -> '.../app.R'` menu at the top of the screen.
  Once all packages are installed, select `Run App` from the `Addins` menu in Rstudio or use the command below to launch the app:
- You will see input-UI for your function to find root on suggested interval. Please enter your function and algorithm-parameters and press "OK". You will see visualization of newton algorithm for your input function step by step. 
 
## Explanation
UI-interface visualizes Newton's algorithm's work. You can choose colors for vizualisation and accuracy. First point is calculated as middle of right and left border. If you input wrong parameters, you will see message about it. For cleaning all values press "Reset".

You can run all unittests provided using `unittest.discover`:
```
python -m unittest discover
```

## Example
First of all, UI-menu:  

<img src="https://sun9-53.userapi.com/ug-N8BnuUMiB15O99iQEqzBNL0_f7uyitl5tKw/we8720H_XP8.jpg"  width="639" height="592">

Enter your function:

<img src="https://sun9-66.userapi.com/4wfDfQd302GFEZrGqNc-WwWA095QUhPNWVo8Iw/RA_pUpuoGrc.jpg"  width="639" height="592">

And press "OK" (you'll see function graph first):

<img src="https://sun9-8.userapi.com/Ur3moc4fswUQNqprJYt06R23FD9PYYlAr7-TFw/Ryguyiz3w9U.jpg"  width="639" height="592">

Next you will see step by step algorithm.  

_Step 1:_

<img src="https://sun9-35.userapi.com/ce7DlrhR-e8AkN9olXxMvlp7pmykWudwPIr9sQ/lXapU2hcP_Y.jpg"  width="639" height="592">

_Step 2:_

<img src="https://sun9-26.userapi.com/UWkzM2zK_TAZ7z0XXhf8kbtyoD6oWvBQjlcofg/fw-LgpnconM.jpg"  width="639" height="592">

