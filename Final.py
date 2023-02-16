from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton, MDRaisedButton
from kivymd.uix.behaviors.magic_behavior import MagicBehavior
from screenhelper import screen_helper
from kivymd.uix.dialog import MDDialog
from kivymd.utils import asynckivy
from gtts import gTTS
from googletrans import Translator
from kivy.core.audio import SoundLoader
from kivymd.uix.textfield import MDTextField
import os
import time
from kivy.clock import Clock
import requests
from bs4 import BeautifulSoup
from wotd import WordOfTheDay
from random_word import RandomWords
from kivy.uix.image import Image
import speech_recognition as sr

Window.size = (300, 500)


class MagicButton(MagicBehavior, MDRaisedButton):
    pass


class MainScreen(Screen):
    newword = ""

    def show_about(self):
        close_button = MDFlatButton(text="Close", on_release=self.close_about)
        self.aboutpopup = MDDialog(title="About", text="Created by Krishna "
                                                       "and Shivanjali",
                                   size_hint=(0.7, 1),
                                   buttons=[close_button])
        self.aboutpopup.open()

    def close_about(self, obj):
        self.aboutpopup.dismiss()


class SearchResultScreen(Screen):
    newtranslatedword = ""
    ResultwordMeaning = ""
    myword = ""

class SplashScreen(Screen):
    pass

class HistoryScreen(Screen):
    history_file = ""

    def show_deleted(self):
        close_button = MDFlatButton(text="Close", on_release=self.close_deleted)
        self.deletedpopup = MDDialog(title="Confirmed", text="History deleted",
                                     size_hint=(0.7, 1),
                                     buttons=[close_button])
        self.deletedpopup.open()

    def close_deleted(self, obj):
        self.deletedpopup.dismiss()

    def clear_history(self):
        open("history.txt", "w").close()
        self.show_deleted()


class RandomWordScreen(Screen):
    Wordlength = ""
    RWord = ""
    WordHindi=""
    WordMeaning=""

class WordOfTheDayScreen(Screen):
    word = WordOfTheDay()
    WordOfTheDayHindi=""
    WordOfTheDayMeaning=""


class SavedWordScreen(Screen):
    saved_file = ""

    def show_savedwordsdeleted(self):
        close_button = MDFlatButton(text="Close", on_release=self.close_savedwordsdeleted)
        self.savedwordsdeletedpopup = MDDialog(title="Confirmed", text="Your Saved Words deleted",
                                               size_hint=(0.7, 1),
                                               buttons=[close_button])
        self.savedwordsdeletedpopup.open()

    def close_savedwordsdeleted(self, obj):
        self.savedwordsdeletedpopup.dismiss()

    def clear_savedwords(self):
        open("savedwords.txt", "w").close()
        self.show_savedwordsdeleted()


class SettingScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(SearchResultScreen(name='result'))
sm.add_widget(HistoryScreen(name='history'))
sm.add_widget(RandomWordScreen(name='randomwords'))
sm.add_widget(SavedWordScreen(name='saved'))
sm.add_widget(SettingScreen(name='settings'))


class Samika(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        self.refresh()
        # Clock.schedule_once(self.change_screen, 10)

        self.theme_cls.theme_style = "Light"

        return screen
    # def change_screen(self, dt):
    #     self.screen_helper.screen_manager.current='main'

    def check(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = "Dark"
            self.root.get_screen('result').ids.resim.source = "assets/black.png"
            self.root.get_screen('randomwords').ids.ranim.source = "assets/black.png"
            self.root.get_screen('Wordoftheday').ids.worim.source = "assets/black.png"
            self.root.get_screen('history').ids.hisim.source = "assets/black.png"
            self.root.get_screen('saved').ids.savim.source = "assets/black.png"
            self.root.get_screen('settings').ids.setim.source = "assets/black.png"

        else:
            self.theme_cls.theme_style = "Light"
            self.root.get_screen('result').ids.resim.source = "assets/bg.png"
            self.root.get_screen('randomwords').ids.ranim.source = "assets/bg.png"
            self.root.get_screen('Wordoftheday').ids.worim.source = "assets/bg.png"
            self.root.get_screen('history').ids.hisim.source = "assets/bg.png"
            self.root.get_screen('saved').ids.savim.source = "assets/bg.png"
            self.root.get_screen('settings').ids.setim.source = "assets/bg.png"

    def save_history(self):
        if self.root.get_screen('settings').ids.savehistoryswitch.active:
            text1 = self.root.get_screen('main').ids.namee.text
            count = 1
            file1 = open("history.txt", "a")
            file1 = open("history.txt", "r+")
            for line in file1:
                if line != "\n":
                    count += 1
            file1.close()

            saved_text = (str(count) + " - " + text1)
            file1 = open("history.txt", "a")
            file1.write(saved_text + "\n")
            count = count + 1
            file1.close()
        else:
            pass

    def save_savedWords(self):
        savedtext = self.root.get_screen('main').ids.namee.text
        savedcount = 1
        savedfile = open("savedwords.txt", "a")
        savedfile = open("savedwords.txt", "r+")
        for line in savedfile:
            if line != "\n":
                savedcount += 1
        savedfile.close()

        newsavedtext = (str(savedcount) + " - " + savedtext)
        savedfile = open("savedwords.txt", "a")
        savedfile.write(newsavedtext + "\n")
        savedcount = savedcount + 1
        savedfile.close()

    def translate(self):
        text1 = self.root.get_screen('main').ids.namee.text
        chooselanguage = self.root.get_screen('main').ids.spinner_id.text
        translator = Translator()
        dec_lan = translator.detect(text1)
        input_lang = dec_lan.lang
        text2 = text1
        if input_lang != "en":
            translated = translator.translate(text1, src=dec_lan.lang, dest='en')
            print(translated.text)
            text2 = translated.text

        if chooselanguage == "Hindi":
            new_translated = translator.translate(text2, src="en", dest="hi")
            new_text = new_translated.text
            finnal_text = "Meaning of " + text1 + " in Hindi is.  " + new_text

            translated_words = self.root.get_screen('result').ids.translatedword
            translated_words.font_name = 'font/Hindi'
            translated_words.text = new_text
            language = "hi"

        if chooselanguage == "Chinese":
            new_translated = translator.translate(text2, src="en", dest="zh-cn")
            new_text = new_translated.text
            finnal_text = "Meaning of " + text1 + " in Chinese is.  " + new_text

            translated_words = self.root.get_screen('result').ids.translatedword
            translated_words.font_name = 'font/NotoSansSC.otf'
            translated_words.text = new_text
            language = "zh-cn"

        elif chooselanguage == "Spanish":
            new_translated = translator.translate(text2, src="en", dest="es")
            new_text = new_translated.text
            finnal_text = "Meaning of " + text1 + " in Spanish is.  " + new_text

            translated_words = self.root.get_screen('result').ids.translatedword
            translated_words.text = new_text
            language = "es"

        elif chooselanguage == "Bengali":
            new_translated = translator.translate(text2, src="en", dest="bn")
            new_text = new_translated.text
            finnal_text = "Meaning of " + text1 + " in Bengali is.  " + new_text

            translated_words = self.root.get_screen('result').ids.translatedword
            translated_words.font_name = 'font/Bengali.ttf'
            translated_words.text = new_text
            language = "bn"

        elif chooselanguage == "Punjabi":
            new_translated = translator.translate(text2, src="en", dest="pa")
            new_text = new_translated.text
            finnal_text = "Meaning of " + text1 + " in Punjabi is.  " + new_text

            translated_words = self.root.get_screen('result').ids.translatedword
            translated_words.font_name = 'font/Punjabi'
            translated_words.text = new_text
            language = "hi"

        elif chooselanguage == "Greek":
            new_translated = translator.translate(text2, src="en", dest="el")
            new_text = new_translated.text
            finnal_text = "Meaning of " + text1 + " in Greek is.  " + new_text

            translated_words = self.root.get_screen('result').ids.translatedword
            translated_words.font_name = 'font/Greek.ttf'
            translated_words.text = new_text
            language = "en"

        elif chooselanguage == "French":
            new_translated = translator.translate(text2, src="en", dest="fr")
            new_text = new_translated.text
            finnal_text = "Meaning of " + text1 + " in French is.  " + new_text

            translated_words = self.root.get_screen('result').ids.translatedword
            translated_words.text = new_text
            language = "fr"

        else:
            new_translated = translator.translate(text2, src="en", dest="hi")
            new_text = new_translated.text
            finnal_text = "Meaning of " + text1 + " in Hindi is.  " + new_text

            translated_words = self.root.get_screen('result').ids.translatedword
            translated_words.font_name = 'font/Hindi'
            translated_words.text = new_text
            language = "hi"

        text_speak = gTTS(text=finnal_text, lang=language)

        w=self.root.get_screen('result').ids.mainword
        w.text=text2
        print(new_text)
        print(finnal_text)
        text_speak.save("sound.mp3")
        sound = SoundLoader.load("sound.mp3")

        RWord =self.root.get_screen('result').ids.ResultMeaning

        try:
            search = text2
            soup = BeautifulSoup(requests.get(f"https://google.com/search?q={search}+meaning").text, "html.parser")
            # print(soup.prettify())
            meaning=soup.find("div",class_="MSiauf")
            tempmeaning = meaning.text
            RWord.text = str(tempmeaning)
            print("first")
        except:
            try:
                search = text2
                soup = BeautifulSoup(requests.get(f"https://google.com/search?q={search}+meaning").text, "html.parser")
                # print(soup.prettify())
                meaning = soup.find("div", class_="BNeawe s3v9rd AP7Wnd")
                tempmeaning = meaning.text
                RWord.text = str(tempmeaning)
                print("second")
            except:
                RWord.text = "Sorry try again"


        sound.play()

    def randomwords(self):
        r = RandomWords()
        translator = Translator()
        Wordlength = self.root.get_screen('randomwords').ids.lengthofrandomword
        WordHindi=self.root.get_screen("randomwords").ids.randomwordhindi
        WordMeaning=self.root.get_screen("randomwords").ids.randomwordmeaning
        length = self.root.get_screen('settings').ids.slider.value
        Length_of_word = int(length)
        text1 = r.get_random_word(hasDictionaryDef="true", minLength=Length_of_word, maxLength=Length_of_word)
        print(text1)
        Wordlength.text = "Length of your word is " + str(Length_of_word)
        RWord = self.root.get_screen("randomwords").ids.random_word
        RWord.text = text1

        try:
            search = text1
            soup = BeautifulSoup(requests.get(f"https://google.com/search?q={search}+meaning").text, "html.parser")
            # print(soup.prettify())
            meaning = soup.find("div", class_="MSiauf")
            tempmeaning = meaning.text
            WordMeaning.text = str(tempmeaning)
            print("first")
        except:
            try:
                search = text1
                soup = BeautifulSoup(requests.get(f"https://google.com/search?q={search}+meaning").text, "html.parser")

                # print(soup.prettify())
                meaning = soup.find("div", class_="BNeawe s3v9rd AP7Wnd")
                tempmeaning=meaning.text
                WordMeaning.text=str(tempmeaning)


            except:
                WordMeaning.text="Sorry try again"



        temphin=translator.translate(text1, src="en", dest="hi")
        WordHindi.text=temphin.text
        WordHindi.font_name="font/Hindi"

        speak = gTTS(text=temphin.text, lang="hi")
        speak.save("sound.mp3")

        speakeng = gTTS(text=text1, lang="en")
        speakeng.save("soundeng.mp3")

    def playaudio(self):
        sound = SoundLoader.load("sound.mp3")
        sound.play()


    def playaudioen(self):
            sound = SoundLoader.load("soundeng.mp3")
            sound.play()

    def checkaudio(self):
        word = self.root.get_screen('main').ids.namee
        print(word.text)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening')
            r.pause_threshold = 0.7
            useraudio = r.listen(source)
            try:
                Query = r.recognize_google(useraudio, language='en-In')

                if Query.lower()==word.text.lower():
                    usercorrect="Yes," + Query+ "  is Correct"
                    self.root.get_screen('result').ids.checkword.text = usercorrect
                    self.root.get_screen('result').ids.checkword.text_color = 19/255, 179/255, 47/255, 1
                    self.root.get_screen('result').ids.checkword.font_size =20
                else:
                    userremark = "The word is '" +word.text+"' and you said '"+Query+"'\n Try Again"
                    print(userremark)
                    self.root.get_screen('result').ids.checkword.text = userremark
                    self.root.get_screen('result').ids.checkword.text_color = 1, 0, 0, 1
                    self.root.get_screen('result').ids.checkword.font_size = 18

            except Exception as e:
                print(e)
                self.root.get_screen('result').ids.checkword.text ="Please say it again"

    def reset_search(self):
        print("hyy")
        self.root.get_screen('result').ids.checkword.text = "click on listen to check your pronunciation"
        self.root.get_screen('result').ids.checkword.text_color = 0, 0, 0, 1
        self.root.get_screen('result').ids.checkword.font_size = 18

    def WOTDay(self):
        translator=Translator()
        Wotd = WordOfTheDayScreen.word.string
        WordOfTheDayHindi=self.root.get_screen("Wordoftheday").ids.wordofthedayhindi
        temphindi=translator.translate(Wotd, src="en", dest="hi")
        WordOfTheDayHindi.text=temphindi.text
        WordOfTheDayHindi.font_name="font/Hindi"
        speak = gTTS(text=temphindi.text, lang="hi")
        speak.save("sound.mp3")
        speaken = gTTS(text=Wotd, lang="en")
        speaken.save("soundeng.mp3")


        WordOfTheDayMeaning = self.root.get_screen("Wordoftheday").ids.WordOfTheDayMeaning

        try:
            search = Wotd
            soup = BeautifulSoup(requests.get(f"https://google.com/search?q={search}+meaning").text, "html.parser")
            # print(soup.prettify())
            meaning=soup.find("div",class_="MSiauf")
            tempmeaning = meaning.text
            WordOfTheDayMeaning.text = str(tempmeaning)
        except:
            try:
                search = Wotd
                soup = BeautifulSoup(requests.get(f"https://google.com/search?q={search}+meaning").text, "html.parser")
                # print(soup.prettify())
                meaning = soup.find("div", class_="BNeawe s3v9rd AP7Wnd")
                tempmeaning = meaning.text
                WordOfTheDayMeaning.text = str(tempmeaning)
            except:
                WordOfTheDayMeaning.text = "Sorry try again"

    def refresh(self):
        async def refresh_savedwords():
            await asynckivy.sleep(0.1)
            file = open("savedwords.txt", "a")
            file = open("savedwords.txt", "r")
            saved_file = ""
            no_of_line = 0
            for line in file:
                saved_file = saved_file + line
                no_of_line = no_of_line + 1
            file.close()
            saved_words = self.root.get_screen('saved').ids.usersavedwords
            if no_of_line == 0:
                saved_words.text = "        Nothing is saved yet"
            else:

                saved_words.text = saved_file

        asynckivy.start(refresh_savedwords())

        async def refresh_history():
            await asynckivy.sleep(0.1)
            file = open("history.txt", "a")
            file = open("history.txt", "r")
            history_file = ""
            no_of_line = 0
            for line in file:
                history_file = history_file + line
                no_of_line = no_of_line + 1
            file.close()
            history_words = self.root.get_screen('history').ids.historywords
            if no_of_line == 0:
                history_words.text = "        Nothing is saved yet"
            else:

                history_words.text = history_file

        asynckivy.start(refresh_history())

    def searchword(self):
        file = open("savedwords.txt", "r")
        word = self.root.get_screen('main').ids.namee.text
        s = " "

        while (s):
            s = file.readline()
            l = s.split()
            if word in l:
                self.likeno = 1
                break
            else:
                self.likeno = 2
        self.select()

    def select(self):
        self.likeno = self.likeno + 1
        if self.likeno % 2 == 0:
            self.root.get_screen("result").ids.hearticon.icon = "heart"
            self.root.get_screen("result").ids.hearticon.text_color = 1, 0, 0, 1
        else:
            self.root.get_screen("result").ids.hearticon.icon = "heart-outline"
            self.root.get_screen("result").ids.hearticon.text_color = 0, 0, 0, 1


    def listen(self):
        self.root.get_screen("main").ids.micicon.icon = "microphone-outline"
        newword = self.root.get_screen('main').ids.namee
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening')
            r.pause_threshold = 0.7
            audio = r.listen(source)
            try:
                Query = r.recognize_google(audio, language='en-In')

                print("the query is printed='", Query, "'")
                newword.text = Query

            except Exception as e:
                print(e)
                print("Please say it again")
                return "None"
            return Query

    def transapp(self):
        chooselanguage = self.root.get_screen('settings').ids.applang_id.text
        print(chooselanguage)
        temp=self.root.get_screen('settings').ids.setw1.text
        print(temp)



Samika().run()
