from fastapi import FastApi

app = FastApi()

@app.post("/user")
def register(user):
    return {"name" : user.name, "email":user.email}