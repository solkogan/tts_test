Пример программы, которая синтезирует речь с помощью модуля Python https://pypi.org/project/pyttsx3/

Сперва нужно установить голоса отсюда:

https://github.com/Olga-Yakovleva/RHVoice/wiki/Latest-version - прокрутите до раздела SAPI5 Russian

Самый лучший голос это Алена - https://cloud.mail.ru/public/3NBP26GRC42z/AcapelaGroup_Alena_Nvda.ru.rar 

После того как голоса есть в системе, установите модуль:

pip install pyttsx3

Запустите программу voicelist.py чтобы узнать список голосов и их имена

Скопируйте имя нужного вам голоса в программу testspeak.py

Обратите внимание что у Алены имя заканчивается на SAPI 5 и всю эту строку нужно считать за имя (а не только Alyona)

