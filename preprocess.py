import json
import os
from tqdm.auto import tqdm

tqdm.pandas()
from transformers import AutoTokenizer
from tone_utils import clear_all_marks


def vowel_split(x):
    for i, c in enumerate(x):
        if c in ["a", "e", "i", "o", "u", "y"]:
            return x[i:]
    return None


def do_rhyme(v1, v2):
    if v1[0] in ["u", "y"] and len(v1) > 2 and v1[1] in ["a", "e", "i", "o"]:
        v1 = v1[1:]
    if v2[0] in ["u", "y"] and len(v2) > 2 and v2[1] in ["a", "e", "i", "o"]:
        v2 = v2[1:]
    return v1 == v2


token = ""
tokenizer = AutoTokenizer.from_pretrained("bkai-foundation-models/vietnamese-llama2-7b-40GB", token=token)
words = dict([(tokenizer.decode([i]), i) for x, i in tokenizer.get_vocab().items()])
syllables = [x.strip() for x in open("./data/syllables.txt").readlines()]
words = dict([(x, i) for x, i in tqdm(words.items()) if x.lower().strip() in syllables])

words_extra = dict([
    (x, {
        "id": i,
        "vowel": vowel_split(clear_all_marks(x.lower()).lower().strip())
    })
    for x, i in words.items()])

for key, val in tqdm(words_extra.items()):
    rhymes = []
    val["rhymes_with"] = []
    for other_key, other_val in words_extra.items():
        if key == other_key:
            continue
        if do_rhyme(val["vowel"], other_val["vowel"]):
            val["rhymes_with"].append(other_key)
    val["rhymes_with_ids"] = [words_extra[x]["id"] for x in val["rhymes_with"]]

with open("data/rhymables.json", "wt") as f:
    json.dump(words_extra, f)
