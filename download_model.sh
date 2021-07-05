#! /bin/bash

wget https://alphacephei.com/vosk/models/vosk-model-small-ru-0.15.zip
unzip vosk-model-small-ru-0.15.zip
mkdir model
mv vosk-model-small-ru-0.15/* model/
rm -r vosk*
