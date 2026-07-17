from dotenv import load_dotenv
import os

load_dotenv()



def get_env(key: str | int) -> str:
    # os.getenv expects a string key; ensure the key is stringified
    value = os.getenv(str(key))

    if value is None:
        raise ValueError(f"{key} is not set.")

    return value


DATABASE_URL = get_env("DATABASE_URL")
JWT_SECRET = get_env("JWT_SECRET")
ACCESS_TOKEN_EXPIRES_IN = get_env("ACCESS_TOKEN_EXPIRES_IN")
REFRESH_TOKEN_EXPIRES_IN = get_env("REFRESH_TOKEN_EXPIRES_IN")
JWT_ALGORITHM = get_env("JWT_ALGORITHM")


