from dataclasses import dataclass

from src.yummy.dubbing_data import DubbingData


@dataclass
class EpisodeData:
	number: str
	dubbings: list[DubbingData]
