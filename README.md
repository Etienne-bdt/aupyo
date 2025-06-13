# AUPYO: Audio Processing Utilities in Python

AUPYO is a Python package designed to provide utility functions for some audio processing. 

## Features

## Installation

You can install AUPYO using pip. First, clone the repository:

```bash
git clone https://github.com/Etienne-bdt/aupyo.git
cd aupyo
```

Then, install the package:

```bash
pip install .
```

## Usage

For now aupyo exposes two audio classes
- a Track, containing a duration, sample rate, raw audio data, ...
- a Mixture, a dictionnary of multiple tracks with instrument as keys.

### Example usage 

```python
from aupyo.type import Mixture, Track
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### Project management

This project uses [uv](https://astral.sh/uv) to manage dependencies ! 
If you want to deploy the dev .venv easily, just install `uv` and run

```bash
uv sync
```

This should get you started instantly. 

## License

This project is licensed under the Apache 2.0 - see the [LICENSE](LICENSE) file for details.