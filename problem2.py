# installl an external module and use it to perform an operation of your interest
import pyttsx3
engine = pyttsx3.init()

engine.say('''Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.
''')
engine.runAndWait()