from dataclasses import dataclass


@dataclass
class AnimeMetadata:
	title: str
	description: str
	anime_id: int
	season: int
	anime_status: str
	duration: int
	genres: list[str]
	type_name: str
	views: int
	year: int
	min_age: str
	poster_url: str
