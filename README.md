Run instructions:


On this machine:
```
scp * root@45.55.151.24:~/newton
scp .env root@45.55.151.24:~/newton
```

On the remote machine in tmux:

```
mkdir newton; cd newton
conda create -n newton python=2 pip
source activate newton
pip install -r requirements.php
source activate .env
python tweet.py
```