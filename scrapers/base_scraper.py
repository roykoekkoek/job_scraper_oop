"""
Deze code implemteert een base class die zal dienen voor verschillende Python webscrapers

"""

from abc import ABC, abstractmethod
from typing import Dict

class Scraper(ABC):
    """Base class voor scraper"""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_specific_job_listing(self) -> Dict:
        pass

    @abstractmethod
    def get_list_jobs(self, query) -> Dict:
        pass
    


