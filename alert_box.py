import pymsgbox
from playsound import playsound
import os


def display_message_mac(body_Str, title_Str):
	playsound(os.path.join(os.getcwd(), "Sounds", "air_horn_sound.mp3"))
	answer = pymsgbox.confirm(title=title_Str, text=body_Str, buttons=["OK", "EXIT"])
	return answer
