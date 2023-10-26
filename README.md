
## Installation

To install this project locally, follow the below instructions

- Clone this repo
- [Install Docker](https://docs.docker.com/engine/install/)
- Install flask

```bash
  pip3 install flask
```

- Install flask_sqlalchemy
```bash
  pip3 install flask_sqlalchemy
```

- Start the kong server
```bash
  docker compose up
```

- On a new terminal window, start the flask server
```bash
  flask run
```


## Endpoints

* Home route for asset upload [http://localhost:8000/](http://localhost:8000/) - Will return the asset name and the CDN url of the asset on successful upload.
* To access CDN url for an asset [http://localhost:8000/url/<asset_name>] 
    * **Example** - [http://localhost:8000/url/apple.jpeg](http://localhost:8000/url/apple.jpeg)

* CDN url endpoint [http://localhost:8000/download/<upload_id>]
    * **Example** - [http://localhost:8000/download/1](http://localhost:8000/download/1)
