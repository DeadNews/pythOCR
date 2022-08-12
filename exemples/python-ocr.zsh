#!/usr/bin/env zsh

for F in "$@"; do
    cd "${F:h}"

    # mode='filter'
    # mode='ocr'
    mode='full'

    appDir='/path/to/pythOCR'
    python /path/to/pythoCR.py --lang 'rus' -c "${appDir}/config/userconfig.ini" \
        --vpy "${appDir}/exemples/[1920x1080]_FilterTemplatev2.vpy" --regex-replace "${appDir}/config/regex_replace_my.json"\
        --sub-format ass --mode ${mode} --work-dir '/tmp/' --output-dir "./OCRv0/" ${F}

    mkdir -p "./OCRv1"
    /path/to/re-ocr.py "./OCRv0/${F:t:r}.ass"

done

kdialog --title "${0:t:r}" --passivepopup "${1:h:t} done" 7

# mkdir ~/my/bin/pyenv_temp
# cd ~/my/bin/pyenv_temp
# python -m venv . --system-site-packages
# source ~/my/bin/pyenv_temp/bin/activate
# pip install colorama configargparse opencv-python tqdm ...
