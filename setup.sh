echo Installing tk...
sudo apt install python3-tk

echo Installing pillow...
sudo pip install pillow

echo Installing dos2unix...
sudo apt install dos2unix

echo Marking as executable and converting
chmod +x ./ArcadeMenu.pyw

dos2unix ./ArcadeMenu.pyw

