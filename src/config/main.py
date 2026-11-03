from pathlib import Path

from src.config.templates import TemplatesConfig
from src.config.play import PlayConfig


class Config:
	output_dir: Path
	max_retries: int
	metadata: bool
	templates: TemplatesConfig
	play: PlayConfig
