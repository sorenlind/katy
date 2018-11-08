# coding: utf-8
"""Classifier based on TextCat algorithm."""

from collections import Counter

import regex
from cleanliness import normalize

CUTOFF = 200
NMAX = 5


def preprocess_text(text):
    """Prepare text for computing profile."""
    text = normalize(text)
    text = remove_punctuation(text)
    return text


def remove_punctuation(text):
    """Remove punctuation except single quotes and dashes."""
    return regex.sub(r"[^\P{P}\'\-]+", "", text)


def compute_profile(text, nmax, cutoff):
    """Compute profile of specified text."""
    ngram_counter = Counter()
    words = text.split()
    for word in words:
        ngrams = ngrams_from_word("_" + word + "_", nmax)
        ngram_counter.update(ngrams)

    temp = [ngram for ngram, _freq in sorted(ngram_counter.items(), key=lambda x: x[1], reverse=True)][:cutoff]
    return {ngram: index + 1 for index, ngram in enumerate(temp)}


def ngrams_from_word(word, nmax):
    """Build all possible character n-grams of length 1 to nmax for specified word."""
    ngrams = []
    for pos in range(len(word)):
        for size in range(1, nmax + 1):
            if size + pos > len(word):
                break
            ngram = word[pos:pos + size]
            ngrams.append(ngram)
    return ngrams


def compute_distance(profile_a, profile_b):
    """Compute the distance between specified profiles."""
    distance = 0
    penalty_unknown = max(len(profile_a), len(profile_b)) + 1
    all_n_grams = set([n_gram for profile in [profile_a, profile_b] for n_gram in profile.keys()])
    for n_gram in all_n_grams:
        distance += abs(profile_a.get(n_gram, penalty_unknown) - profile_b.get(n_gram, penalty_unknown))
    return distance


class TextCat(object):
    """Class for text classification using the TextCat algorithm."""

    def __init__(self, profiles, nmax, cutoff):
        """Initialize a TextCat instance using specified profiles."""
        self.profiles = profiles
        self.nmax = nmax
        self.cutoff = cutoff

    def profile(self, text):
        """Compute the profile of specified raw text."""
        text = preprocess_text(text)
        return compute_profile(text, self.nmax, self.cutoff)

    def classify(self, text):
        """Classify specified text."""
        profile = self.profile(text)
        scores = {}
        for lang, lang_profile in self.profiles.items():
            scores[lang] = compute_distance(profile, lang_profile)
        return min(scores, key=scores.get)


def load():
    """Load and intialize TextCat classifier."""
    from .profiles import LANGUAGE_PROFILES
    return TextCat(LANGUAGE_PROFILES, NMAX, CUTOFF)
