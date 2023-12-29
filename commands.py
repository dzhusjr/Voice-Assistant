commands_dict = {
    "open_opera()":["open opera","open browser"],
    "open_discord()":["open discord"],
    "open_vscode()":["open vs code"],
    """talk("Here you go to Stack Over flow.Happy coding");os.system(f"START https://stackoverflow.com/")""":["open stack overflow"],
    """talk("Here you go to Google");os.system(f"START https://www.google.com.ua/?hl=ua")""":["open google"],
    """talk("Here you go to Youtube");os.system(f"START https://www.youtube.com/")""":["open youtube"],
    "create_task(' '.join(words[words.index('task')+1:]))":["task"],
    "change_uname(words[words.index('me')+1])":["call me"],
    "change_uname(words[words.index('is')+1])":["my name is"],
    "change_uname(words[words.index('to')+1])":["change my name to"],
    "change_assname(words)":["change name","change your name"],
    """talk(random.choice([f"You've named me {data['assname'].capitalize()}.",f"My friends call me {data['assname'].capitalize()}.",f"I'm {data['assname'].capitalize()}. Pleased to meet you.",f"My name is {data['assname'].capitalize()}, but you knew that already."]))""":["your name"],
    "play(words)":["play "],
    "media.set_pause(1);is_playing = False":["pause"],
    "media.set_pause(0);is_playing = True":["resume","continue"],
    "media.stop();is_playing = False":["stop"],
    "information(' '.join(words[words.index('wikipedia')+1:]))":["wikipedia"],
    "information(' '.join(words[words.index('is')+1:]))":["what is", "what means"],
    """talk("Here is your task list");os.system(f"START {task_path}")""":["show tasks","show notes","show todo list","show me notes","show me todo list","show me task list","show me my notes","show me my todo list","show me my task list"],
    "create_task(' '.join(words[words.index('down')+1:]))":["write down"],
    "create_task(' '.join(words[words.index('note')+1:]))":["note"],
    "clear_todo_list()":["clear to-do list", "empty to-do list", "delete notes","clear notes", "remove notes"],
    """os.system("del /s /q %systemdrive%\$Recycle.bin");talk("Done!")""":["clear trash", "empty trash", "delete trash", "remove trash","clear recycle", "empty recycle"],
    "search(words)":["search","google"],
    """unit_convert(' '.join(words[words.index('convert')+1:]))""":["convert"],
    """talk(f"Locating {' '.join(words[words.index('is')+1:])}");os.system(f"START https://www.google.nl/maps/place/{' '.join(words[words.index('is')+1:])}")""":["where is"],
    "shutdown()":["shutdown","turn off my computer","shut down","turn of my computer"],
    "restart()":["restart"],
    "speed_test()":["speedtest","speed test","internet speed"],
    """talk(f"It is {round(eval(query.replace('calculate','').replace('count','').replace('divided by','/').replace('multiply by','*')),2)}")""":["calculate","count"],
    "pyautogui.press('volumeup')":["volume up","increase volume","louder"],
    "pyautogui.press('volumedown')":["volume down","decrease volume","quieter","lower"],
    "pyautogui.press('volumemute')":["mute","silence"],
    """talk("I won't respond to that")""":['*','stupid'],
    "talk('Ok');listen = False;button.configure(image = photo)":["nothing","forget","bye"],
    "talk('Hi! Nice to hear you!')":["hello","good morning","good evening","good afternoon","hi","hey"],
    """talk(f'It is {datetime.today().strftime("%B %d, %Y")}')""":["date"],
    """talk(f'It is {datetime.now().strftime("%H:%M")}')""":["time"],
    "talk(pyjokes.get_joke())":["joke"],
    "talk('The quick brown fox jumped over the lazy dog')": ["tell me something"],
    "talk('I have been created by Roman.')":["who made you" ,"who created you"],
    "talk('If you talk then definitely your human.')":["who am i"],
    """talk("Thanks to Roman. Further It's a secret")""":["why you came to world"],
    "talk('It is 7th sense that destroy all other senses')":["is love"],
    """talk(f"I'm {assname.capitalize()}, your virtual assistant")""":["who are you"],
    "talk('I was created as a Minor project by Mister Roman')":["reason for you"],
    """talk("It's hard to understand")""":["love you"],
    """talk("I'm not a robot")""":["are you a robot"],
    """talk("I'm a robot")""":["are you a human"],
    """talk(random.choice(['I understand we all need to recharge once in a while.',"Listen to me. Put away all the gadgets right now and take a nap. I'll wait here.",'Try concatenating natural speech. That usually makes me drift right off.',"If you can't sleep, try closing your eyes and taking some deep breaths."]))""":["i want to sleep","i want to rest","i'm tired","i am tired"],
    """talk(random.choice(["I'm sorry you're feeling that way sometimes. Taking a quiet moment can help. You could try listening to your favorite music or doing some simple stretches.","I am sorry you are feeling this way. Talking to a friend or family member might help."]))""":["i'm sad"],
    """talk(random.choice(['Well, that just brightened my whole day.',"That's great. You should write down everything about how you're feeling at the minute so you can remember it."]))""":["i'm happy"],
    """talk("I'm sorry you're going through this. I've heard that taking your mind off things can help take a break and find something that makes you smile.")""":["i'm angry"],
    """talk("I'm sorry you're afraid, but I'm glad you're asking for help. Take some deep breaths and think about all the people and the things that are there for you. If you feel like you're in danger, please find help.")""":["i'm scared"],
    """talk("That may be beyond my abilities at the moment")""":["give me some ideas","give me an idea"],
    """talk("I'm not sure about, may be you should give me some time")""":["be my gf","be my bf","be my girlfriend"],
    "talk(f'I like you too {uname.capitalize()}')":["i like you","you are nice","you are cool","you are the best","you're nice","you're cool","you're the best"],
    """talk(random.choice(["I am fine, Thank you. How are you, Sir?","I'm fine, glad you asked me that"]))""":["how are you","how is it going"],
    """talk("It's good to know that your fine")""":["fine","good"],
    "talk('At your service')":["thank you","thanks"],
    "asyncio.get_event_loop().run_until_complete(getweather(' '.join(words[words.index('in')+1:])))":["weather in"],
    """talk(random.choice(["Thanks for giving me your time","Nice to meet you. Bye"]));quit()""":["exit","quit"],
    """winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True);talk("Recycle Bin is empty")""":["empty recycle bin"],
    """talk("Hibernating");os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")""":["sleep","hibernate"],
    """talk("locking the device");os.system("rundll32.exe user32.dll,LockWorkStation")""":["lock"]
}