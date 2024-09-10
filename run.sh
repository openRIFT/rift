# Install packages from pip
pip3 install colorama
pip3 install rich
pip3 install requests

echo Please provide your password, as RIFT will be install to /usr/local/bin/

# Remove old version of RIFT
sudo rm /usr/local/bin/rift

# Move rift to /usr/local/bin
sudo cp rift.py /usr/local/bin/rift
sudo chmod +x /usr/local/bin/rift

# Move Locales and other info
mkdir .rift
cp lang .rift -r
cp .rift/ ~/ -r
rm .rift -r

# Run
rift