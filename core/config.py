# core/config.py
"""
Configuration file for the Bodega beat generator.

This module defines project-wide constants, primarily filesystem paths.
All paths are built relative to the project root using `pathlib`, ensuring
the application works correctly regardless of the current working directory.
"""

from pathlib import Path



# Base directory of the project (where this file is located, then up two level)
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directory
DATA_DIR = BASE_DIR / "data"

# Path to chord progressions JSON file
CHORD_PROGRESSIONS_PATH = DATA_DIR / "chord_progressions.json"