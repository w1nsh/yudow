from pathlib import Path

from src.yummy.parser import YummyParser
from src.yummy.response_parser import ResponseParser

from src.yummy.episode_data import EpisodeData
from src.yummy.dubbing_stats import DubbingStats


class YuDow:
	def __init__(
		self,
		base_rdir: Path,
		encoding: str = 'utf-8',
	) -> None:
		self._base_rdir = base_rdir
		self._encoding = encoding
		self._yp = YummyParser(
			encoding=self._encoding,
			base_rdir=self._base_rdir,
		)
		self._yrp = ResponseParser(
			encoding=self._encoding,
			base_rdir=self._base_rdir,
		)


	def search_anime(
		self,
		query: str,
		limit: int = 1,
	) -> list[tuple[str, int]]:
		self._yp.search(
			query=query,
			limit=limit,
		)
		return self._yrp.get_animes()


	def load_anime_data(
		self,
		anime_id: int,
		need_videos: bool,
	) -> None:
		self._yp.get_anime(
			anime_id=anime_id,
			need_videos=need_videos,
		)
		self._anime_data = self._yrp.load_anime_data()


	def load_dubbings_stats(
		self,
	) -> list[DubbingStats]:
		...
