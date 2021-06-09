import random as r

def UltraFormat(s:str)->str:
    wordBuffer=s.split(" ")
    while "" in wordBuffer:
        wordBuffer.remove("")
    forbidden=(
        "i","you","we","they","it","he","she",
        "me","us","them","him","her",
        "my","your","our","their","its","his",
        "mine","yours","ours","theirs","hers",
        "a","an","the","this","that","these","those",
        "is","are","am",
        "do","does","doing","did","done",
        "have","has","having","had",
        "what","when","why","where","how","who","which","whom","whomst","whence",
        "about","above","after","beside","besides","before","can","could","even","for","here","there",
        "in","on","at","no","not","yes","or","and","per","but","so","should","shall","to","till","from","must","ought",
        "let","perhaps","unless","may","of","up","down","despite","although","though","albeit","spite","always","very",
		"gonna","wanna","coulda","shoulda","oughta",
        "ultra","ultraman","ultramen","ultrawoman","ultrawomen",
        "",
    )
    special=(
        "i'm","you're","he's","she's","it's","they're","we're",
        "i've","you've","they've","we've",
        "i'd","you'd","he'd","she'd","it'd","they'd","we'd",
        "don't","let's",
    )
    for pos,word in enumerate(wordBuffer):
        scapegoat=word
        if scapegoat.lower() not in special:
            for symbol in "`\"|'<^>!?,.:;-()[]{}=+&%@#$~/*0123456789":
                scapegoat=scapegoat.replace(symbol,"")
            if scapegoat.lower() not in forbidden:
                wordBuffer[pos]=f"**Ultra**-{word}" if r.randrange(4) in (0,2) else word
    return " ".join(wordBuffer)
