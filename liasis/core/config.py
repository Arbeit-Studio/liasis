from liasis.core import DataStructure
from dataclasses import dataclass


@dataclass
class AppConfig(DataStructure):
    """
    A Data Structure to describe an Application Configurations.

    Each application should declare a DefaultConfig class extending this one
    and describe it's own attributes needed for configuration.
    """
    pass