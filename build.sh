#!/bin/bash

echo -e "  ___           _     ___        "  
echo -e " | _ \__ _ _ __(_)___|   \ _____ __"
echo -e " |   / _  | '_ \ |___| |) / -_) V /"
echo -e " |_|_\__,_| .__/_|   |___/\___|\_/" 
echo -e "          |_|           "           

# -------------------------------------------------------

VERSION="v0.3"
GITHUB="https://github.com/Rapi-Dev/RapiMake"

echo -e "----------------------"
echo -e "|Project: RapiMake"
echo -e "|Version: $VERSION"
echo -e "|Github: $GITHUB"
echo -e "----------------------"

echo -e "1) Build a bot"
echo -e "2) Exit"

# -------------------------------------------------------

build_a_bot() {
    sleep 2
    clear
    echo -e "1) Build basic bot"
    echo -e "2) Insert modules into the bot"
    echo -e "3) Exit"
    read -r TYPE
      case $TYPE in
          1 )
             build_basic_bot ;;
          2 )
             modules_list ;;
          3 )
             exit ;;

                     * )
    esac
}

build_basic_bot() {
    echo "Please enter the directory you want me to for the bot files to be stored in! (e.g /Bots/Test-Bot)"
    read -r DIRECTORY
    mkdir $DIRECTORY

    cd $DIRECTORY
    curl -Lo  main.py https://raw.githubusercontent.com/Rapi-Dev/RapiMake/main/assets/main.py?token=ARSKP2KRLUZY4DSW7AKTN7LAS4I6Y

    pip3 install discord
    pip3 install python-dotenv

    echo "Successfully installed the basic bot files"
    sleep 1
    clear

    mkdir Cogs
    echo -e "Enter the prefix you want for your bot. (e.g !)"
    read -r PREFIX

    echo -e "Enter the token of your bot. (e.g You can generate one at: https://discord.dev)"
    read -r TOKEN

    echo -e "TOKEN=$TOKEN\nPREFIX=$PREFIX" >> .env


    echo -e "The bot has successfuly been configured!"

}

modules_list() {
    sleep 2
    clear

    echo "1 | Install Fun Module"
    echo "1 | Install Images Module"
    echo "3 | Exit"

    read -r TYPE
      case $TYPE in
          1 )
             install_fun ;;
          2) 
              install_imgs ;;
          3 )
             exit ;;

                     * )
    esac
}

# -------------------------------------------------------

install_fun() {

  echo -e "Please enter the directory of the bot that you had set earlier on while creating the basic setup!"

  read DIR
  cd $DIR
  cd Cogs

  pip3 install nekos.py
  pip3 install requests

  curl -Lo fun.py https://raw.githubusercontent.com/Rapi-Dev/RapiMake/main/assets/fun.py

  echo -e "Installed the Fun Module successfuly!"
}

install_imgs() {

  echo -e "Please enter the directory of the bot that you had set earlier on while creating the basic setup!"

  read DIR
  cd $DIR
  cd Cogs

  pip3 install nekos.py
  pip3 install Tamako.py

  curl -Lo fun.py https://raw.githubusercontent.com/Rapi-Dev/RapiMake/main/assets/fun.py

  echo -e "Installed the Images Module successfuly!"
    
}

# -------------------------------------------------------

read -r TYPE
  case $TYPE in
      1 )
         build_a_bot ;;
      2 )
         exit ;;

                * )
esac

# -------------------------------------------------------
