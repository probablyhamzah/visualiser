# Visualiser
A terminal visualiser for songs.

![Alt text](stuff/sample1.png?raw=true "SamplePic1")

![Alt text](stuff/sample2.png?raw=true "SamplePic2")

## Installation
```bash
pip3 install visualiser
```

## Usage
```python
from visualiser import Visualiser

viz = Visualiser('path/to/audio-file')

# for rgb colours:
# viz = Visualiser('path/to/audio-file', is_rgb=True)

viz.visualise()
```
