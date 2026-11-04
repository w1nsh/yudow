from dataclasses import dataclass

from src.config.players import Players
from src.config.dubbings import Dubbings

@dataclass
class PlayConfig:
	players: list[Players]
	dubs: list[Dubbings]
