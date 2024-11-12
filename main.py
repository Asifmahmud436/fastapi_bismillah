from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()


# path operator
@app.get('/blog') # path
# path operation function
def index(limit=10,published:bool=True,sort : Optional[str]=None):
    if published:
        return {'data':f'{limit} published blogs from the database'}
    else:
        return {'data':f'{limit} blogs from the database'}

# we can use curly braces for dynamic use
@app.get('/blog/{id}')
def show(id:int):
    return {'data': id }


# creating model
class Blog(BaseModel):
    title : str
    body : str
    published_at : Optional[bool]

@app.post('/blog')
def create_blog(blog:Blog):
    return {'data':f'A blog is created with the title {blog.title}'}