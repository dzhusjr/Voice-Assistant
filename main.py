print("\nImporting packages...\n")
try:
    from speech_recognition import Microphone
    from speech_recognition import Recognizer
    from quantulum3 import parser
    from pint import UnitRegistry
    from datetime import datetime
    from pafy import new
    # from vlc import MediaPlayer as MP
    from pywhatkit import search as srch
    from pywhatkit import info
    from tkinter import *
    from PIL import Image, ImageTk
    from ctypes import windll
    import re, urllib.parse, urllib.request, python_weather, asyncio, os, pyjokes, winshell, win32gui, json, random, pyttsx3, pyautogui, speedtest
    import time as t
except Exception as ex:
    print(ex)
    exit()

from commands import commands_dict

print("Starting...")
# GUI
root = Tk()
photo = ImageTk.PhotoImage(Image.open("1.png").resize((40, 40)))
photo1 = ImageTk.PhotoImage(Image.open("2.png").resize((40, 40)))
root.geometry("40x40+5-5")
root.overrideredirect(1)
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "black")


# Text-Speech
engine = pyttsx3.init()
engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
engine.setProperty("rate", 180)

# Speech-Text
r = Recognizer()
r.pause_threshold = 0.5
r.energy_threshold = 1000
is_playing = listen = False


def is_active():
    global listen, is_playing
    if is_playing:
        media.set_pause(1)
        is_playing = False
    listen = True
    button.configure(image=photo1)


# display button
button = Button(root, image=photo, borderwidth=0, bg="black", activebackground="black", command=is_active)
button.pack()
# -----------
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
data_path = "data.json"
media = None
user32 = windll.user32
ureg = UnitRegistry()

# Setup
with open(data_path) as f:
    data = json.load(f)
assname, uname = data["assname"], data["uname"]

# Adjusting the microphone
with Microphone() as mic:
    print("Adjusting the microphone...\n")
    r.adjust_for_ambient_noise(source=mic, duration=3)

print("Ready!")

# system  functions
def update_data(new_data):
    global data
    with open(data_path) as f:
        data = json.load(f)
    with open(data_path) as f:
        json.dump(new_data, f)


def is_full_screen():
    try:
        return win32gui.GetWindowRect(user32.GetForegroundWindow()) == (0, 0, user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
    except:
        return False


def talk(text):
    engine.say(text)
    print(text)
    engine.runAndWait()


def listen_command(printing=True):
    if printing:
        print("Listening...")
    with Microphone() as mic:
        audio = r.listen(source=mic, timeout=1, phrase_time_limit=5)
    try:
        if printing:
            print("Recognizing...")
        query = r.recognize_google(audio_data=audio, language="en-EN").lower()
        print(f"You: {query}")
    except:
        query = listen_command(printing)
    return query


def respond():
    global assname, listen
    query = listen_command()
    button.configure(image=photo)
    root.update()
    # query = input('You:')
    words = query.split(" ")
    for k, v in commands_dict.items():
        if any(phrase in query for phrase in v):
            exec(k)
            break
    else:
        talk("I didn't get that!")
    listen = False


# main functions
def create_task(query):
    if query:
        task = query
    else:
        talk("What to write?")
        print("Listening...")
        button.configure(image=photo1)
        root.update()
        task = listen_command(False)
        button.configure(image=photo)
        root.update()
    with open("todo-list.txt", "a", encoding="utf-8") as file:
        file.write(f"❗️ {task}\n")
    talk(f"Task {task} added to todo-list!")


def clear_todo_list():
    f = open("todo-list.txt", "w")
    f.close()
    talk("Your to-do list is cleared")


# def play(words):
#     global listen, is_playing, media
#     try:
#         song = " ".join(words[words.index("play") + 1 :])
#     except:
#         talk("Play what?")
#         print("Listening...")
#         song = listen_command(False)
#     video = new(
#         "https://www.youtube.com/watch?v="
#         + "{}".format(
#             re.findall(
#                 r"watch\?v=(\S{11})",
#                 urllib.request.urlopen("https://www.youtube.com/results?" + urllib.parse.urlencode({"search_query": song})).read().decode(),
#             )[0]
#         )
#     )
#     value = video.allstreams[4].filename.replace(".mp4", "")
#     talk(f"Playing {value}")
#     media = MP(video.getbestaudio().url)
#     media.play()
#     is_playing, listen = True, False


def search(words):
    try:
        query = " ".join(words[words.index("search") + 1 :])
    except:
        query = " ".join(words[words.index("google") + 1 :])
    talk("Searching")
    srch(query)


def information(query):
    talk(info(query, lines=1, return_value=1))


def unit_convert(query):
    for r in ("hectares", "ha"):
        query.replace(*r)
    from_, to_ = query.split(" to ")
    if len(from_.split(" ")) == 1:
        from_ = "1 " + from_
    qfrom = parser.parse(from_)
    qfrom_pint = ureg.Quantity(qfrom[0].value, str(qfrom[0].unit))()

    qto = parser.parse("1 " + to_)
    qto_str = str(qto[0].unit)
    try:
        result = qfrom_pint.to(qto_str)
        if result.is_integer():
            result = int(result)
        talk(from_, "is", result)
    except:
        talk("I don't know how to convert that!")


def speed_test():
    talk("Testing your internet speed...")
    speed = speedtest.Speedtest()
    talk(f"Download speed is {round(speed.download()/1000000)} Mbps and Upload speed is {round(speed.upload()/1000000)} Mbps")


def open_opera():
    talk("Here is Opera")
    os.startfile("C:\\Users\\User\\AppData\\Local\\Programs\\Opera GX\\launcher.exe")


def open_discord():
    talk("Here is discord")
    os.startfile("C:\\Users\\User\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk")


def open_vscode():
    talk("Here is VS Code. Good coding!")
    os.startfile("C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")


async def getweather(region):
    client = python_weather.Client(format=python_weather.METRIC)
    try:
        weather = await client.find(region)
    except:
        talk("Invalid region")
        getweather()
    for forecast in weather.forecasts:
        if str(forecast.date) == f'{datetime.today().strftime("%Y-%m-%d")} 00:00:00':
            talk(f"The weather in {region} is {forecast.sky_text}. It's {forecast.temperature} degrees celsius.")
    await client.close()


def change_uname(new_uname):
    data["uname"] = new_uname
    update_data(data)
    talk(f"Ok, {data['uname'].capitalize()}")


def change_assname(words):
    try:
        new_assname = words[words.index("to") + 1]
    except:
        talk("What would you like to call me?")
        button.configure(image=photo1)
        root.update()
        new_assname = listen_command(False)
        button.configure(image=photo1)
        root.update()
    data["assname"] = new_assname
    update_data(data)
    talk("Thanks for naming me")


def shutdown():
    talk("Are you sure you want to shutdown your computer?")
    print("Listening...")
    button.configure(image=photo1)
    root.update()
    if listen_command(False) == "yes":
        talk("Hold On a Sec ! Your system is on its way to shut down")
        os.system("shutdown /s /t 1")
    else:
        talk("Ok i won't do that")
    button.configure(image=photo)
    root.update()


def restart():
    talk("Are you sure you want to restart your computer?")
    print("Listening...")
    button.configure(image=photo1)
    root.update()
    if listen_command(False) == "yes":
        talk("Restarting system...")
        os.system("shutdown /r /t 1")
    else:
        talk("Ok i won't do that")
    button.configure(image=photo)
    root.update()


# Run the code
if __name__ == "__main__":
    while 1:
        if not is_full_screen():
            root.wm_attributes("-topmost", True)
        try:
            if listen:
                respond()
            root.update()
        except Exception as error:
            if "listening timed out while waiting for phrase to start" not in str(error):
                talk("Oops! Something went wrong(")
            else:
                print(error)
            continue
