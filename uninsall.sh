#!/bin/bash

# Define colors for output
R="\033[91;1m"
G="\033[92;1m"
B="\033[94;1m"
Y="\033[93;1m"
W="\033[97;1m"
Complete="${B}[${G}COMPLETE${B}]${G}"
ERROR="${Y}[${R}ERROR${Y}]${R}"
Enter="${B}[${G}+${B}]${G}"
sign="${G}[${B}*${G}]${B}"

# Ensure script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo -e "${R}Please run this script as root (sudo)."
    exit 1
fi

# Clear the terminal
clear

# List of desktop environments to uninstall
default_environment="lightdm" # The default environment you want to keep
environments_to_remove=(
    "gdm3"
    "kali-desktop-gnome"
    "kali-desktop-kde"
    "kali-desktop-xfce"
    "kali-desktop-lxde"
    "kali-desktop-i3"
)

# Main menu
echo -e "${sign} Environment Manager"
echo -e """
1. Revert to default environment (lightdm)
2. Exit
"""

read -p "${Enter} Enter your choice: " choice

case $choice in
    1)
        # Confirm user wants to proceed
        read -p "${R}Are you sure you want to revert to the default environment (lightdm)? (yes/no): " confirm
        if [[ "$confirm" != "yes" ]]; then
            echo -e "${R}Operation canceled."
            exit 0
        fi

        echo -e "${Complete} Reverting to default environment..."

        # Uninstall all environments except the default
        for env in "${environments_to_remove[@]}"; do
            if [[ "$env" != "$default_environment" ]]; then
                echo -e "${G}Removing $env...${W}"
                apt-get remove --purge "$env" -y
            fi
        done

        # Reconfigure the default environment
        echo -e "${G}Reconfiguring $default_environment as the default...${W}"
        dpkg-reconfigure "$default_environment"

        # Fix missing dependencies and update the system
        echo -e "${G}Fixing dependencies and updating system...${W}"
        dpkg --configure -a
        apt-get -f install -y
        apt-get update -y
        apt-get upgrade -y

        echo -e "${Complete} System restored to default environment (lightdm)."
        ;;
    2)
        echo -e "${R}Exiting script."
        exit 0
        ;;
    *)
        echo -e "${ERROR} Invalid choice."
        ;;
esac
