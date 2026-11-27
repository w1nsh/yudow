from pathlib import Path

from src.app import YuDow

BASE_DIR = Path(__file__).parent
ENCODING = 'utf-8'

yudow = YuDow(
	BASE_DIR,
	ENCODING,
)

yudow.load_anime(357)
lds =  yudow._config
lds_path = Path(__file__).parent / 'tests' / 'del_url_to_boolean.txt'
lds_path.write_text(str(lds), encoding=ENCODING)
