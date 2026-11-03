from pathlib import Path
from typing import Any
import json

from src.yummy.episode_data import EpisodeData
from src.yummy.dubbing_data import DubbingData
from src.yummy.player_data import PlayerData
# from src.yummy.anime_metadata import AnimeMetadata


class ResponseParser:
	def __init__(
		self,
		encoding: str,
		base_rdir: Path,
	) -> None:
		self._encoding = encoding
		self._base_rdir = base_rdir


	def get_animes(
		self,
	) -> list[tuple[str, int]]:
		animes = []
		json_data = self._read_json(
			file=self._base_rdir / 'search.json',
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
			file=self._base_rdir / 'anime.json',
		)
		anime_data: list[EpisodeData] = []

		for video in json_data['response']['videos']:
			number = video['number']
			dubbing = video['data']['dubbing']
			player = video['data']['player']
			views = video['views'] # views specific pair player and dubbing
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


	# def load_anime_metadata(
	# 	self,
	# ) -> AnimeMetadata:
	# 	json_data = self._read_json(
	# 		file=self._base_rdir / 'anime.json',
	# 	)


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
	