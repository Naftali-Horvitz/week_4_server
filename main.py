import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from utils.encrypt import caesar_encrypt, fence_encrypt, fence_decrypt, write_endpoint
app= FastAPI()

path_names = "data/names.txt"

# mode = "encrypt" | "decrypt"

class DataCaesar(BaseModel):
    text: str
    offset: int
    mode: str

class DataFence(BaseModel):
    text: str
    


@app.get("/test")
def test():
    return { "msg": "hi from test"}
    
@app.get("/test/{name}")
def test_username(name: str):
    with open(path_names, 'a') as f:
        f.write(name + "\n")
    return { "msg":"saved user",}

@app.post("/caesar")
def caesar_cipher(data: DataCaesar):
    result =caesar_encrypt(data.text, data.offset, data.mode)
    return {f"{data.mode}ed_text:": result}

@app.get("/fence/encrypt")
def caesar_cipher(text: str):
    result = fence_encrypt(text)
    return {"encrypted_text": result}

@app.post("/fence/decrypt")
def caesar_cipher(text: DataFence):
    result = fence_decrypt(text.text)
    return {"decrypted_text": result}
    








if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8012,
        reload=True
    )