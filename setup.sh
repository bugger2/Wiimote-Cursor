sudo apt-get update
sudo apt-get install --no-install-recommends bluetooth -y
sudo apt-get install python-cwiid
sudo apt-get install python3-matplotlib
python -m pip install -U pip
python -m pip install -U matplotlib
echo 'Please hold the 1 and 2 buttons on your Wiimote now.'
python CursorFunctions.py
