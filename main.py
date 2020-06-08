from fastapi import FastAPI, Security
from auth0 import AuthError, get_current_user

app = FastAPI(title="API Lindo Crl",
    description="lindocrl official api crl",
    version="1.0.0",)

@app.get("/")
def health():
    return { "running": True }

@app.get("/private")
def private(user=Security(get_current_user)):
    return {"message": "You're an authorized user"}

# @app.get("/private-with-scopes")
# def privateScopes(user=Security(get_current_user, scopes["read:example"])):
#     return {"message": "You're authorized with scopes!"}

# api.lindocrl.org/cup/{year}/prediction
# endpoint to post prediction bulk

# api.lindocrl.org/cup/{year}/prediction
# endpoint to update prediction bulk

