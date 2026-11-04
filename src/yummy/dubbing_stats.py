from dataclasses import dataclass


@dataclass
class DubbingStats:
	name: str
	views: int
	episode_list: dict[str, bool]
