#!/usr/bin/env python

import re
import json


def type_regex_replace(string):
    with open(string, "r", encoding="utf8") as inputfile:
        json_str = inputfile.read()
    json_str = json.loads(json_str)
    return [(re.compile(entry["regex"]), entry["replace"]) for entry in json_str]


regex_replace_my = type_regex_replace('/home/deadnews/my/bin/pythOCR/config/regex_replace_my.json')
# print(regex_replace_my)

text = r"""
»>› → »
›› → »
»> → »
<< → «
<‹ → «
'! → !
! . → !..
л. , → л.
л . → л.
лол ? → лол?
лол ! → лол!
МАКАМТМ → Wakanim
\\Wakanim → Wakanim
---
лол'
↓
лол!
---
лол\nлол\nлол → лол лол лол
Но\Nкак?
---
лол   лол → лол лол
"название" → «название»
©бпасибо
{\i1}убита‚{\i0} → убита‚
{an8\i1} → {\an8}
<font.olor="#ffff00"> → {\an8}
<font color="#ffff00">Погибель демонов{\an} → {\an8} Погибель демонов
Нет,\Nнельзя'\NВы\Nбудете\Nтолько\Nзадерживать\NТандзиро.
‚.ищем, где перепихнуться с невиданными расами!
ЛОЛ ‚.ищем, где
"""

# test = re.sub(r'\'\n', r'!\n', text)
# test = re.sub(r'\\n', r' ', text)
# test = re.sub(r' +', r' ', text)
# test = re.sub(r'\"(.+?)\"', r'«\1»', text)
# test = re.sub(r'\\\\Wakanim', r'Wakanim', text)
# test = re.sub(r'{\\i1}', r'', text)

# print(test)

for regex in regex_replace_my:
    text = re.sub(regex[0], regex[1], text)

print(text)
