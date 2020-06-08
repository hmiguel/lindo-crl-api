import json

from fastapi import Depends
from fastapi.security import OAuth2AuthorizationCodeBearer, SecurityScopes
from jose import jwt
from six.moves.urllib.request import urlopen

AUTH0_DOMAIN = "lindocrl.eu.auth0.com"
API_AUDIENCE = "api.lindocrl.org"
ALGORITHMS = ["RS256"]

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

# Define a Authorization scheme specific to our Auth0 config
auth0_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=AUTH0_DOMAIN, tokenUrl=API_AUDIENCE
)

async def get_current_user(security_scopes: SecurityScopes, token: str = Depends(auth0_scheme)):
    # This down to `END` comment is from https://auth0.com/docs/quickstart/backend/python/01-authorization#create-the-jwt-validation-decorator
    jsonurl = urlopen("https://" + AUTH0_DOMAIN + "/.well-known/jwks.json")
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)

    rsa_key = {}
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"],
            }

    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer=f"https://{AUTH0_DOMAIN}/",
            )
        except jwt.ExpiredSignatureError:
            raise AuthError(
                {"code": "token_expired", "description": "token is expired"}, 401
            )
        except jwt.JWTClaimsError:
            raise AuthError(
                {
                    "code": "invalid_claims",
                    "description": "incorrect claims,"
                    "please check the audience and issuer",
                },
                401,
            )
        except Exception:
            raise AuthError(
                {
                    "code": "invalid_header",
                    "description": "Unable to parse authentication" " token.",
                },
                401,
            )
       # END from Auth0

        # token.scope is represented as a string of scopes space seperated
        token_scopes = payload.get("scope", "").split()

        # Check that we all scopes are present
        for scope in security_scopes.scopes:
            if scope not in token_scopes:
                raise AuthError(
                    {
                        "code": "Unauthorized",
                        "description": f"You don't have access to this resource. `{' '.join(security_scopes.scopes)}` scopes required",
                    },
                    403,
                )

        return payload