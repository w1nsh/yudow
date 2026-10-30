from pathlib import Path
from typing import Any
import json


class ResponseParser:
	def __init__(
		self,
		encoding: str,
		base_rdir: Path,
	) -> None:
		self._encoding = encoding
		self._base_rdir = base_rdir


	def get_anime_url(
		self,
	) -> str:
		json_data = self._read_json(
			file=self._base_rdir / "search.json",
		)
		return json_data["response"][0]["anime_url"]


	def g(self): pass


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
	