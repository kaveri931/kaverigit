import random
from config import app
 

@app.get('/message')
def greetnow():
    return "This is my task"


@app.get('/number')
def fun():
    num = random.randit(0,100)
    return f"{num} is returned"     