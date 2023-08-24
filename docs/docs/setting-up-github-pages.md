Testing

Pre-req

mkdocs

https://www.mkdocs.org/getting-started/



ModuleNotFoundError: No module named 'apt_pkg'

sudo apt remove python3-apt
sudo apt autoremove
sudo apt autoclean
sudo apt install python3-apt


Install Make

```
sudo apt update && sudo apt upgrade -y
sudo apt install -y make
```

Install Poetry

```
curl -sSL https://install.python-poetry.org | python3 -
export PATH="/home/curtis/.local/bin:$PATH"
poetry --version
```


Make lint

```
sudo chmod a+x markdown-lint.sh
```


///

sudo apt-get install python-pip 
sudo apt-get install python3-pip
pip3 install mkdocs
Create branch \gh-pages\




pip install pymdown-extensions
pip install mkdocs-awesome-pages-plugin
pip install mkdocs-macros-plugin