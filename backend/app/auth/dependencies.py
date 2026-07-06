from fastapi import Depends, HTTPException, status
from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials,
)
from jose import jwt, JWTError
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

print("DEP SECRET:", SECRET_KEY)
print("DEP ALGORITHM:", ALGORITHM)

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    print("\n===== GET_CURRENT_USER CALLED =====")

    token = credentials.credentials

    print("TOKEN RECEIVED:")
    print(token)

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        print("\nPAYLOAD:")
        print(payload)

        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

        print("CURRENT USER:", email)

        return email

    except JWTError as e:
        print("\n===== JWT ERROR =====")
        print(type(e))
        print(str(e))
        print("=====================")

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    except Exception as e:
        print("\n===== GENERAL ERROR =====")
        print(type(e))
        print(str(e))
        print("=========================")

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )