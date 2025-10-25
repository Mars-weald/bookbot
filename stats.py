def words_in_book(vords):
    listed_words = vords.split()
    return len(listed_words)

def characters_in_book(vords):
    characters = {}
    small = vords.lower()
    for c in small:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

def sordid(d):
    liszt = []
    dicty = {}
    for e in d:
        if e.isalpha():
            dicty["character"] = e
            dicty["number"] = d[e]
            liszt.append(dicty)
            dicty = {}
        else:
            pass
    def sort_by(v):
        return v["number"]
    liszt.sort(reverse=True, key=sort_by)
    return liszt
