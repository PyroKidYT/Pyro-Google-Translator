# © PyroKid

import asyncio
from google_translate_py import AsyncTranslator

# Language Codes
############################
# Amharic	am
# Arabic	ar
# Basque	eu
# Bengali	bn
# English (UK)	en-GB
# Portuguese (Brazil)	pt-BR
# Bulgarian	bg
# Catalan	ca
# Cherokee	chr
# Croatian	hr
# Czech	cs
# Danish	da
# Dutch	nl
# English (US)	en
# Estonian	et
# Filipino	fil
# Finnish	fi
# French	fr
# German	de
# Greek	el
# Gujarati	gu
# Hebrew	iw
# Hindi	hi
# Hungarian	hu
# Icelandic	is
# Indonesian	id
# Italian	it
# Japanese	ja
# Kannada	kn
# Korean	ko
# Latvian	lv
# Lithuanian	lt
# Malay	ms
# Malayalam	ml
# Marathi	mr
# Norwegian	no
# Polish	pl
# Portuguese (Portugal)	pt-PT
# Romanian	ro
# Russian	ru
# Serbian	sr
# Chinese (PRC)	zh-CN
# Slovak	sk
# Slovenian	sl
# Spanish	es
# Swahili	sw
# Swedish	sv
# Tamil	ta
# Telugu	te
# Thai	th
# Chinese (Taiwan)	zh-TW
# Turkish	tr
# Urdu	ur
# Ukrainian	uk
# Vietnamese	vi
# Welsh	cy

async def main():
    print(await AsyncTranslator().translate("Hello!!", "en", "hi"))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

