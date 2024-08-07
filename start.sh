if [ -z $SOURCE_CODE ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Apurv-Arya/Auto-Forward-Bot-V2
else
  echo "Cloning Custom Repo from $SOURCE_CODE "
  git clone $SOURCE_CODE /Auto-Forward-Bot-V2
fi
cd /Auto-Forward-Bot-V2
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
