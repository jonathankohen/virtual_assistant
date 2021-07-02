import pyttsx3

engine = pyttsx3.init()


rate = engine.getProperty("rate")
print(rate)
engine.setProperty("rate", 125)

volume = engine.getProperty("volume")
print(volume)
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

engine.say(
    f"Hello! I'm Lily, a virtual assistant here to help with anything you may need. My current speaking rate is {str(rate)}, and my volume is currently set to {str(volume)} out of one."
)
engine.runAndWait()
engine.stop()

engine.save_to_file("Hello world", "test.mp3")
engine.runAndWait()


def onStart(name):
    print("starting", name)


def onWord(name, location, length):
    print("word", name, location, length)


def onEnd(name, completed):
    print("finishing", name, completed)
    if name == "notes":
        engine.say("Sure, I can jot that down for you")
    elif name == "splinter":
        engine.endLoop()


engine.connect("started_utterance", onStart)
engine.connect("started_word", onWord)
engine.connect("finished_word", onEnd)

# book something
# order pizza
# look stuff up
# make a call
# tell time
# calculate
# notes
# book a cab