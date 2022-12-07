import pylatex.utils

from .documents import ResumeDocument

# escaping hyphens prevents latex from substituing fancy hyphens
pylatex.utils._latex_special_chars.pop("-")
