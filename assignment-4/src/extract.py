from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import pos_tag
from nltk import ne_chunk
from nltk import Tree

waste = ['physics','chemistry','physiology','literature','wikipedia']

class NEExtract:
    def __init__(self,data):
        self.text = data
    def main(self):
        text = self.text

        nmli = []
        try:
            for sentence in sent_tokenize(text):
                #print '\nSentence:\n', sentence
                tokens = word_tokenize(sentence)
                pos_tagged_tokens = pos_tag(tokens)
                phrase_chunks = ne_chunk(pos_tagged_tokens)
                #print 'tokens:\n', tokens
                #print 'tokens with part of speech tags:\n', pos_tagged_tokens
                for chunk in [chunk for chunk in phrase_chunks if hasattr(chunk, 'node')]:
                    nmli.append(  Tree(
                        chunk.node, [(' '.join(c[0] for c in chunk.leaves()))]).__str__() )
        except :
            pass

        neli = []    
        for j in nmli:
            temp = dict()
            j = j.strip('()')
            nl = j.split()
            k = 1
            ntype = nl[0]
            nname = ' '.join(nl[1:])
            if ntype == 'PERSON' or ntype == 'GPE':
                temp['type'] = ntype
                temp['name'] = nname
                if temp not in neli and nname.lower() not in waste:
                    neli.append(temp)

        print '#'*70+'\nNamed Entites\n'+'#'*70            
        for j in neli:
            ntype = j['type']
            nname = j['name']            
            print ntype+',    '+nname
