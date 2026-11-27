from dataclasses import dataclass


@dataclass
class SeasonMetadata:
	title: str
	anime_season: int
	anime_id: int
	description: str
	type: str
	info: str
	year: int
	anime_status: str
	poster_url: str
