Run instructions:

```
scp * root@45.55.151.24:~/phd
scp .env root@45.55.151.24:~/phd
conda create -n phd python=2 pip
source activate phd
pip install -r requirements.txt
source activate .env
python tweet.py
```