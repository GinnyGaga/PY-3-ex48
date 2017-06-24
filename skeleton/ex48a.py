class lexicon(object):

    def scan(stuff):
        sentence = []
        directions = ['north','south','east']
        verbs = ['go','kill','eat']
        stops = ['in','of','the']
        nouns = ['bear','princess']
        numbers = [3,91234,1234]
        errors = ['IAS','ASDFADFASDF']
        words = stuff.split()

        for word in words:
            try:
                intword = int(word)
                sentence.append(('number',int(word)))
            except ValueError:

                if word in directions:
                    sentence.append(('direction',word))
                elif word in verbs:
                    sentence.append(('verb',word))
                elif word in stops:
                    sentence.append(('stop',word))
                elif word in nouns:
                    sentence.append(('noun',word))
                elif word in errors:
                    sentence.append(('error',word))        
                else:
                    sentence.append(('unkown',word))
        return sentence


    print (scan("go north"))
    print (scan("kill the princess"))
    print (scan("eat the bear"))
    print (scan("open the door and smack the bear in the nose"))
    print (scan("open 1234 door"))
