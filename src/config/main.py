from dataclasses import dataclass
from pathlib import Path

from src.config.templates import TemplatesConfig

@dataclass
class Config:
	output_dir: Path
	max_retries: int
	metadata: bool
	templates: TemplatesConfig
