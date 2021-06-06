def sys(query):
    import os
    import pluto as pl

    if(('open control panel' in query) or ('control panel' in query)):
        pl.speak("Yep sure here you go.")
        pl.speak("Openning Control Pannel")
        os.system('start control')
        

    elif(('open file explorer' in query) or ('show me the files in this pc' in query)):
        pl.speak("Yep sure here you go.")
        pl.speak("Openning File Explorer")
        os.system('explorer')
        

    elif(('open run' in query) or ('open run command' in query) or ('open run command box' in query)):
        pl.speak("Yep sure here you go.")
        pl.speak("Openning Run Command Starting Up")
        os.system("explorer.exe Shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}")
      

    elif(('open command prompt' in query)):
        pl.speak("Yep sure here you go.")
        pl.speak("Launching Command Prompt")
        os.system("cmd") 

    elif(('open task manager' in query)):
        pl.speak("Yep sure here you go.")
        pl.speak("Openning TaskManager")
        os.system("taskmgr")

    elif(('open my computer' in query) or ('open this PC' in query)):
        pl.speak("Yep sure here you go.")
        pl.speak("Openning My Computer")
        os.system("explorer =")
       
    elif(('show my drives in this pc' in query) or ('show my drives' in query) or ('show my drive' in query)):
        pl.speak("Yep sure ")
        pl.speak("Here is Your drives")
        os.system("explorer =")
        
    elif(('show downloads folder' in query) or ('open downloads folder' in query) or ('show my downloads' in query) or ('open my downloads folder' in query) or ('show my downloads folder' in query)):
        pl.speak("Yep sure here you go.")
        pl.speak("Openning your Downloads")
        os.system('explorer shell:::{088e3905-0323-4b02-9826-5d99428e115f}')