from pathlib import Path

from src.yummy.parser import YummyParser
from src.yummy.response_parser import ResponseParser

from src.yummy.anime_metadata import AnimeMetadata

from src.yummy.dubbing_stats import DubbingStats


class YuDow:
	def __init__(
		self,
		base_rdir: Path,
		encoding: str,
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


	def load_anime(
		self,
		anime_id: int,
		metadata: bool,
	) -> None:
		self._yp.get_anime(
			anime_id=anime_id,
		)
		if metadata:
			self._load_anime_metadata()
		self._load_anime_data()


	def _load_anime_data(
		self,
	) -> None:
		# call after get anime (yp)
		self._anime_data = self._yrp.load_anime_data()


	def _load_anime_metadata(
		self,
	) -> None:
		# call after get anime (yp)
		self._anime_metadata = self._yrp.load_anime_metadata()


	def load_dubbings_stats(
		self,
		dubbing_stats: list[DubbingStats] | None = None,
	) -> list[DubbingStats]:
		# call after load_anime_data (yudow)
		if dubbing_stats is None:
			dubbing_stats = []
		for ep_data in self._anime_data:
			for dub_data in ep_data.dubbings:
				views = 0
				for player_data in dub_data.players:
					views += player_data.views
				if dub_data.name not in [dubbing.name for dubbing in dubbing_stats]:
					dubbing_stats.append(
						DubbingStats(
							name=dub_data.name,
							views=views,
							episode_list={ep_data.number: True},
						)
					)
				else:
					for dubbing in dubbing_stats:
						if dubbing.name == dub_data.name:
							dubbing.views += views
							dubbing.episode_list[ep_data.number] = True
							break
		return dubbing_stats
