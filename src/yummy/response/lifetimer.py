from pathlib import Path
import datetime

from src.yummy.response.filenames import ReponseFilenames
from src.yummy.response.timestamp import ResponseTimestamp


TIME_FORMAT = '%Y.%m.%d %H:%M:%S.%f'

class ResponseLifetimer:
	def __init__(
		self,
		base_rdir: Path,
		timestamp_lifetime: int = 30,
	) -> None:
		self._base_rdir = base_rdir
		self._timestamp_lifetime = timestamp_lifetime


	def write(
		self,
		timestamp: ResponseTimestamp,
	) -> None:
		f_timestamp = timestamp.timestamp.strftime(TIME_FORMAT)
		filepath = self._base_rdir / f'{timestamp.filename.value}.txt'
		filepath.write_text(
			f_timestamp,
		)


	def load(
		self,
		filename: ReponseFilenames,
	) -> ResponseTimestamp:
		filepath = self._base_rdir / f'{filename.value}.txt'
		file_data = filepath.read_text()
		timestamp = datetime.datetime.strptime(
			file_data,
			TIME_FORMAT,
		)
		return ResponseTimestamp(
			filename=filename,
			timestamp=timestamp,
		)


	def timestamp(
		self,
		filename: ReponseFilenames,
	) -> ResponseTimestamp:
		return ResponseTimestamp(
			filename=filename,
			timestamp=datetime.datetime.now()
		)


	def timestamp_is_valid(
		self,
		timestamp: ResponseTimestamp,
	) -> bool:
		min_time = datetime.timedelta(0)
		max_time = datetime.timedelta(
			seconds=self._timestamp_lifetime,
		)
		time_difference = datetime.datetime.now() - timestamp.timestamp
		return min_time < time_difference < max_time


	def timestamp_is_exists(
		self,
		filename: ReponseFilenames,
	) -> bool:
		return (self._base_rdir / f'{filename.value}.txt').exists()
