echo "Unix InstaPy Setup"
echo =============================================================================================
echo "Downloading Chrome Driver..."
export LC_ALL=C

arch=$(getconf LONG_BIT)
kernel=$(uname)
echo "Installing depedencies..."
if [ $kernel == "Darwin" ]; then
  echo "MacOS System detected"
else
  sudo apt-get update
  sudo apt-get -y upgrade
  sudo apt-get -y install unzip python3-pip python3-dev build-essential libssl-dev libffi-dev xvfb
  sudo pip3 install --upgrade pip
  export LANGUAGE=en_US.UTF-8
  export LANG=en_US.UTF-8
  export LC_ALL=en_US.UTF-8
  locale-gen en_US.UTF-8
  sudo dpkg-reconfigure locales
  sudo pip3 install --upgrade pip
  pushd ~
  pushd -0
fi
echo
pushd ../
echo "Downloading Chrome Driver..."
echo
if [ $kernel == "Darwin" ]; then
  sudo python setup.py install
else
  sudo pip install setuptools
  sudo apt-get install python-dev
  sudo pip install ./
fi
pushd -0
echo "Setup is completed."

