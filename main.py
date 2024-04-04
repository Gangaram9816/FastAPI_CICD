from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello FastAPI App CICD TEST"}

if __name__=='__main__':
    uvicorn.run(app)
