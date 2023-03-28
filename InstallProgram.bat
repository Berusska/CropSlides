title Instalace Programu
@echo off
cls
::color 2
echo """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
echo """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
echo """                                                                                            """  
echo """         ______                _____ ___     __                                             """ 
echo """        / ____/________  ____ / ___// (_)___/ /__  _____                                    """
echo """       / /   / ___/ __ \/ __ \\__ \/ / / __  / _ \/ ___/                                    """
echo """      / /___/ /  / /_/ / /_/ /__/ / / / /_/ /  __(__  )                                     """ 
echo """      \____/_/   \____/ .___/____/_/_/\__,_/\___/____/                                      """ 
echo """                     /_/                                                                    """
echo """                                                          @@@@@                             """  
echo """                                                         @@@@                               """  
echo """                                                        @@@.                                """  
echo """                                                      &@@@                                  """  
echo """                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                          """  
echo """                             ,@@@@@@@@@@@@@@@  _  @@@@@@@@@@@@@@@@                          """  
echo """                              @@@@@@@@@@@@@@@ |_| @@@@@@@@@@@@@@&                           """  
echo """                               &@@@@@@@@@@@@@ |\  @@@@@@@@@@@@@@                            """  
echo """                                @@@@@@@@@@@@@@@ \/ @@@@@@@@@@@@                             """  
echo """                                  @@@@@@@@@@@@@ /\ @@@@@@@@@@                               """  
echo """                                    &@@@@@@@@@@@@@@@@@@@@@(                                 """  
echo """                                                                                          TS""" 
echo """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
echo """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
echo.
echo.
echo Vitejte u instalace programu!
echo.
echo Hint: Instalacni soubor by nemel byt umisten ve slozce, ceste ke slozce, v niz je diakritika.
echo Aktualni cesta je %~dp0
echo    K pokracovani stisknete jakoukoli klavesu.
echo.
pause > nul
echo Nyni se Vam spusti instalace programovaciho jazyku Python 3.11.2.
echo     Zaskrknete moznost "Add Python to PATH".
echo     Zvolte napr. moznost "Install now" (pokud nebude v nabidce, instalaci Pythonu zavrete)
timeout 2 > nul 
%~dp0\Source\python-3.11.2-amd64.exe
echo     K pokracovani stisknete jakoukoli klavesu.
pause > nul
echo.
echo Aktualne mate Python na ceste:
echo ________________________________________________________________________________________________________________________
echo.
where python
echo ________________________________________________________________________________________________________________________
echo     Pokud tomu je tak a tedy je Python nainstalovan, stisknete Enter.
pause > nul
echo.
echo Nyni se Vam nainstaluji potrebne python moduly.
echo ________________________________________________________________________________________________________________________
echo.
::%~dp0\Source\InstallModules.bat
pip install Pillow
pip install pathlib
pip install pdf2image
echo _________________________________________________________________________________________________________________________
echo     Moduly nainstalovany. Pokud nektery ne, doreste jeho instalaci dodatecne.
echo     Nyni stisknete libovolnou klavesu.
echo.
pause > nul
echo.
echo Nyni se zjistuje cesta zdrojoveho kodu programu.
timeout 2 > nul

::Následující najde python skript a uloží jeho cestu; vyhledává i v podsložkách
for /r ./ %%a in (*) do if "%%~nxa"=="CropSlides.py" set CestaProgramu=%%~dpnxa

echo     Aktualni cesta zdrojoveho kodu je:
if defined CestaProgramu (echo          %CestaProgramu%) else (echo      File not found)
::https://devblogs.microsoft.com/oldnewthing/20120731-00/?p=7003
::https://stackoverflow.com/questions/13876771/find-file-and-return-full-path-using-a-batch-file


echo.
echo Nyni se vytvori spousteci soubor pro program.
set CestaPythonu=python 
set prikaz=%CestaPythonu% %CestaProgramu%
::echo %prikaz%


echo echo off >RunProgram.bat
echo cls >>RunProgram.bat
echo echo.    >>RunProgram.bat
echo echo """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" >> RunProgram.bat
echo echo """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" >> RunProgram.bat
echo echo """                                                                                            """ >> RunProgram.bat 
echo echo """         ______                _____ ___     __                                             """ >> RunProgram.bat
echo echo """        / ____/________  ____ / ___// (_)___/ /__  _____                                    """ >> RunProgram.bat 
echo echo """       / /   / ___/ __ \/ __ \\__ \/ / / __  / _ \/ ___/                                    """ >> RunProgram.bat
echo echo """      / /___/ /  / /_/ / /_/ /__/ / / / /_/ /  __(__  )                                     """ >> RunProgram.bat 
echo echo """      \____/_/   \____/ .___/____/_/_/\__,_/\___/____/                                      """ >> RunProgram.bat 
echo echo """                     /_/                                                                    """ >> RunProgram.bat
echo echo """                                                          @@@@@                             """ >> RunProgram.bat 
echo echo """                                                         @@@@                               """ >> RunProgram.bat 
echo echo """                                                        @@@.                                """ >> RunProgram.bat 
echo echo """                                                      &@@@                                  """ >> RunProgram.bat 
echo echo """                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                          """ >> RunProgram.bat 
echo echo """                             ,@@@@@@@@@@@@@@@  _  @@@@@@@@@@@@@@@@                          """ >> RunProgram.bat 
echo echo """                              @@@@@@@@@@@@@@@ |_| @@@@@@@@@@@@@@&                           """ >> RunProgram.bat 
echo echo """                               &@@@@@@@@@@@@@ |\  @@@@@@@@@@@@@@                            """ >> RunProgram.bat 
echo echo """                                @@@@@@@@@@@@@@@ \/ @@@@@@@@@@@@                             """ >> RunProgram.bat 
echo echo """                                  @@@@@@@@@@@@@ /\ @@@@@@@@@@                               """ >> RunProgram.bat 
echo echo """                                    &@@@@@@@@@@@@@@@@@@@@@(                                 """ >> RunProgram.bat 
echo echo """                                                                                          TS""" >> RunProgram.bat
echo echo """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" >> RunProgram.bat
echo echo """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" >> RunProgram.bat
echo echo. >>RunProgram.bat
echo %prikaz% >> RunProgram.bat 
::Nebo lze také ::echo|set /p=%CestaPythonu% %CestaProgramu% > RunProgram.bat 
echo exit 0 >> RunProgram.bat

timeout 2 > nul
echo     Spousteci soubor RunProgram.bat byl vytvoren. Naleznete jej ve zdejsi slozce.
::https://stackoverflow.com/questions/2027070/how-to-concatenate-strings-in-a-windows-batch-file
::@pause
echo.
echo ........................................................................................................................
echo Instalace (pokus o ni) dokoncena. Stisknete jakoukoli klavesu, by jste ukoncili instalaci...
pause > nul 
echo Zaviram instalacni program...
timeout 2 > nul
exit 0







::https://www.itninja.com/question/copying-one-line-output-from-a-text-file-into-a-batch-file-as-a-variable
::https://stackoverflow.com/questions/19642622/how-do-i-echo-ascii-art-that-contains-special-characters-in-a-batch-file
::https://patorjk.com/software/taag/#p=testall&h=3&v=3&c=bash&f=Electronic&t=instalation


::https://asciiart.club/
::▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒░░░░▒▒░░░░▒▒▒▒░░░░░▒▒▒░░░░░▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░▒▒▒▒░░░
::▓▓▓▓▓▓▓▓▓█▓▓▓▓▒▒▒░░▒▒▒'jφ▄░░░░░▒▒▒▒▒░░░`░▒░▒▒▒╢╣▒▒▒▒░░░╢▒▒░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░░░
::▓▓▓▓▓▓▓▓▓▒░░▒▒▒▒░░░▒@░`░▀▓█▓▒¡░▒▓▓▒▒▒░╫▒░▒╢╣▒╣╣▒▒▒▒▒░░▒╣▒░¡▒▒▒▒▒░▒▒▒░░░▒▒▒▒▒░▒▒
::▒░▀▓▓▓▓▓█▓▓░░░▒▒░▒▓▓▓▒Ñ▄;`╙▓██▒▒▒▓█▒░╠▓░▒▒╢▓▓▓▒▒▒▒▒▒░░▒▒░░░▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒░░▒░`
::░▒░░░░▀▓▓▓▓╙░░░░▒╢╢▒▓▓▓▓▓▓▄░╙▓▓▓▒▒▓▓▒▒▒▒▒▒╢▓▓▒░░░▒░░░╜╜▒@▒▒▒▒░▒░░▒▒▒▒░'` ░▒░▒▒`
::░░░░░░░░░░░░░░░░░▒▒▒▒░░╢▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▄▓▓▓▓▌░░░▄▓▓▓▓▓▓▄▄▒▒▒▒░░░░░░░▒▒░`░
::░░░░░░░░▒▒▒░░░░░▒▒▒▒▒µg▒░▒╫▓▓▓▓▒▒▒▒▒░░░░░░░░░▒▒▓▓▓▓▓██████▓▓▓▓▒▒╜╢▒▒░░'░░░░▒▒░¡▒
::░░░░░░░▒▒▒▒░░'└╙░░▒▒░╙╙▒▒▒╣╣▓▓▒░░░▒░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▒░░░▒░░╙▒▒░░░░░▒▒░`░░
::░░░¡¡░░▒▒▒▒▒▒▒▓▓▓▓▓▓▓@▓▓▓▓▓▓▒▒░░░░░░└░░,:░░░░░░░▒▓▓▓▓▓▓▓▄▄▄▄░░░░░░░░╙▒`,░░░░`¡▒░
::░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▀▀▓▓▓▓▓▓▓▓▓▓▒░` '`:.' ` '^=``'░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓@░░.@▒▒░░ ░░░
:: ░▒▒▒▒▒▒▒▒░░░░░▄▓██▓▓▓▓▓▀▀▀░▒@╣@╖╖           ,¿▒╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▒▒▒▒▒`:░░
::¡└░░▒▒▒▒▒░░▄▓▓▓▓▓▓▓▓▓▄φ@▓▓▓▓▓▓▓▓▓░░╥@@╖╓p@g╖╫▓▓▓▓▓▓▓▓▓▓▓▄▒▒▒▓▓▓╨╣╣╣▒▒╫▒║▒▒░░░▒▒▒
::▒,░░░░░░░░░╜▀▀▀▀▀▀▒▒╢▒╣▒▒░░▄████▒▓▓▓▓╣▓▓╣▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▒▒▒░░░░╫░░▒▒`░▒▒▒▒
::▒░░░░░░░` ,¡░`┌░░╫╢@▓▓▓▓▓▒█████▓▓▓▓▓░]▓██▓▒█▓▓▓░▀█▓▓▓▓██▓░▀▀▀▓▓▓▓▀╜░ ░░░░░¡░░░░▒
::▒░░░░░░░¡¡`¡¡¡╥╣╫╣▒╜╜▒▒╜╙▓█▓██▓▓▓▓▓░░▐▓██▓▌▐█▓▓▓▒▒░▀▓▓▓▓▓█▄░░░░░░░░░ ░░░░ `░░░ ¡
::▒▒▒`░▒░░░¡░░░╜╙░░░▒r ░` ░▀▀▀╫▓▓▓▓▒░░░▐▓█▓▓▓,▓█▌▓▓░░░░░░╢▓▓▓▒▒▒▒▒░░░░,░░░░`░░░` ░
::░░▒░░░░░¡└░░░ ░░╫▒▒ :░ :░░░╫▓▓▓▓░▒▒▒▒▒▓██▓▓░░▀▒╫▓░░░░░¡░╟▓▓▌░░▒▒▒░░▒▒▒▒▒ ,▒░░ ,░
::░░░░░░░░░░░░ ¡¡░░░░ ░  ░░░░╫╫▒░░░▒▒▒▒▒╬███▓▒░░░░▓▓░░░░░░░░▓▓▒▒░░░░░╢╢▒╣  ░░░░ ░░
::░░░░░░░░░░░░░░░░▒▒` ▒░'░░░▒▒▒▒▒░░░░▒▒▒░░▀╢▓▌▒▒▒░░░░░░░░▒▒▒░░░░░░░░░░╢▒`,░░░░░░░░
::░░░▒▒▒▒▒▒▒▒▒▒░░▒▒░ ;░`'░▒▒▒░░░░░░▒▒▒▒░``'╟▓▓▒▒░░░▒░▒▒▒▒▒░░░╢▒▒▒▒▒░░`└`└░░░▒▒░▒░░
::░░░░` `└░░░░░░░▒░` ░░  ░░░░░░░░░░░░░░░░`'¡░¡░░▒░░,,░▒▒░░░░░░░▒▒▒▒▒▒░  ¡m░░░░▒▒▒▒


::https://stackoverflow.com/questions/2048509/how-to-echo-with-different-colors-in-the-windows-command-line