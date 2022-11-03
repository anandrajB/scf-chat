# CHAT APPLICATION 

### A Pluggable chat application

# BUILD WITH FLASK==2.2.2 and MONGODB==5.0


## Authors

- [@Mohamed-Sheik-Ali](https://github.com/Mohamed-Sheik-Ali)
- [@anandrajB](https://github.com/anandrajB)


## INSTALLATION AND RUNNING

1. pip install -r requirements.txt
2. gunicorn --bind 0.0.0.0:5000 wsgi:app
3. flask run


## DATABASE

1. TESTING :  atlas
2. PRODUCTION : DIGITALOCEAN MONGODB _V5


## API Reference
#### Post a configuration - Admin only

```http
  POST /config/create_config/
```

| Parameter | Type     | Description                |  Request         |
| :-------- | :------- | :------------------------- |:-----------------|
| `xpath` | `list` | **Required**.  list of Xpaths |  json  |
| `url` | `URL field` | **Required**. domain URL|  json  |
| `label` | `URL field` | **Required**. label for the xpath|  json  |


#### Get a configuration

```http
  GET /config/get_config/
```

| Parameter | Type     | Description                |  Request          |
| :-------- | :------- | :------------------------- |:-----------------|
| `domain_url` | `URL field` | **Required**. domain URL|  Query params  |


#### Post a conversation


``` 
    socket.io 
    event => "send_message"
```

| Parameter | Type     | Description                |  Request   |
| :-------- | :------- | :------------------------- |:------------|
| `config_id` | `string` | **Required**. Config reference |  json  |
| `sender` | `email` | **Required**. User |  json  |
| `members` | `list` | **Required**. members of a particular chat|  json  |
| `party` | `string` | **Required**. party name the members in the chat|  json  |
| `text` | `string` | **Required**. Message to be sent|  json  |
| `subject` | `string` | **Required**. Details processed from Xpath|  json  |


#### Get conversation between users

```http
     GET /conv/msgs/
```

| Parameter | Type     | Description                |  Request          |
| :-------- | :------- | :------------------------- |:-----------------|
| `members` | `list` | **Required**. members of the chat |  Query Params  |
| `config_id`| `string` | **Required**. Config Reference  | Query Params |


#### Get conversation of the currently logged in user

```http
     GET /conv/convo_list/
```

| Parameter | Type     | Description                |  Request          |
| :-------- | :------- | :------------------------- |:-----------------|
| `user` | `email` | **Required**. currently logged in user |  Query Params  |
| `config_id`| `string` | **Required**. Config Reference  | Query Params |

#### Get the count of unread messages received by the user

```http
     GET /count/count_msgs/
```

| Parameter | Type     | Description                |  Request          |
| :-------- | :------- | :------------------------- |:-----------------|
| `config_id`| `string` | **Required**. Config Reference  | Query Params |


#### Update the is_read status of the messages

```http
     GET /count/update_read/
```

| Parameter | Type     | Description                |  Request          |
| :-------- | :------- | :------------------------- |:-----------------|
| `config_id`| `string` | **Required**. Config Reference  | json |
| `members` | `list` | **Required**. members of the chat |  json  |
| `is_read` | `boolean` | **Required**. read status |  json |
