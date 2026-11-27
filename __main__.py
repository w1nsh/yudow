from pathlib import Path

from src.app import YuDow

BASE_DIR = Path(__file__).parent
ENCODING = 'utf-8'

yudow = YuDow(
	BASE_DIR,
	ENCODING,
)

yudow.load_anime(357)
lds =  yudow._anime_metadata
lds_path = Path(__file__).parent / 'tests' / 'am.txt'
lds_path.write_text(str(lds), encoding=ENCODING)
