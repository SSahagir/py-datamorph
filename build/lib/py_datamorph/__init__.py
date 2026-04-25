# py-datamorph initialization
"""
py-datamorph: A professional data engineering toolkit.
Developed by: Sk Sahagir (Roll: 11000224051)
"""

# Importing core classes so users can access them easily
# Instead of: from py_datamorph.converter import DataMorphConverter
# Users can do: from py_datamorph import DataMorphConverter

from .converter import DataMorphConverter
from .cleaner import DataMorphCleaner

# Define what is accessible when using 'from py_datamorph import *'
__all__ = [
    'DataMorphConverter',
    'DataMorphCleaner'
]

# Metadata
__version__ = "1.0.0"
__author__ = "Sk Sahagir"