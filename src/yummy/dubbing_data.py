from dataclasses import dataclass

from src.yummy.player_data import PlayerData


@dataclass
class DubbingData:
	name: str
	players: list[PlayerData]
