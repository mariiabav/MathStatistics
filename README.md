# Telegram bot
## Purpose
Application is used for visualization of server data.
## Requirements
- [python 3.8.x](https://www.python.org/downloads/) or higher 
- additional packages (see in `requirements.txt`) 
- [R](https://cran.r-project.org/) version 4.0.3 or later
- [Rstudio](https://www.rstudio.com/products/rstudio/download/) version 1.3.1093 or later
## Installation
- Download these files from GitLab or clone this repository via https:
    ```
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
 
## App interface

<img src="https://sun9-37.userapi.com/impf/m2EXaxLh8HBpnbOI9hjoI9BlWYmqgu1EEvtfMQ/WRROcqTzqG4.jpg?size=898x454&quality=96&proxy=1&sign=fe35bba6dc2eeec44d89bcf3e9d76fe0"  width="650" height="592">

<img src="https://sun9-3.userapi.com/impf/OHyKJI5Yl5bAaPHTEEs5SUoxsrvQvCfWu_CaLA/5Z_WJfNZslU.jpg?size=896x449&quality=96&proxy=1&sign=7c1284c959998d117b50a69d0ddaad34"  width="700" height="592">

<img src="https://sun9-14.userapi.com/impf/guM1-MeZh3OcpYYNCgS1GMOr3qP9PN-JBcZOzQ/CKmEQLbfRq0.jpg?size=899x452&quality=96&proxy=1&sign=3973d0de9087301c8f183b32fa50bdd1"  width="750" height="592">



