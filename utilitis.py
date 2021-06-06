def service(query):
    import os
    from pluto import speak

    if(('disconnect wi-fi' in query)):
        speak("Yep sure")
        speak("Disconnecting from connected Welifi Network")    
        os.system("netsh wlan disconnect")
        print('starting up...')

    elif(('show wi-fi' in query) or ('show wi-fi network' in query) or ('show me wi-fi network' in query) or ('show available wi-fi network' in query) or ('show me available wi-fi network' in query) or ('open wi-fi network' in query)):
        speak("Yep sure")
        os.system("start ms-availablenetworks:")
        print('starting up...')

    elif(('show notifications' in query) or ('show notifications' in query) or ('show notifications panel' in query) or ('show my notifications' in query) or ('show my notifications' in query)):
        speak("Yep sure")
        speak("Here is your notifications Pannel")
        os.system("start ms-actioncenter:")
        print('starting up...')

