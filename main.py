#!/usr/bin/env python
# coding: utf-8

# In[1]:


import uvicorn
from fastapi import FastAPI


# In[2]:


app = FastAPI()


# In[3]:


@app.get('/')
def index():
    return{message: "Flower prediction app"}


# In[16]:


@app.get('/Welcome')
def get_name(name: str):
    return{'Welcome to Ellas Flower prediction app': f'{name}'}


# In[18]:


#run api with uvicorn
if __name__ == 'main':
    uvicorn.run(app, host = '127.0.0.1', port = 8000)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


# In[ ]:




