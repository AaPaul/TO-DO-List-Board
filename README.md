# TO-DO-List-Board

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FAaPaul%2FTO-DO-List-Board&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)


A task management web application to record daily tasks, including User Registration, Login, Search and full Create Read Update and DELETE functionality. Login required. Each user can only access their own tasks.

## Demo
This demo is depolyed on [Heroku](https://www.heroku.com/).

![](./pictures/todo_screenshot.png)

You can also visit the **[DEMO](https://to-do-list-board.herokuapp.com/login/)** here.

Default account shows below.

Username: paul \
Password: paul123#


## Environment settings

- Python: 3.8
- Anaconda: 4.10.3
- Django: 3.0.3
- PostgreSQL: 12.9


Download requirment packages with anaconda.
```
conda env create -f todo.yaml
```

Download requirment packages with pip.
```
pip install -r requirements.txt
```


After installing all required packages, we need to run the command below to initial our database in the target folder.

```
python manage.py migrate
```

Then you can run it by
```
python manage.py runserver
```

It will be deployed at `localhost:8000` as default.


