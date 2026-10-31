from pathlib import Path

from src.app import YuDow


BASE_RDIR = Path(__file__).parent / 'responses'
ENCODING = 'utf-8'

yudow = YuDow(
	BASE_RDIR,
	ENCODING,
)

print(yudow.search_anime('этот', 5))


# yp.get_anime(anime_url)
# lad = yrp.load_anime_data()
# lad_path = Path(__file__).parent / 'tests' / 'lad.txt'
# lad_path.write_text(
# 	str(lad),
# 	encoding=ENCODING,
# )
