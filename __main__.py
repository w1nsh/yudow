from pathlib import Path

from src.app import YuDow


BASE_RDIR = Path(__file__).parent / 'responses'
ENCODING = 'utf-8'

yudow = YuDow(
	BASE_RDIR,
	ENCODING,
)

yudow.load_anime(357, True)
lds =  yudow._anime_metadata
lds_path = Path(__file__).parent / 'tests' / 'am.txt'
lds_path.write_text(str(lds), encoding=ENCODING)
