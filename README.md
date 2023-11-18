# Lục bát generator that strictly follows the rules 
Generating thơ lục bát (and other traditional kinds with rhyme and tone rules) using arbitrary LMs by customizing `huggingface`'s `generate` function. 
Without custom logits processor:
```
mùa hè nắng nóng oi nồng
mưa rào rào hạt mưa tuôn xối xả
mây mù giăng kín trời xanh
gió lùa qua kẽ lá xào xạc rì rào
nhìn ra ngoài nắng chói chang
nhớ mùa đông giá buốt căm căm
mùa đông rét mướt lạnh căm
mồ hôi ướt đẫm mặt mày tái xanh
```
With customized logits processor:
```
đêm hè nóng nực oi nồng
để em nhớ lại mùa đông năm nào
đêm đông rét mướt mưa rào
ấm êm giấc ngủ ngọt ngào giấc mơ
đêm khuya gió lạnh sương mờ
bên thềm em đứng đợi chờ bóng ai
đêm xuân hoa nở đầy đài
đêm thu lá rụng rơi dài khắp sân
đêm rằm đèn đỏ rực ngàn
đêm trăng rằm tháng tám tràn trề hương
```
## The rules
> Quy tắc cơ bản của cặp câu lục bát là các tiếng thứ 2, 6, 8 mang thanh bằng, tiếng thứ 4 mang thanh trắc, còn lại có thể tùy ý. Đuôi câu lục vần với tiếng thứ sáu của câu bát, đuôi câu bát vần với đuôi câu lục sau. Nếu tiếng thứ sáu của câu bát là thanh ngang (dương bình) thì tiếng thứ 8 phải là thanh huyền (âm bình) và ngược lại.

By building a dictionary of rhymable syllables and a custom logits processor, we can enforce the next token to contain specific vowels and/or rhyme with a previous token. see class `SixEightLogitsProcessor` in `generation/logits_process.py` for details.

## Run the code
First you may need to generate the rhymable dict for your specific tokenizer/model. See `preprocess.py`

The model used in this repo is `suicaokhoailang/bkllama2-poem-generator` which I've finetuned from `bkai-foundation-models/vietnamese-llama2-7b-40GB'` on  the Vietnamese poem dataset at `Libosa2707/vietnamese-poem`. The algorithm however should work on any language models, you may need to tune the prompt a little bit and performance may vary,
See the `infer` on how to run the code for inference.

## What's next
- Creating new logits processor for other kinds of poems
- ???
- Profits