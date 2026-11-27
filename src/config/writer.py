from pathlib import Path

from src.config.main import Config


class ConfigWriter:
	def __init__(
		self,
		cdir: Path,
		encoding: str = 'utf-8',
	) -> None:
		self._cdir = cdir
		self._encoding = encoding


	def write(
		self,
		config: Config,
		filename: str,
	) -> None:
		config_toml = (
			f'output_dir = \"{config.output_dir}\"\n'
			f'max_retries = {config.max_retries}\n'
			f'metadata = {config.metadata}\n\n'
			'[templates]'
			f'episodes = \"{config.templates.episodes}\"\n'
			f'metadata = \"{config.templates.metadata}\"\n'
		)
		(self._cdir / filename).write_text(
			data=config_toml,
			encoding=self._encoding,
			)
