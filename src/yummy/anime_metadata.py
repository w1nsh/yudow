from dataclasses import dataclass

from src.yummy.season_metadata import SeasonMetadata


@dataclass
class AnimeMetadata:
	title: str
	anime_id: int
	other_titles: list[str]
	original: str
	description: str
	anime_status: str
	duration: int
	genres: list[str]
	type: str
	views: int
	year: int
	year_season: int
	min_age: str
	poster_url: str
	anime_seasons: list[SeasonMetadata]
