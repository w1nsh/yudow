from pathlib import Path

from src.config.parser import ConfigParser
from src.config.writer import ConfigWriter

from src.yummy.parser import YummyParser
from src.yummy.response.parser import ResponseParser
from src.yummy.response.filenames import ReponseFilenames
from src.yummy.response.lifetimer import ResponseLifetimer

from src.yummy.dubbing_stats import DubbingStats


class YuDow:
	BASE_RDIR_ENDPOINT = 'responses'
	BASE_CDIR_ENDPOINT = 'config'
	BASE_ODIR_ENDPOINT = 'downloaded'
	CONFIG_FILENAME = 'config.toml'

	def __init__(
		self,
		base_dir: Path,
		encoding: str,
	) -> None:
		self._rdir = base_dir / self.BASE_RDIR_ENDPOINT
		self._cdir = base_dir / self.BASE_CDIR_ENDPOINT
		self._odir = base_dir / self.BASE_ODIR_ENDPOINT
		self._encoding = encoding

		self._cp = ConfigParser(
			cdir=self._cdir,
			odir=self._odir,
			encoding=self._encoding,
		)
		self._cw = ConfigWriter(
			cdir=self._cdir,
			encoding=self._encoding,
		)
		self._config = self._cp.config(self.CONFIG_FILENAME)

		self._yp = YummyParser(
			encoding=self._encoding,
			rdir=self._rdir,
		)
		self._yrp = ResponseParser(
			encoding=self._encoding,
			rdir=self._rdir,
		)
		self._rl = ResponseLifetimer(
			rdir=self._rdir,
		)


	def search_anime(
		self,
		query: str,
		limit: int = 1,
	) -> list[tuple[str, int]]:
		self._yp.search(
			filename=ReponseFilenames.SEARCH,
			query=query,
			limit=limit,
		)
		return self._yrp.get_animes()


	def load_anime(
		self,
		anime_id: int,
	) -> None:
		method = ReponseFilenames.GET_ANIME
		if self._rl.timestamp_is_exists(
			filename=method,
		):
			timestamp = self._rl.load(
				filename=method,
			)
			if not self._rl.timestamp_is_valid(
				timestamp=timestamp,
			):
				self._yp.get_anime(
					filename=method,
					anime_id=anime_id,
				)
				self._rl.write(
					timestamp=self._rl.timestamp(
						filename=method,
					),
				)
		else:
			self._yp.get_anime(
				filename=method,
				anime_id=anime_id,
			)
			self._rl.write(
				timestamp=self._rl.timestamp(
					filename=method,
				),
			)
		if self._config.metadata:
			self._anime_metadata = self._yrp.load_anime_metadata()
		self._anime_data = self._yrp.load_anime_data()


	def load_dubbings_stats(
		self,
		anime_id: int | None = None,
	) -> list[DubbingStats]:
		if anime_id:
			self.load_anime(
				anime_id=anime_id,
			)
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
