{
  "config_id": "6333dfb904e7224d084ab575",
  "members": [
    "elon@gmail.com",
    "nani@gmail.com"
  ],
  "party": "VARSH TECH PALLADAM",
  "subject": [
    {
      "label": "Limit Amount",
      "xpath": "21011"
    },
    {
      "label": "Maximum Invoice Amount",
      "xpath": "234"
    }
  ],
  "message": [
    {
      "text": "Hi every o , am elo maa ,  money !!!",
      "sender": "buyer@gmail.com",
      "is_read": true
    }
  ]
}


gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 app:app

gunicorn --worker-class eventlet -w 1 app:app