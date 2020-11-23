# Telegram bot
## Purpose
Telegram bot sends memes and GIFs.
Application is used for visualization of server data.
## Requirements
- [python 3.8.x](https://www.python.org/downloads/) or higher 
- additional packages (see in `requirements.txt`) 
- [R](https://cran.r-project.org/) version 4.0.3 or later
- [Rstudio](https://www.rstudio.com/products/rstudio/download/) version 1.3.1093 or later
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
- Install shiny package in Rstudio
  ```
  install.packages("shiny")
  ```

## Usage
- Run server from the root folder of repository. Use the commands:
   ```
   git checkout develop
   cd src
   python3 manage.py runserver
   ```
- Start app through the `File -> Open File -> '.../ui.R'` in Rstudio. Select `Run App` from the Rstudio menu.
 
## Explanation
UI-interface visualizes Newton's algorithm's work. You can choose colors for vizualisation and accuracy. First point is calculated as middle of right and left border. If you input wrong parameters, you will see message about it. For cleaning all values press "Reset".

You can run all unittests provided using `unittest.discover`:
```
python -m unittest discover
```

## App interface
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

