from fastapi import FastAPI
from fastapi import HTTPException
from Models._all_models import *


host = "127.0.0.1"
port = 8000

app = FastAPI()

@app.get('/')
async def root():
    return {'first api':'My first Api'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app:app', host=host, port=port, reload=True)