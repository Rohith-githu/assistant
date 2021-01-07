from mod import *
with open('settings.json') as f:
    data = json.load(f)
date_string = datetime.datetime.now().strftime("%d%m%Y%H%M%S")

def take_voice() :
	r = sr.Recognizer()
	with sr.Microphone() as source :
		r.energy_threshold = data['energy_threshold']
		r.adjust_for_ambient_noise(source, data['ambience_meter'])
		print('Listening...')
		audio = r.listen(source)
		r.pause_threshold = data['pause_threshold']
		try :
			print('recognizing...')
			query = r.recognize_google(audio, language=data['language'])
			print(f'You : {query}')
		except Exception as e:
			print('pls say that again')
			return 'None'
		return query

def say(query):
    print(f'{query}')
    tts = gTTS(query)
    tts.save(f'voice{date_string}.mp3')
    playsound(f'voice{date_string}.mp3')
    os.unlink(f'voice{date_string}.mp3')

def screenshot():
	screenshot = pyautogui.screenshot()
	screenshot.save(f'Screenshots/screenshot{date_string}.png')

def google(query):
    webbrowser.open(f'https://www.google.com/search?q={query}')

def encyclopedia(ask):
	try :
		app_id = 'WT7WP4-U5G6E93E2R'
		client = wolframalpha.Client(app_id)
		res = client.query(ask)
		for pod in res.pods:
			say('These are the results from WolframAlpha : {p.text}'.format(p=pod))
	except StopIteration :
		google(ask)
	except Exception as e:
		if 'what is' in ask :
			ask = ask.replace('what is', '')
			say(wikipedia.summary(ask))
		elif 'who is' in ask :
			ask = ask.replace('who is', '')
			say(wikipedia.summary(ask))

def password():
    set1 = string.ascii_uppercase
    set2 = string.ascii_lowercase
    set3 = string.digits
    set4 = string.punctuation
    passlen = 8
    passset = []
    passset.extend(set1)
    passset.extend(set2)
    passset.extend(set3)
    passset.extend(set4)
    random.shuffle(passset)
    pyperclip.copy(''.join(passset[0:passlen]))

def wiki(query) :
	query = query.replace('wikipedia')
	say(wikipedia.summary(query))

def maps(place) :
	say(f'searching directions for {place}')
	webbrowser.open(f'https://www.google.co.in/maps/place/{place}')
	say(f'heres the {place}')


def call(text):
	action_call = 'electra'
	text = text.lower()
	if action_call in text or 'elektra' in text:
		return True
	return False


def today_date():
	now = datetime.datetime.now()
	date_now = datetime.datetime.today()
	week_now = calendar.day_name[date_now.weekday()]
	month_now = now.month
	day_now = now.day

	months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
	]

	ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
	]

	say("Today is " + week_now + ", " + months[month_now - 1] + " the " + ordinals[day_now - 1] + ".")

def say_hello(text):
    greet = ['Hi sir!', 'What are you doing?','are you bored','What can i do for you?','yaa i am here']
    return say(random.choice(greet))