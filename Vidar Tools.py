from pystyle import Anime, Colors, Colorate, System, Center, Write
import time
from discord_webhook import DiscordWebhook

ascii_art = r"""
 __      __  _____   _____               _____      _______    ____     ____    _         _____ 
 \ \    / / |_   _| |  __ \      /\     |  __ \    |__   __|  / __ \   / __ \  | |       / ____|
  \ \  / /    | |   | |  | |    /  \    | |__) |      | |    | |  | | | |  | | | |      | (___  
   \ \/ /     | |   | |  | |   / /\ \   |  _  /       | |    | |  | | | |  | | | |       \___ \ 
    \  /     _| |_  | |__| |  / ____ \  | | \ \       | |    | |__| | | |__| | | |____   ____) |
     \/     |_____| |_____/  /_/    \_\ |_|  \_\      |_|     \____/   \____/  |______| |_____/ 
                                                                                                
                                                                                                
"""[1:]

def systeme():
  Anime.Fade(text=Center.Center(ascii_art), color=Colors.red_to_yellow, mode=Colorate.Vertical, enter=True)
  webhook_spammer()



def init():
    System.Clear()
    System.Size(160, 50)
    System.Title("Vidar Tools v.1.1 By Anthoxdu13")

    systeme()

def webhook_spammer():
    System.Title("Vidar Tools WebHook Spammer")
    print(Colorate.Horizontal(color=Colors.red_to_yellow, text=Center.XCenter(ascii_art)))
    url = input(Colorate.Horizontal(Colors.yellow_to_red, "\n WebHook Url -> "))
    Msg = input(Colorate.Horizontal(Colors.yellow_to_red, "\n Votre Message -> "))
    print(Colorate.Horizontal(Colors.yellow_to_red, "\n/!\ Le Message Va Être Spam Tant Que Le Tools Est Ouvert !"))
    print(Colorate.Horizontal(Colors.yellow_to_red, "\n/!\ Je Décline Toute Responsabilité Pour Ce Que Vous En Faites."))
    a = input(Colorate.Horizontal(Colors.yellow_to_red, "\nVoulez-Vous Continuer (O/N) -> "))
    if a =="O":
      while True:
        webhook = DiscordWebhook(url=url, content=Msg+" (with Vidar Tools for Discord)")
        response = webhook.execute()
        time.sleep(1)
        print(Colorate.Horizontal(Colors.yellow_to_red, "Le message est partie"))
    else:
      systeme()

init()
