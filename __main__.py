from pathlib import Path

from src.app import YuDow


BASE_RDIR = Path(__file__).parent / 'responses'
ENCODING = 'utf-8'

yudow = YuDow(
	BASE_RDIR,
	ENCODING,
)

yudow.load_anime(357, False)
lds =  yudow.load_dubbings_stats()
lds_path = Path(__file__).parent / 'tests' / 'lds.txt'
lds_path.write_text(str(lds), encoding=ENCODING)
