from pathlib import Path
from typing import Any
import json

from src.yummy.episode_data import EpisodeData
from src.yummy.dubbing_data import DubbingData
from src.yummy.player_data import PlayerData

from src.yummy.anime_metadata import AnimeMetadata
from src.yummy.season_metadata import SeasonMetadata


class ResponseParser:
	def __init__(
		self,
		encoding: str,
		rdir: Path,
	) -> None:
		self._encoding = encoding
		self._rdir = rdir


	def get_animes(
		self,
	) -> list[tuple[str, int]]:
		animes = []
		json_data = self._read_json(
			file=self._rdir / 'search.json',
		)
		for anime in json_data['response']:
			animes.append(
				(
					anime['title'],
					anime['anime_id'],
				)
			)
		return animes


	def load_anime_data(
		self,
	) -> list[EpisodeData]:
		json_data = self._read_json(
			file=self._rdir / 'anime.json',
		)
		anime_data: list[EpisodeData] = []

		for video in json_data['response']['videos']:
			number = video['number']
			dubbing = video['data']['dubbing']
			player = video['data']['player']
			views = video['views']
			player_url = video['iframe_url']

			for ep_data in anime_data:
				if ep_data.number == number:
					ep_player = PlayerData(
						name=player,
						url=player_url,
						views=views,
					)

					for dub_data in ep_data.dubbings:
						if dub_data.name == dubbing:
							dub_data.players.append(ep_player)
							break
					else:
						ep_dub = DubbingData(
							name=dubbing,
							players=[ep_player,],
						)
						ep_data.dubbings.append(ep_dub)

					break
			else:
				ep_player = PlayerData(
					name=player,
					url=player_url,
					views=views,
				)
				ep_dub = DubbingData(
					name=dubbing,
					players=[ep_player,],
				)
				ep = EpisodeData(
					number=number,
					dubbings=[ep_dub,],
				)
				anime_data.append(ep)

		return anime_data


	def load_anime_metadata(
		self,
	) -> AnimeMetadata:
		json_data = self._read_json(
			file=self._rdir / 'anime.json',
		)['response']
		title = json_data['title']
		anime_id = json_data['anime_id']
		original = json_data['original']
		other_titles = json_data['other_titles']
		description = json_data['description']
		anime_status = json_data['anime_status']['title']
		duration = json_data['duration']
		type = json_data['type']['name']
		views = json_data['views']
		year = json_data['year']
		year_season = json_data['season']
		min_age = json_data['min_age']['title_long']
		poster_url = json_data['poster']['fullsize']

		genres = []
		for genre in json_data['genres']:
			genres.append(genre['title'])

		anime_seasons = []
		for anime_season in json_data['viewing_order']:
			anime_seasons.append(
				SeasonMetadata(
					title=anime_season['title'],
					anime_season=anime_season['data']['index'],
					anime_id=anime_season['anime_id'],
					description=anime_season['description'],
					type=anime_season['type']['name'],
					info=anime_season['data']['text'],
					year=anime_season['year'],
					anime_status=anime_season['anime_status']['title'],
					poster_url=anime_season['poster']['fullsize'],
				)
			)

		return AnimeMetadata(
			title=title,
			other_titles=other_titles,
			original=original,
			description=description,
			anime_id=anime_id,
			anime_status=anime_status,
			duration=duration,
			genres=genres,
			type=type,
			views=views,
			year=year,
			year_season=year_season,
			min_age=min_age,
			poster_url=poster_url,
			anime_seasons=anime_seasons,
		)


	def _read_json(
		self,
		file: Path,
	) -> dict[str, Any]:
		"""
		Reads json file and returns him data.

		Args:
			file (Path): Path to the json file.

		Returns:
			dict[str, Any]: Json data.
		"""
		return json.loads(file.read_text(self._encoding))
	