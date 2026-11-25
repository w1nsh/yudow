from datetime import datetime
from dataclasses import dataclass

from src.yummy.response.filenames import ReponseFilenames


@dataclass
class ResponseTimestamp:
	filename: ReponseFilenames
	timestamp: datetime
