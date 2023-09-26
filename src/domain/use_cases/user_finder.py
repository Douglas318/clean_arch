from typing import Dict
from abc import ABC, abstractmethod

class UserFinder(ABC):

    @abstractmethod
    def find(self, first_name: str) -> Dict: pass
