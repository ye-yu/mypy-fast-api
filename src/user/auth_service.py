from passlib.hash import bcrypt


class AuthService:
    def hash_password(self, password: str) -> str:
        return bcrypt.using(rounds=13).hash(password)  # type: ignore

    def verify_password(self, password: str, hash: str) -> bool:
        return bcrypt.verify(password, hash)

    @staticmethod
    def instantiate() -> 'AuthService':
        return AuthService()
