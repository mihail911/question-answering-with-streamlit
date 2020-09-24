from typing import Dict, Union

from attrdict import AttrDict  # type: ignore

config: Dict[str, Union[int, str]] = {"framework": "pt", "NUM_SENT": 10}
config = AttrDict(config)
