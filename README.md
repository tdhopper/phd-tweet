### Run instructions

On this machine:

```
scp * root@45.55.151.24:~/phd
scp .env root@45.55.151.24:~/phd
```

On the remote machine in tmux:

```
cd phd
conda create -n phd python=2 pip
source activate phd
pip install -r requirements.pip
source activate .env
python tweet.py
```

### `.env` File

```
export PHD_CONSUMER_KEY=
export PHD_CONSUMER_SECRET=
export PHD_TOKEN=
export PHD_TOKEN_SECRET=
```
