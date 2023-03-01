from jose import JWTError, jwt
import datetime import datetime, timedelta

#SECRET_KEY
#Algorithm
#Expiration time

# Save them as variables

# Reference:  wwww.fastapi.tiangolo.com/tutorial/security/oauth2.jwt/?h=boy
SECRET_KEY ="long sequence number get it from reference above"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token():
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
    



