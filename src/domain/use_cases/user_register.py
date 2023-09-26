from typing import Dict
from abc import ABC, abstractmethod

class UserRegister(ABC):

    @abstractmethod
    def register(self, first_name: str, last_name: str, age: int) -> Dict: pass
