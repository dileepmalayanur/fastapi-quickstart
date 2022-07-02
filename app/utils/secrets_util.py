import time

from argon2.exceptions import VerifyMismatchError
from jwcrypto import jwk, jwt
from argon2 import PasswordHasher

from app.utils.common_util import repeat_to_at_least_length

def generate_auth_code(payload: str, encryption_key: str) -> str:
    length_of_plain_key = int(256/8)
    if len(encryption_key) < length_of_plain_key:
        encryption_key = repeat_to_at_least_length(encryption_key, length_of_plain_key)

    if len(encryption_key) > length_of_plain_key:
        encryption_key = encryption_key[0:length_of_plain_key]

    jwk_key = jwk.JWK.from_password(encryption_key)
    jwt_valid_seconds = 3
    expiry_time = round(time.time()) + jwt_valid_seconds
    claims = {"exp": expiry_time, "sub": "FastAPI Authentication"}
    jwttoken = jwt.JWT(header={"alg": "A256KW", "enc": "A256CBC-HS512"}, claims=claims)
    jwttoken.make_encrypted_token(jwk_key)
    jwetoken = jwttoken.serialize(compact=True)
    return jwetoken

def decrypt_auth_code(encrypted_payload: str, encryption_key: str):
    length_of_plain_key = int(256/8)
    if len(encryption_key) < length_of_plain_key:
        encryption_key = repeat_to_at_least_length(encryption_key, length_of_plain_key)

    if len(encryption_key) > length_of_plain_key:
        encryption_key = encryption_key[0:length_of_plain_key]

    jwk_key = jwk.JWK.from_password(encryption_key)
    jwttoken = jwt.JWT()
    jwttoken.deserialize(encrypted_payload, jwk_key)
    return jwttoken.claims if jwttoken is not None else None

def build_password_hash(password: str):
    hasher = PasswordHasher()
    return hasher.hash(password)

def verify_password_hash(password_hash: str, password: str):
    hasher = PasswordHasher()
    try:
        hasher.verify(password_hash, password)
        verified = True
    except VerifyMismatchError:
        verified = False

    return verified
