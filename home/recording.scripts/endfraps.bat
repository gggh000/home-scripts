sleeptime=%1 %2
set /a seconds=%1% * 60
echo fraps recording at %2 will be ended in %1 minutse or in %seconds% seconds
timeout /T %seconds%
echo ending fraps recording...
autohotkey c:\scripts\%2
echo done...
