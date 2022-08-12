#!/usr/bin/env python
from pathlib import Path
from re import MULTILINE, sub
from sys import argv


def regex(text):
    text = sub(r"\\N", r" ", text)
    text = sub(r"\\n", r" ", text)
    text = sub(r"{\\i1}", r"", text)
    text = sub(r"{\\i0}", r"", text)
    text = sub(r"\\i1", r"", text)
    text = sub(r"{an8}", r"{\\an8} ", text)
    text = sub(r'<font color="#ffff00">', r"{\\an8} ", text)
    text = sub(r'<font.olor="#ffff00">', r"{\\an8} ", text)
    text = sub(r"{\\an}", r"", text)
    text = sub(r" +", r" ", text)
    text = sub(r" +'", r"'", text)
    text = sub(r"!'!", r"!", text)
    text = sub(r"'!", r"!", text)
    text = sub(r"!'", r"!", text)
    text = sub(r"! \.", r"!..", text)
    text = sub(r"\. ,", r".", text)
    text = sub(r" \.", r".", text)
    text = sub(r"\МАКАМТМ", r"Wakanim", text)
    text = sub(r"\\\\Wakanim", r"Wakanim", text)
    text = sub(r"\\Wakanim", r"Wakanim", text)
    text = sub(r"'\n", r"!\n", text)
    text = sub(r" !", r"!", text)
    text = sub(r" \?", r"?", text)
    text = sub(r"чЧ", r"Ч", text)
    text = sub(r"ОЙ", r"Ой", text)
    text = sub(r"©бпасибо", r"Спасибо", text)
    text = sub(r"@тправимся", r"Отправимся", text)
    text = sub(r"@н", r"Он", text)
    text = sub(r"« ", r"«", text)
    text = sub(r"[«<‹][«<‹]", r"«", text)
    text = sub(r"[«<‹][«<‹]", r"«", text)
    text = sub(r" »", r"»", text)
    text = sub(r"[»>›][»>›]", r"»", text)
    text = sub(r"[»>›][»>›]", r"»", text)
    text = sub(r'[«<‹"](.+?)["»>›]', r"«\1»", text)
    # text = sub(r' —', r'\\N—', text)
    # text = sub(r'\"(.+?)\"', r'«\1»', text)
    text = sub(
        r"Редакторы Марина Степанцова, Екатерина Гусева",
        r"Переводчик: Андрей трубицын \\N Редакторы: Марина Степанцова, Екатерина Гусева",
        text,
    )
    text = sub(
        r"Руководитель проекта Юлия Парамонова",
        r"Руководитель проекта: Юлия Парамонова \\N OCR: Kawaiika; Редактура: JiLleON",
        text,
    )
    text = sub(
        r"«Истребитель демонов» «Китеё5и по Уа!Бба»",
        r"«Истребитель демонов» \\N «Kimetsu no Yaiba»",
        text,
    )
    text = sub(r"СУККУбОЧ ками", r"суккубочками", text)

    save = 0
    if save:
        # https://habr.com/ru/post/349860/#lookaroundfrance
        # ушло в первый прогон:
        text = sub(r"^[.,‚„][.,‚„]", r"...", text, flags=MULTILINE)
        text = sub(r"[.,‚„][.,‚„][.,‚„]", r"...", text)
        text = sub(r"[.,‚„][.,‚„][.,‚„][.,‚„]", r"...", text)

    return text


test_text = r"""
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
не начало строки ‚.ищем, где
,.,
‚.‚
— Диалог. — Да.
"""

if not argv[1:]:
    text = regex(test_text)
    print(text)

else:
    for infile in argv[1:]:
        p = Path(infile)
        text = p.read_text()
        text = regex(text)

        Path(p.parents[1], "OCRv1", f"{p.stem}.regex.ass").write_text(text)
