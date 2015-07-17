__author__ = 'gil'

from nltk.corpus import wordnet
import re
song_words_theme ={}
rhymes=[]


# initial dic from txt file according to theme
def makeDic():
    f = open('TimeToRhyme/words.txt', 'r')
    stringtp = re.sub(r'\(.+?\)\s*', '', f.read())
    tmp=stringtp.split('#')
    j=0;
    while j<len(tmp):
        ans=tmp[j]
        ans= tmp[j].split('\n')
        ans=" ".join(ans).split(' ')
        song_words_theme[ans[1]]=ans[2:]
        j=j+1
    for item in song_words_theme.values():
         item.append(0)



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















# set points to each theme acoording to the song words
def setPoint(word):
    for i in song_words_theme.keys():
        if word in song_words_theme[i]:
            N=len(song_words_theme[i])
            song_words_theme[i][N-1]=song_words_theme[i][N-1]+1



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



# return the song theme until now
def whatTheTheme():
    max=0
    songTheme=''
    for theme in song_words_theme.keys():
        N= len(song_words_theme[theme])
        if song_words_theme[theme][N-1]> max :
            max=song_words_theme[theme][N-1]
            songTheme=theme
    return songTheme

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


