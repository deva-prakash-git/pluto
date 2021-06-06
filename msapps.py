def apps(query):
    
    import os
    from pluto import speak

    if(('open paint' in query)):
        speak("Yep sure here you go.")
        speak("starting up...")
        os.system('mspaint')
        
    elif(('open notepad' in query)):
        speak("Yep sure here you go.")
        speak("starting up...")
        os.system('notepad')
        
    elif(('open camera' in query)):
        speak("Yep sure here you go.")
        speak("starting up...")
        os.system('start microsoft.windows.camera:')
        
    elif(('open settings' in query) or ('open windows settings' in query)):
        speak("Yep sure here you go.")
        speak("Openning Windows Settings")
        os.system('start ms-settings:')
        
    elif(('show me the calendar' in query) or ('open calendar' in query) or ('show calendar' in query) or ('show me this month in calendar' in query)):
        speak("Yep sure here you go.")
        speak("Openning Calander")
        os.system('start outlookcal:')
    
    elif(('open music player' in query) or ('play music' in query)):      
        speak("Yep sure here you go.")
        speak("Launching Groove Music")
        os.system("start mswindowsmusic:")
        
    elif(('open calculator' in query) or ('open Kalsi' in query)):
        speak("Yep sure here you go.")
        speak("starting up...")
        os.system('calc')

    elif(('open alarm' in query) or ('set alarm' in query) or ('open stopwatch' in query)):
        speak("Yep sure here you go.")
        speak("Openning Alaram & Clock")
        os.system('explorer.exe shell:Appsfolder\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App')

    elif(('open microsoft edge' in query) or ('open edge' in query)):
        speak("Openning Microsoft edge")
        os.system('start microsoft-edge:https://www.google.com')

    elif(('open photos' in query) or ('open my gallery' in query) or ('show my gallery' in query) or ('open my photos' in query)):
        speak("Yep sure here you go.")
        if(('open photos' in query) or ('open my photos' in query)):
            speak("Openning Photos")
            os.system('start ms-photos:')
        elif(('open my gallery' in query) or ('show my gallery' in query)):
            speak("Openning Gallery")
            os.system('start ms-photos:')

    elif(('open windows security' in query) or ('open windows security settings' in query) or ('open windows defender' in query)):
        speak("Yep sure here you go.")
        speak("Openning Windows Security")
        os.system('start windowsdefender:')
        print('starting up...')

    elif(('open video player' in query) or ('open movies and TV' in query)):
        speak("Yep sure here you go.")
        speak("Openning Video Player")
        os.system('start mswindowsvideo:')
        print('starting up...')

          
           
           

    

