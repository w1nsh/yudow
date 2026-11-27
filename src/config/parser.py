from pathlib import Path
import tomllib

from src.config.main import Config
from src.config.templates import TemplatesConfig


class ConfigParser:
	def __init__(
		self,
		cdir: Path,
		odir: Path,
		encoding: str = 'utf-8',
	) -> None:
		self._cdir = cdir
		self._odir = odir
		self._encoding = encoding


	def config(
		self,
		filename: str,
	) -> Config:
		try:
			config_toml = tomllib.loads(
				(self._cdir / filename).read_text(
					encoding=self._encoding,
				)
			)
		except Exception:
			config_toml = dict()
		
		output_dir = Path(config_toml.get('output_dir', str(self._odir)))
		max_retries = config_toml.get('max_retries', 3)
		metadata = config_toml.get('metadata', True)
		templates = config_toml.get('templates', dict())
		templates_episodes = templates.get('episodes', 'ep{episode_number}')
		templates_metadata = templates.get('metadata', '{anime_title}')
		
		return Config(
			output_dir=output_dir,
			max_retries=max_retries,
			metadata=metadata,
			templates=TemplatesConfig(
				episodes=templates_episodes,
				metadata=templates_metadata,
			),
		)
