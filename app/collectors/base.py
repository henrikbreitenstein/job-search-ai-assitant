from abc import ABC, abstractmethod

from app.models import JobPosting

class BaseCollector(ABC):

    @abstractmethod
    def collect(self) -> list[JobPosting]:
        pass
