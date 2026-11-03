from pathlib import Path

from src.config.players import Players
from src.config.dubbings import Dubbings


class PlayConfig:
	players: list[Players]
	dubs: list[Dubbings]
