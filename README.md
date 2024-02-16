# Steins;Gate dialogue parser

Parses Steins;Gate VN dialogue like this:
```html
<voice name="Rintaro" class="VID_OKA" src="voice/OKA_0160" mode="on">
"But they underestimated me, for I am not so easily played. One day, I will expose their deeds and put an end to their reign!"

</PRE>

<PRE @box00>[text00290]
Having come to a satisfactory conclusion, I take a celebratory bottle of Dr P -- my favorite soda -- from the fridge.

The lab has no air conditioning. Ice cold drinks are essential.


<voice name="Rintaro" class="VID_OKA" src="voice/OKA_0161" mode="on">
"Ah, <I>elixir intellectualis</i>⑰, a drink fit for a genius!"

</PRE>

<PRE @box00>[text00300]
<voice name="Itaru" class="VID_DAR" src="voice/DAR_0012" mode="on">
"Cola's better."
```
and produces a cleaned JSON file with this:
```json
  {
    "char": "Rintaro",
    "text": "\"But they underestimated me, for I am not so easily played. One day, I will expose their deeds and put an end to their reign!\""
  },
  {
    "text": "Having come to a satisfactory conclusion, I take a celebratory bottle of Dr P -- my favorite soda -- from the fridge."
  },
  {
    "text": "The lab has no air conditioning. Ice cold drinks are essential."
  },
  {
    "char": "Rintaro",
    "text": "\"Ah, *elixir intellectualis*\u2470, a drink fit for a genius!\""
  },
  {
    "char": "Itaru",
    "text": "\"Cola's better.\""
  },
```

Expects an input file called 'Master_Copy.txt' and produces a 'parsed.json'