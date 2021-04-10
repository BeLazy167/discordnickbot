from random import randint
#convert file to list
def nicke():
    def ad(z, f) :
        for lines in z :
            lines = lines.rstrip( )
            f.append( lines )
        return f

    #creating noun list
    noun_list = open( 'noun' )
    nouns = list( )
    nouns = ad( noun_list, nouns )

    #creating adjective list
    adjective_list = open( 'final_adjective.txt' )
    adjectives = list( )
    adjectives = ad(adjective_list,adjectives)

    #creating verb list
    verb_list = open( 'verbs' )
    verbs = list()
    verbs = ad( verb_list,verbs)

    #random int for adjective
    for_adjective = randint( 0, len( adjectives ) )

    #random int for verb
    for_verbs = randint( 0, len( verbs ) )

    #random int for noun
    for_noun = randint(0,len(nouns))

    #to choose between verb and adjective
    toss = randint( 1, 2 )

    if toss == 1 :#for adjective + noun pair
        name = ( adjectives[ for_adjective ] + ' ' + nouns[for_noun] )

    else : #for verb + noun pair
        name =  ( verbs[ for_verbs] + ' ' + nouns[for_noun])
    return name