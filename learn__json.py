from dataclasses import is_dataclass, asdict
from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from json.encoder import JSONEncoder


class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)
        if isinstance(o, (datetime, date)):
            return o.isoformat()
        if is_dataclass(o):
            return asdict(o)
        if isinstance(o, Enum):
            return o.value
        if isinstance(o, Exception):
            return str(o)
        return JSONEncoder.default(self, o)
