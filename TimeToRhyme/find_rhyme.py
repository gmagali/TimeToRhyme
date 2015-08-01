__author__ = 'gil'

from nltk.corpus import wordnet


rhymes=[]


# initial dic from txt file according to theme
def makeDicRhyms():
    f = open('TimeToRhyme/rhyms.txt', 'r')
    stringtp = f.read()
    stringtp=stringtp.replace(" ", "")
    tmp=stringtp.split('#')
    j=0;
    while j<len(tmp):
        ans=tmp[j]
        ans= tmp[j].split('\n')
        ans="".join(ans).split(',')
        rhymes.append(ans)
        j=j+1


# find list of rhyme in acoording to theme
def its_rhyme(subject, word):
    rhymeList=[]
    endWord=word[len(word)-3:]
    N= len(song_words_theme[subject])
    for i in song_words_theme[subject][:N-2]:
        if endWord == i[len(i)-3:]:
            rhymeList.append(i)
    return rhymeList


# find list of rhime
def its_rhyme_test( word):
    i=0
    while(i<len(rhymes)):
      if rhymes[i].__contains__(word):
          return rhymes[i]
      else:
          i=i+1
    return []




def DeletBlancks (list):
    ans=[]
    for i in list:
        if not i=="" or i=='\n\n':

            ans.append(i)
    return ans


def Find_synonyms(word):

    tmp=[]
    for synset in wordnet.synsets(word,pos='n'):
        for lemma in synset.lemmas():
            tmp.append( lemma.name())

    return set(tmp)


import nltk
def rhyme(inp, level):
     entries = nltk.corpus.cmudict.entries()
     syllables = [(word, syl) for word, syl in entries if word == inp]
     rhymes = []
     for (word, syllable) in syllables:
             rhymes += [word for word, pron in entries if pron[-level:] == syllable[-level:]]
     return set(rhymes)



def its_rhyme1(listWords, word):
    ans=[]

    for newword in listWords:
        if doTheyRhyme(newword, word):
            ans.append(newword)
    return ans


def doTheyRhyme ( word1, word2 ):
  # first, we don't want to report 'glue' and 'unglue' as rhyming words
  # those kind of rhymes are LAME
  if word1.find ( word2 ) == len(word1) - len ( word2 ):
      return False
  if word2.find ( word1 ) == len ( word2 ) - len ( word1 ):
      return False

  return word1 in rhyme ( word2, 2 )





from nltk.corpus import wordnet as wn

def makeCategoriesList(text):
    categotyList=[]
    for word in nltk.word_tokenize(text):
        try:
            word = wn.synset(word+'.n.01')
            theme=word.hypernyms()
            for lemma in theme[0].lemmas():
                     ans= lemma.name()
            em=wn.synset(ans+".n.01")
            newwords=em.hyponyms()
            for sys in newwords:
                     categotyList.append(sys.lemmas()[0].name())
        except Exception , e :
            pass
    return set(categotyList)



