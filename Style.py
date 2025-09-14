# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Developed by : Mohammed Al-Baqer
# Version : 1.1.0
# Copyright (c) 2024 - 2025 Mohammed Al-Baqer

import os
import time
import sys
from datetime import datetime
from prettytable import PrettyTable
from AscallArtCLI.BackGround import(Red, Green, Blue, Black, Yellow, Cyan, Orange, Pink, Magenta, White, Reset)
from AscallArtCLI.Colors import(R, G, B, Y, D, C, P, O, W, M, S)
from AscallArtCLI.Tags import(
    START,
    END,
    sign,
    Enter,
    ERROR,
    INFO,
    Information,
    Working,
    NotWorking,
    warning,
    Complete,
    successfully,
    Failed,
    please,
    Question,
    Help,
    other,
    notice,
    note,
    Running,
    Ready,
    DONE,
    Loading,
    OK,
    Okay,
    stop,
    Critical,
    paused,
    Retrying,
    Skip,
    SCAN,
    Chacking,
    Hacking,
    security,
    AI,
    Press,
    Confirm
)

def DateTime():
    try:
        now = datetime.now()
        FormatedTime = now.strftime("%I:%M:%S %p")
        FormatedDay = now.strftime("%A")
        DateDay = (
            B + "[" + G + "Today" + B + "]" +
            W + "(" + Y + FormatedDay +
            M + f" {now:%B %d %Y}" +
            W + ") " + B + "[" +
            G + "Time" + B + "]" +
            Y + "[" + R + FormatedTime +
            Y + "]" + W
        )
        return DateDay
    except Exception as e:
        return str(e)
DateTime = DateTime()

os.system('cls' if os.name == 'nt' else 'clear')

"""if os.geteuid() != 0:
    sudo = "\033[1;31m" + "sudo" + "\033[97;1m"
    root = "\033[93;1m" + "root" + "\033[97;1m"
    print(f"{please} {W}please use {root} Type a command {sudo}")
    sys.exit()"""

table = PrettyTable()

# wallpapers
KaliLinux_2019_4 = "kali-wallpapers-2019.4"
KaliLinux_2020_4 = "kali-wallpapers-2020.4"
KaliLinux_2021_4 = "kali-wallpapers-2021.4"
KaliLinux_2022 = "kali-wallpapers-2022"
KaliLinux_2023 = "kali-wallpapers-2023"
KaliLinux_Mobile_2023 = "kali-wallpapers-mobile-2023"
KaliLinux_2024 = "kali-wallpapers-2024"
KaliLinux_2025 = "kali-wallpapers-2025"
KaliLinux_all = "kali-wallpapers-all"
KaliLinux_legacy = "kali-wallpapers-legacy"
KaliLinux_legacy_wallpapers = "kali-legacy-wallpapers"
KaliLinux_community = "kali-wallpapers-community"
KaliLinux_everything = "kali-linux-everything"

# Desktop Environments
sddm = "sddm"
lightdm = "lightdm"
gdm3 = "gdm3"
gnome = "kali-desktop-gnome"
kde = "kali-desktop-kde"
xfce = "kali-desktop-xfce"
lxde = "kali-desktop-lxde"
i3 = "kali-desktop-i3"

print(f"""{B}
            ..,;:ccc,.                             
          ......''';lxO.                           
.....''''..........,:ld;                           
           .';;;:::;,,.x,                          
      ..'''.            0Xxoc:,.  ...              
  ....                ,ONkc;,;cokOdc',.            
 .                   OMo           ':ddo.          
                    dMc               :OO;          
                    0M.                 .:o.       
                    ;Wd                            
                     {B};XO,                         {R}_____ _                            {Y}__ _         _        
                       {B},d0Odlc;,..               {R}/__   \ |__   ___ _ __ ___   ___   {Y}/ _\ |_ _   _| | ___     
                           {B}..',;:cdOOd::,.         {R}/ /\/ '_ \ / _ \ '_ ` _ \ / _ \  {Y}\ \| __| | | | |/ _ \ 
                                    {B}.:d;.':;.     {R}/ /  | | | |  __/ | | | | |  __/  {Y}_\ \ |_| |_| | |  __/ 
                                       {B}'d,  .'    {R}\/   |_| |_|\___|_| |_| |_|\___|  {Y}\__/\__|\__, |_|\___|   
                                         {B};l   ..                                            {Y}|___/         
                                          {B}.o       {G} _  _  _   |  o    |    o               
                                            {B}c       {G}|-<_ |_|_ |_ |    |___ | |\| |_| ><
                                            {B}.'    
                                             {B}.      {Y}By {W}: {B}Mohammed Al-Baqer
                                                    {Y}INSTAGRAM {W}: {B}wsl.iq{W}""")
                                                    

def choose_environment():
    try:
        table = PrettyTable()
        table.field_names = [f"{B}ID{W}", f"{G}Options{W}"]
        table.add_row([f"{C}1{W}", f"{P}Switch between Kali Linux environments{W}"])
        table.add_row([f"{C}2{W}", f"{P}Install environments{W}"])
        table.add_row([f"{C}3{W}", f"{P}Install single wallpaper{W}"])
        table.add_row([f"{C}4{W}", f"{P}Install all wallpapers{W}"])
        table.add_row([f"{C}5{W}", f"{P}Uninstall environments{W}"])
        print(table)
        def ASCLLART(prompt: str) -> str:
            return input(f"\033[91;1m┌─[\033[95;1mMohammed Al-Baqer\033[93;1m@\033[94;1mWSL.IQ\033[91;1m]─[\033[92;1m{prompt}\033[91;1m]\n└──╼\033[91;1m❯\033[93;1m❯\033[92;1m❯\033[97;1m ")
        
        choice = ASCLLART("please Enter choice number")

        if choice == '1':
            table = PrettyTable()
            table.field_names = [f"{B}ID", f"{G}Options"]
            table.add_row([f"{C}1{W}", f"{P}gdm3{W}"])
            table.add_row([f"{C}2{W}", f"{P}lightdm{W}"])
            table.add_row([f"{C}3{W}", f"{P}sddm{W}"])
            print(table)

            ChoiceDESKTOP = ASCLLART("please Enter choice number")
            
            if ChoiceDESKTOP in ['1', '2', '3']:
                DESKTOP = ['gdm3', 'lightdm', 'sddm'][int(ChoiceDESKTOP) - 1]
                os.system(f"sudo dpkg-reconfigure {DESKTOP}")
            else:
                print(f"{please} Incorrect selection please try again{W}")

        elif choice == '2':
            table = PrettyTable()
            table.field_names = [f"{B}ID{W}", f"{G}Options{W}"]
            table.add_row([f"{C}1{W}", f"{P}lightdm{W}"])
            table.add_row([f"{C}2{W}", f"{P}gdm3{W}"])
            table.add_row([f"{C}3{W}", f"{P}kali-desktop-gnome{W}"])
            table.add_row([f"{C}4{W}", f"{P}kali-desktop-kde{W}"])
            table.add_row([f"{C}5{W}", f"{P}kali-desktop-xfce{W}"])
            table.add_row([f"{C}6{W}", f"{P}kali-desktop-lxde{W}"])
            table.add_row([f"{C}7{W}", f"{P}kali-desktop-i3{W}"])
            print(table)

            ChoiceINTRFACE = ASCLLART("please Enter choice number")

            if ChoiceINTRFACE in ['1', '2', '3', '4', '5', '6', '7']:
                INTERFACE = ['lightdm', 'gdm3', 'kali-desktop-gnome', 'kali-desktop-kde', 'kali-desktop-xfce', 'kali-desktop-lxde', 'kali-desktop-i3'][int(ChoiceINTRFACE) - 1]
                os.system(f"sudo apt install {INTERFACE}")
            else:
                print(f"{ERROR} Incorrect selection please try again{W}")

        elif choice == '3':
            input(f"{warning} {W}The download size is {G}[{B}50GB{G}]{W} and takes {G}[{B}30 minutes{G}]{W} If you agree click {B}[{G}Enter{B}]{W} or you want to stop and exit click {B}[{Y}Ctrl {W}+{Y} C{B}]{W}\n\r")
            print(DateTime)
            table = PrettyTable()
            table.field_names = [f"{B}ID{W}", f"{G}Options{W}"]
            table.add_row([f"{C}1{W}", f"{P}kali-wallpapers-2019.4{W}"])
            table.add_row([f"{C}2{W}", f"{P}kali-wallpapers-2020.4{W}"])
            table.add_row([f"{C}3{W}", f"{P}kali-wallpapers-2021.4{W}"])
            table.add_row([f"{C}4{W}", f"{P}kali-wallpapers-2022{W}"])
            table.add_row([f"{C}5{W}", f"{P}kali-wallpapers-2023{W}"])
            table.add_row([f"{C}6{W}", f"{P}kali-wallpapers-mobile-2023{W}"])
            table.add_row([f"{C}7{W}", f"{P}kali-wallpapers-2024{W}"])
            table.add_row([f"{C}8{W}", f"{P}kali-wallpapers-2025{W}"])
            table.add_row([f"{C}9{W}", f"{P}kali-wallpapers-legacy{W}"])
            table.add_row([f"{C}10{W}", f"{P}kali-legacy-wallpapers{W}"])
            table.add_row([f"{C}11{W}", f"{P}kali-wallpapers-community{W}"])
            print(table)
            ChoiceWALLPAPER = ASCLLART("please Enter choice number")
            if ChoiceWALLPAPER in [str(i) for i in range(1, 12)]:
                WALLPAPER = [
                    "kali-wallpapers-2019.4",
                    "kali-wallpapers-2020.4",
                    "kali-wallpapers-2021.4",
                    "kali-wallpapers-2022",
                    "kali-wallpapers-2023",
                    "kali-wallpapers-mobile-2023",
                    "kali-wallpapers-2024",
                    "kali-wallpapers-2025",
                    "kali-wallpapers-legacy",
                    "kali-legacy-wallpapers",
                    "kali-wallpapers-community"
                ][int(ChoiceWALLPAPER) - 1]
                os.system(f"sudo apt install {WALLPAPER}")
            else:
                print(f"{please} Incorrect selection please try again{W}")
                ChoiceWALLPAPER = ASCLLART("please Enter choice number")
        elif choice == '4':
            ALL = input(f"{Question} The download size is {G}[{B}50GB{G}]{W} and takes {G}[{B}30 minutes{G}]")
            Choice = print(Confirm)
            if ALL == "C":
                os.system("sudo apt install kali-wallpapers-all")
                os.system("sudo apt install kali-linux-everything")
                os.system("sudo apt install kali-legacy-wallpapers")
                os.system("sudo apt install kali-wallpapers-legacy")
                os.system("sudo apt install kali-wallpapers-community")
                os.system("sudo apt install kali-wallpapers-2019.4")
                os.system("sudo apt install kali-wallpapers-2020.4")
                os.system("sudo apt install kali-wallpapers-2021.4")
                os.system("sudo apt install kali-wallpapers-2022")
                os.system("sudo apt install kali-wallpapers-2023")
                os.system("sudo apt install kali-wallpapers-mobile-2023")
                os.system("sudo apt install kali-wallpapers-2024")
                os.system("sudo apt install kali-wallpapers-2025")
                os.system(f"sudo apt install {sddm}")
                os.system(f"sudo apt install {lightdm}")
                os.system(f"sudo apt install {gdm3}")
                os.system(f"sudo apt install {gnome}")
                os.system(f"sudo apt install {kde}")
                os.system(f"sudo apt install {xfce}")
                os.system(f"sudo apt install {lxde}")
                os.system(f"sudo apt install {i3}")
                print(f"{INFO} Go to Path {B}[{Y}/usr/share/backgrounds/{B}]{W} to find wallpapers")
            elif ALL == "e":
                print(f"{stop} Exiting...{W}")
                sys.exit(0)
            else:
                print(f"{please} Incorrect selection please try again{W}")

        elif choice == '5':
            table = PrettyTable()
            table.field_names = [f"{B}ID{W}", f"{G}Options{W}"]
            table.add_row([f"{C}1{W}", f"{P}Uninstall gdm3{W}"])
            table.add_row([f"{C}2{W}", f"{P}Uninstall lightdm{W}"])
            table.add_row([f"{C}3{W}", f"{P}Uninstall sddm{W}"])
            table.add_row([f"{C}4{W}", f"{P}Uninstall kali-desktop-gnome{W}"])
            table.add_row([f"{C}5{W}", f"{P}Uninstall kali-desktop-kde{W}"])
            table.add_row([f"{C}6{W}", f"{P}Uninstall kali-desktop-xfce{W}"])
            table.add_row([f"{C}7{W}", f"{P}Uninstall kali-desktop-lxde{W}"])
            table.add_row([f"{C}8{W}", f"{P}Uninstall kali-desktop-i3{W}"])
            table.add_row([f"{C}9{W}", f"{P}Uninstall all environments{W}"])
            print(table)
            ChoiceUNINSTALL = ASCLLART("please Enter choice number")
            if ChoiceUNINSTALL in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                UNINSTALL = ['gdm3', 'lightdm', 'sddm', 'kali-desktop-gnome', 'kali-desktop-kde', 'kali-desktop-xfce', 'kali-desktop-lxde', 'kali-desktop-i3', 'all'][int(ChoiceUNINSTALL) - 1]
                os.system(f"sudo apt remove {UNINSTALL}")
            else:
                print(f"{please} Incorrect selection please try again{W}")

            print(DateTime)
            time.sleep(5)
            os.system("clear")
            input(f"{Enter} Do you want to restart? If you agree click {B}[{G}Enter{B}]{W} or you want to stop and exit click {B}[{Y}Ctrl {W}+{Y} C{B}]{W}\n\r")

            os.system("sudo reboot")
        else:
            print(f"{please} Incorrect selection please try again{W}")
    except KeyboardInterrupt:
        print(f'{sign} Exiting...{W}')
        sys.exit()

if __name__ == "__main__":
    choose_environment()
