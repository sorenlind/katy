# 👩‍⚖️ katy

This is a small package for doing language detection using the TextCat algorithm.

It supports only a few languages:

* Danish
* English
* Finnish
* German
* Swedish

It was trained on the [Europarl](http://www.statmt.org/europarl/) dataset.

## Usage

```python
from katy import textcat
classifier = textcat.load()
classifier.classify("Here we are now, entertain us.")
```