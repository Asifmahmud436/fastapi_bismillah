from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'Asif'}}

@app.get('/about')
def about():
    return {'data':'This is about page.'}