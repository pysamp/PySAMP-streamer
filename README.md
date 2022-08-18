# PyStreamer

[Streamer](https://github.com/samp-incognito/samp-streamer-plugin) plugin handler for [PySAMP](https://github.com/pysamp/PySAMP)

## Installing

1. To install, you need to download the streamer plugin. After that you must put `streamer.dll` into your server folder (`serverfolder/plugins`).

2. After that, download the repository and put the pystreamer folder in the python folder).

## Example

```python
from .pystreamer.dynamicobject import DynamicObject
from pysamp import on_gamemode_init

@on_gamemode_init
def on_ready():
    global obj
    obj = DynamicObject.create(994, 1161.73767, -1741.43555, 13.06450, 0.0, 0.0, 0.0)
```

## Thanks to

* [Incognito](https://github.com/samp-incognito) for Streamer plugin
* [denNorske](https://github.com/dennorske), [habecker](https://github.com/habecker), [Cheaterman](https://github.com/Cheaterman) for developing PySAMP
* [Me](https://github.com/Ykpauneu) for handler