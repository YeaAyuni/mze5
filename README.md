# mze5
- install requirements via 
  ```
  pip install -r requirements.txt
  ```
- setup ngrok auth token
  [(*get your token here*)](https://dashboard.ngrok.com/get-started/your-authtoken), then run
  ```
  ./ngrok config add-authtoken REPLACE_HERE_WITH_YOUR_TOKEN
  ```
- run server.py
  ```
  python server.py
  ```
- run ngrok
  ```
  ./ngrok http 5000
  ```
