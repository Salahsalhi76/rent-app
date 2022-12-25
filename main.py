from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# @app.get('/')
# def ade():
#     return 'azertyui'

# @app.get('/dalas')
# def dalas(limit=9, published:bool = True, sort: Optional[str] = None):
#     if published:
#         return f'{limit} published blogs from db'
#     else:
#         return f'{limit} bloogs from db' 



# class Blog(BaseModel):
#     title: str
#     body: str
#     published: Optional[bool]


# @app.post('/blog')
# def create_blog(request: Blog):
#     return {'data' : f'blog succesfully created with {request.title} title'}


# # if __name__ == '__dalas__':
# #     uvicorn.run(app, host='127.0.0.1', port=9000 )