screen_helper = """
ScreenManager:
    id:scr_mngr
    SplashScreen:
    MainScreen:
    SearchResultScreen:
    RandomWordScreen:
    WordOfTheDayScreen:
    SavedWordScreen:
    HistoryScreen:
    SettingScreen:
<SplashScreen>:
    name: "Splash"
    Screen:
        Image:
            source:'assets/splash.gif'
            allow_stretch: True
            anim_delay: 0
            anim_reset: True
        MDIconButton:
            icon:"arrow-right-thick"
            pos_hint:{"center_x":0.8,"center_y":0.1}
            on_press:root.manager.current='main'

<MainScreen>:
    id:mainscreen
    name:'main'
    Screen:
        Image:
            id:savim
            pos:self.pos
            source: 'assets/temp.png'
        MDTextField:
            id:namee
            hint_text:"Enter the word"
            helper_text:"you can input in any language"
            helper_text_mode:'on_focus'
            icon_right:'book-search'
            icon_right_color:app.theme_cls.primary_color
            pos_hint:{'center_x': 0.5, 'center_y': 0.7}
            size_hint_x:None
            width:200

        MDIconButton:
            id:micicon
            icon:"microphone-outline"
            pos_hint:{"center_x":0.3,"center_y":0.63}
            on_press:self.icon="microphone"
            on_release:app.listen()

        MagicButton:
            text:"Search"
            pos_hint:{'center_x': 0.43, 'center_y': 0.45}
            on_press:self.grow()
            on_release:root.manager.current='result'
            on_release:app.translate()
            on_release:app.searchword()
            on_release:app.save_history()


        Spinner:
            id:spinner_id
            text:"Hindi"
            background_color:(1/255,200/255,240/255,100)
            font_size:20
            sync_height:True
            values:["Hindi","Spanish","Bengali","Punjabi","Chinese","French","Greek"]
            pos_hint:{'center_x': 0.65, 'center_y': 0.62}
            size_hint:(0.25,0.05)



        MDNavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Samika'
                            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                            elevation:10
                        Widget   


            MDNavigationDrawer:
                id:nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '20dp'
                    padding: '10pd'
                    Image:
                        source:'assets/samika.png'
                        size_hint_y:None


                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text:'RandomWords'
                                on_press:app.randomwords()
                                on_press:root.manager.current='randomwords'
                                on_press:nav_drawer.set_state("close")
                                IconLeftWidget:
                                    icon:'shuffle-variant'

                            OneLineIconListItem:
                                text:'Word of the day'
                                on_press:root.manager.current='Wordoftheday'
                                on_press:app.WOTDay()
                                IconLeftWidget:
                                    icon:'calendar-today'


                            OneLineIconListItem:
                                text:'History'
                                on_press:root.manager.current='history'
                                on_press:nav_drawer.set_state("close")
                                on_press:app.refresh()
                                IconLeftWidget:
                                    icon:'history'

                            OneLineIconListItem:
                                text:'Saved Words'
                                on_press:root.manager.current='saved'
                                on_press:nav_drawer.set_state("close")
                                on_press:app.refresh()
                                IconLeftWidget:
                                    icon:'content-save'

                            OneLineIconListItem:
                                text:'Settings'
                                on_press:root.manager.current='settings'
                                IconLeftWidget:
                                    icon:'account-edit'

                    MDLabel:
                        text:'  Email@gmail.com'
                        font_style:'Subtitle1'
                        size_hint_y:None
                        height:self.texture_size[1]
                    MDFlatButton:
                        text:'  About'
                        on_press:root.show_about()
                        on_press:nav_drawer.set_state("close")
                        font_style:'Subtitle1'

<SearchResultScreen>:
    name:'result'
    Screen:
        Image:
            id:resim
            pos:self.pos
            source: 'assets/bg.png'

        MDLabel:
            text:"Your word is"
            halign:'center'
            pos_hint: {'center_x':0.5,'center_y':0.9}
            font_style:'H3'
            font_size:26
        MDLabel:
            id:mainword
            text:root.myword
            halign:'center'
            pos_hint: {'center_x':0.5,'center_y':0.8}
            font_size:22


        MDLabel:
            id:translatedword
            text:root.newtranslatedword
            halign:'center'
            pos_hint: {'center_x':0.5,'center_y':0.73}
            font_size:18
            font_style:'Subtitle2'

        MDIconButton:
            id:hearticon
            icon:"heart-outline"
            pos_hint:{'center_x': 0.15, 'center_y': 0.1}
            theme_text_color:"Custom"
            text_color:0,0,0,1
            on_press:app.select()
            #on_press:self.twist()
            on_release:app.save_savedWords()

        ScrollView:
            size_hint_y:0.42
            pos_hint: {'center_x':0.5,'center_y':0.5}
            MDList:
                MDLabel:
                    id:ResultMeaning
                    text:root.ResultwordMeaning 
                    size_hint_y: None
                    height: self.texture_size[1]
                    font_style:'Subtitle2'
                    font_size:16
                    
        MDLabel:
            id:checkword
            text:"click on listen to check your pronunciation"
            theme_text_color:"Custom"
            text_color:0,0,0,1
            halign:'center'
            size_hint:(0.7,0.15)
            pos_hint: {'center_x':0.5,'center_y':0.24}
            font_size:16
        
        MagicButton:
            text:"listen"
            pos_hint:{'center_x': 0.48, 'center_y': 0.13}
            size_hint:(0.05,0.05)
            on_press:self.shake()
            on_release:app.checkaudio()
        
        MagicButton:
            text:"play"
            pos_hint:{'center_x': 0.48, 'center_y': 0.07}
            size_hint:(0.05,0.05)
            on_press:self.shake()
            on_release:app.playaudio() 



        MDFloatingActionButton:
            icon:"arrow-left-bold"
            on_press:root.manager.current='main'
            on_press:app.reset_search()
            pos_hint:{"center_x": 0.8, "center_y": 0.1}

<RandomWordScreen>:
    name:'randomwords'
    Screen:
        Image:
            id:ranim
            pos:self.pos
            source: 'assets/bg.png'
        MDLabel:
            text:'Your RandomWord is'
            halign:'center'
            size_hint_y: None
            pos_hint: {'center_x':0.5,'center_y':0.9}
            font_style:'H3'
            font_size:36

        MDLabel:
            id:lengthofrandomword
            text:root.Wordlength 
            halign:'center'
            size_hint_y: None
            font_size:14
            pos_hint: {'center_x':0.5,'center_y':0.75}

        MDLabel:
            id:random_word
            text:root.RWord
            halign:'center'
            size_hint_y: None
            font_size:25
            pos_hint: {'center_x':0.5,'center_y':0.7}

        MDLabel:
            id:randomwordhindi
            text:root.WordHindi 
            halign:'center'
            size_hint_y: None
            pos_hint: {'center_x':0.5,'center_y':0.65}

        ScrollView:
            size_hint_y:0.45
            padding:dp(10)
            spacing:dp(10)
            pos_hint: {'center_x':0.5,'center_y':0.4}
            MDList:
                MDLabel:
                    id:randomwordmeaning
                    text:root.WordMeaning 
                    size_hint_y: None
                    height: self.texture_size[1]
                    font_style:'Subtitle2'
                    font_size:16

        MagicButton:
            text:"play(english)"
            pos_hint:{'center_x': 0.5, 'center_y': 0.13}
            size_hint:(0.05,0.05)
            on_press:self.shake()
            on_release:app.playaudioen()

        MagicButton:
            text:"play(hindi)"
            pos_hint:{'center_x': 0.5, 'center_y': 0.052}
            size_hint:(0.05,0.05)
            on_press:self.shake()
            on_release:app.playaudio()

        MDFloatingActionButton:
            icon:"fan"
            on_press:app.randomwords()
            pos_hint:{"center_x": 0.2, "center_y": 0.1}

        MDFloatingActionButton:
            icon:"arrow-left-bold"
            on_press:root.manager.current='main'
            pos_hint:{"center_x": 0.8, "center_y": 0.1}


<WordOfTheDayScreen>:
    name:"Wordoftheday"
    Screen:
        Image:
            id:worim
            pos:self.pos
            source: 'assets/bg.png'
        MDLabel:
            text:'Word of the day   is'
            halign:'center'
            pos_hint: {'center_x':0.5,'center_y':0.9}
            font_style:'H3'
            font_size:36

        MDLabel:
            text:root.word.string
            halign:'center'
            pos_hint: {'center_x':0.5,'center_y':0.75}
            font_size:22

        MDLabel:
            id:wordofthedayhindi
            text:root.WordOfTheDayHindi 
            halign:'center'
            size_hint_y: None
            pos_hint: {'center_x':0.5,'center_y':0.7}

        ScrollView:
            size_hint_y:0.5
            pos_hint: {'center_x':0.5,'center_y':0.4}
            MDList:
                MDLabel:
                    id:WordOfTheDayMeaning
                    text:root.WordOfTheDayMeaning 
                    size_hint_y: None
                    height: self.texture_size[1]
                    font_style:'Subtitle2'
                    font_size:16
        MagicButton:
            text:"play(english)"
            pos_hint:{'center_x': 0.21, 'center_y': 0.1}
            size_hint:(0.04,0.05)
            on_press:self.shake()
            on_release:app.playaudioen()

        MagicButton:
            text:"play(hindi)"
            pos_hint:{'center_x': 0.55, 'center_y': 0.1}
            size_hint:(0.04,0.05)
            on_press:self.shake()
            on_release:app.playaudio()

        MDFloatingActionButton:
            icon:"arrow-left-bold"
            on_press:root.manager.current='main'
            pos_hint:{"center_x": 0.8, "center_y": 0.1}

<HistoryScreen>:
    name:'history'
    Screen:
        Image:
            id:hisim
            pos:self.pos
            source: 'assets/bg.png'
        BoxLayout:
            orientation: 'vertical'
            padding: dp(20)
            spacing: dp(20)
            MDLabel:
                text:"History"
                halign:'center'
                size_hint_y:0.1
                pos_hint: {'center_x':0.5,'center_y':0.8}
                font_style:'H3'
                font_size:35

            ScrollView:
                size_hint_y: 0.75
                MDList:
                    MDLabel:
                        id:historywords
                        text:root.history_file 
                        size_hint_y: None
                        height: self.texture_size[1]
                        font_style:'Subtitle2'
                        font_size:16

            MDRectangleFlatButton:
                text:'Clear'
                on_press:root.clear_history()
                on_press:app.refresh()
                pos_hint: {'center_x':0.5,'center_y':0.2}

        MDFloatingActionButton:
            icon:"arrow-left-bold-outline"
            on_press:root.manager.current='main'
            pos_hint:{"center_x": 0.8, "center_y": 0.1}



<SavedWordScreen>:
    name:'saved'
    Screen:
        Image:
            id:savim
            pos:self.pos
            source: 'assets/bg.png'
        BoxLayout:
            orientation: 'vertical'
            padding: dp(20)
            spacing: dp(20)
            MDLabel:
                text:"Saved Words"
                halign:'center'
                size_hint_y:0.1
                pos_hint: {'center_x':0.5,'center_y':0.8}
                font_style:'H3'
                font_size:35

            ScrollView:
                MDList:
                    MDLabel:
                        id:usersavedwords
                        text:root.saved_file 
                        size_hint_y: None
                        height: self.texture_size[1]
                        font_style:'Subtitle2'
                        font_size:16


            MDRectangleFlatButton:
                text:'Clear'
                on_press:root.clear_savedwords()
                on_press:app.refresh()
                pos_hint: {'center_x':0.5,'center_y':0.2}

        MDFloatingActionButton:
            icon:"arrow-left-bold"
            on_press:root.manager.current='main'
            pos_hint:{"center_x": 0.8, "center_y": 0.1}

<SettingScreen>:
    name:'settings'
    Screen:
        Image:
            id:setim
            pos:self.pos
            # allow_stretch:True
            source: 'assets/bg.png'
        MDLabel:
            id:setw1
            text:"Settings"
            halign:'center'
            size_hint_y:0.2
            pos_hint: {'center_x':0.5,'center_y':0.87}
            font_style:'H3'
            font_size:36

        MDLabel:
            text:"Dark theme"
            align:'center'
            size_hint_x:None
            pos_hint:{"center_x": 0.4, "center_y": 0.75}

        MDSwitch:
            pos_hint:{"center_x": 0.7, "center_y": 0.75}
            on_active:app.check(*args)
            size_hint_x:None

        MDLabel:
            text:"Save History"
            align:'center'
            size_hint_x:None
            pos_hint:{"center_x": 0.4, "center_y": 0.65}

        MDSwitch:
            id:savehistoryswitch
            pos_hint:{"center_x": 0.7, "center_y": 0.65}
            active:True
            size_hint_x:None

        MDLabel:
            text:"Length of Random Word"
            align:'center'
            size_hint_y:None
            pos_hint:{"center_x": 0.7, "center_y": 0.4}

        MDSlider:
            id:slider
            max:11
            min:5
            hint: False
            pos_hint:{"center_x":0.5,"center_y":0.25}
            size_hint:0.7,0.1
            on_touch_down:print(str(int(slider.value)))


        MDLabel:
            text:str(int(slider.value))
            align:'center'
            ize_hint_x:None
            font_style:"H5"
            pos_hint:{"center_x": 1, "center_y": 0.32}
            
        MDLabel:
            text:"App language"
            align:'center'
            size_hint_x:None
            pos_hint:{"center_x":0.4,"center_y":0.55}
            
        Spinner:
            id:applang_id
            text:"Hindi"
            background_color:(1/255,200/255,240/255,100)
            font_size:20
            sync_height:True
            values:["Hindi","Spanish","Bengali","Punjabi","Chinese","French","Greek"]
            pos_hint:{"center_x":0.7,"center_y":0.55}
            size_hint:(0.25,0.05)
            on_release:app.transapp()


        MDFloatingActionButton:
            icon:"arrow-left-bold"
            on_press:root.manager.current='main'
            pos_hint:{"center_x": 0.8, "center_y": 0.1}


"""
