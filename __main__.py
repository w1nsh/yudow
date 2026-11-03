from pathlib import Path

from src.app import YuDow


BASE_RDIR = Path(__file__).parent / 'responses'
ENCODING = 'utf-8'

yudow = YuDow(
	BASE_RDIR,
	ENCODING,
)
