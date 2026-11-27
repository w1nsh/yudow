from pathlib import Path
from typing import Any
import requests
import json

from src.yummy.response.filenames import ReponseFilenames


class YummyParser:
	_BASE_URL = 'https://api.yani.tv'

	def __init__(
		self,
		encoding: str,
		rdir: Path,
	) -> None:
		self._encoding = encoding
		self._rdir = rdir


	def write(
		self,
		response: dict[str, Any],
		response_file: Path,
	) -> None:
		"""
		Writes api reponse as json file.

		Args:
			response (dict[str, Any]): Reponse data for writing.
			response_file (Path): Path to the reponse file.
		"""
		json_response = json.dumps(
			response,
			ensure_ascii=False,
			indent=4
		)
		response_file.write_text(
			json_response,
			encoding=self._encoding,
		)

	
	def search(
		self,
		filename: ReponseFilenames,
		query: str,
		limit: int,
		offset: int = 0,
	) -> None:
		method = 'search'
		unique_params = {
			'q': query,
			'offset': offset,
			'limit': limit,
		}
		response = self._get_request(
			url_endpoint=method,
			params=unique_params
		)
		self.write(
			response=response,
			response_file=self._rdir / f"{filename.value}.json",
		)


	def get_anime(
		self,
		filename: ReponseFilenames,
		anime_id: int,
		need_videos: bool = True,
	) -> None:
		method = 'anime'
		formated_need_videos = self._to_url_boolean(need_videos)
		unique_params = {
			'need_videos': formated_need_videos,
		}
		response = self._get_request(
			url_endpoint=f'{method}/{anime_id}',
			params=unique_params,
		)
		self.write(
			response=response,
			response_file=self._rdir / f'{filename.value}.json',
		)


	def _to_url_boolean(
		self,
		value: bool,
	) -> str:
		return 'true' if value else 'false' # точно надо или нет?


	def _get_request(
		self,
		url_endpoint: str,
		params: dict[str, Any] | None = None,
	) -> dict[str, Any]:
		"""
		Sends a GET request to the specified API endpoint with the given parameters.

		Args:
			url_endpoint (str): The API endpoint to send the request to.
			params (Optional[dict[str, Any]]): Additional parameters specific to the request. Defaults to None.

		Returns:
			dict[str, Any] | None: The JSON response from the API if the request is successful, None otherwise.
		"""
		url = f'{self._BASE_URL}/{url_endpoint}'
		response = requests.get(
			url,
			params=params,
		)
		response.raise_for_status() # try + endpoint error handling
		json_response = response.json()
		return json_response
