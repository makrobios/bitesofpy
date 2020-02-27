import base64
from cryptography.fernet import Fernet  # type: ignore
from cryptography.hazmat.backends import default_backend  # type: ignore
from cryptography.hazmat.primitives import hashes  # type: ignore
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC  # type: ignore
from os import urandom
from typing import ByteString, Tuple, Optional


class ClamyFernet:
    """Fernet implementation by clamytoe

    Takes a bytestring as a password and derives a Fernet
    key from it. If a key is provided, that key will be used.

    :param password: ByteString of the password to use
    :param key: ByteString of the key to use, else defaults to None

    Other class variables that you should implement that are hard set:

    salt, algorithm, length, iterations, backend, and generate a base64
    urlsafe_b64encoded key using self.clf().
    """
    
    def __new__(cls, password=b"pybites", key=None):
        if password:
            cls.password = password
        if key:
            cls.key = key
        cls.salt = urandom(16)
        cls.algorithm=hashes.SHA256()
        cls.length=32
        cls.iterations=100000
        cls.backend = default_backend()
        instance = super(ClamyFernet, cls).__new__(cls)
        instance.key = cls.key
        instance.password = password
        return instance

    @property
    def kdf(self):
        """Derives the key from the password
        Uses PBKDF2HMAC to generate a secure key. This is where you will
        use the salt, algorithm, length, iterations, and backend variables.
        """
        self._kdf = PBKDF2HMAC(
            algorithm=ClamyFernet.algorithm,
            length=ClamyFernet.length,
            salt=ClamyFernet.salt,
            iterations=ClamyFernet.iterations,
            backend=ClamyFernet.backend)
        return self._kdf
        

    @property
    def clf(self):
        """Generates a Fernet object

        Key that is derived from cryptogrophy's fermet.
        """
        self.fernet = Fernet(self.key)   
        return self.fernet
         

    def encrypt(self, message: str) -> ByteString:
        """Encrypts the message passed to it"""
        self.message = message
        self.fernet = self.clf
        self.token = self.fernet.encrypt(bytes(self.message, 'utf-8'))
        return self.token

    def decrypt(self, token: ByteString) -> str:
        """Decrypts the encrypted message passed to it"""
        self.dec = self.fernet.decrypt(token)
        return self.dec.decode()