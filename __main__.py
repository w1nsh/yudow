from pathlib import Path

from src.yummy.parser import YummyParser
from src.yummy.response_parser import ResponseParser


ENCODING = "utf-8"
BASE_RDIR = Path(__file__).parent / "responses"


yp = YummyParser(
	encoding=ENCODING,
	base_rdir=BASE_RDIR,
)
yrp = ResponseParser(
	encoding=ENCODING,
	base_rdir=BASE_RDIR,
)

yp.search('этот')
anime_url = yrp.get_anime_url()
yp.get_anime(anime_url)
