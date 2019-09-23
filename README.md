# Install dependency

```
sudo apt-get install -y libigraph0-dev libcairo2-dev libjpeg-dev libgif-dev
```

# Install pip package

```
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# How to merge your branch to master
```
git checkout your-branch
git merge master
git checkout master
git merge your-branch
```

# How to create new branch
```
git checkout branch-you-want-to-work-from
git checkout -b your-branch
```
