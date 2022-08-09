@echo off
cd
set /P file="which file would you like to compile? "
py -m nuitka %file% --standalone --onefile --windows-icon-from-ico=icon.ico --enable-plugin=tk-inter --enable-plugin=numpy
pause