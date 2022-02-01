from os import stat
from typing import Optional
from urllib import response
from fastapi.params import Body
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange
import psycopg2

app = FastAPI()

try:
  conn = psycopg2.connect(host='localhost', database='', user='', password='')
  print('connection succeded')
except Exception as error:
  print('connection failed')
  print(error)


class Post(BaseModel):
  title: str
  content: str
  published: bool = True

# my_posts = [{"id":1, "title":"title1", "content":"content1", "published":True, "rating":15}]

def find_post_by_id(id):
  for p in my_posts:
    if p['id'] == id:
      return p

def find_index_post(id):
  for i, p in enumerate(my_posts):
    if p['id'] == id:
      return i


@app.get("/")
def root():
  return {"message":"hello folks"}

@app.get("/posts")
def posts():
  return{"data":my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
  post_dict = post.dict()
  post_dict['id'] = randrange(0,100)
  my_posts.append(post_dict)
  return{"data":post_dict}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
  post=find_post_by_id(id)
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")
    # response.status_code = status.HTTP_404_NOT_FOUND
    # return{"message":f"post with id {id} not found"}
  return{"data":post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
  index = find_index_post(id)
  if index == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
  my_posts.pop(index)
  return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id:int, post:Post):
  index = find_index_post(id)
  if index == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post withi id {id} was not found")
  
  post_dict = post.dict()
  post_dict['id'] = id
  my_posts[index]= post_dict
  return{'data':post_dict}
