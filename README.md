# flask-api

## How To

Clone the repository:

```
https://github.com/muhammadhanif/flask-api.git
```

Change branch:

```
cd flask-api
```

```
git checkout flask-api-sqlite
```

Install library:

```
pip3 install -r requirements.txt
```

Create Database:

```
python3 app.py create_db
```

Seed Database:

```
python3 app.py seed_db
```

Run App:

```
python3 app.py
```

### API

| HOW              | METHOD | URL            | Example                                                                                                               |
| ---------------- | ------ | -------------- | --------------------------------------------------------------------------------------------------------------------- |
| Reads all fruits | GET    | /fruits        | `curl http://127.0.0.1:5000/fruits -X GET -i`                                                                         |
| Read a fruit     | GET    | /fruits/`<id>` | `curl http://127.0.0.1:5000/fruits/1 -X GET -i`                                                                       |
| Create a fruit   | POST   | /fruits        | `curl http://127.0.0.1:5000/fruits -X POST -d name="apple" -d description="apple lorem ipsum dolor sit amet" -i`      |
| Update a fruit   | PUT    | /fruits/`<id>` | `curl http://127.0.0.1:5000/fruits/1 -X PUT -d name="Avocado" -d description="Avocado lorem ipsum dolor sit amet" -i` |
| Delete a fruit   | DELETE | /fruits/`<id>` | `curl http://127.0.0.1:5000/fruits/1 -X DELETE -i`                                                                    |

## Donate

If you want to donate to this project, please contact us:

- Email: moehammadhanif@gmail.com
- Telegram: muhammadhanif/kamus-jawa
