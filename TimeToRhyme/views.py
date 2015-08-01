

from django.shortcuts import render_to_response
import find_rhyme


def home(request):
    if 'Notheme' in request.GET:
        song=request.GET['MySong']
        if not song=="":
                tmp=song.split('\n')
                tmp=" ".join(tmp).split('\r')
                tmp="".join(tmp).split(' ')
                tmp = find_rhyme.DeletBlancks(tmp)
                word='Words that rhymes with '+tmp[len(tmp)-1]
                rhymeList=find_rhyme.its_rhyme_test(tmp[len(tmp)-1])
                return render_to_response('home.html',{'song':song,'rhymeList':rhymeList , 'word':word})
        else:
            song=""
            rhymeList=[]
            return render_to_response('home.html',{'song':song,'rhymeList':rhymeList})

    elif 'Theme' in request.GET:
        song=request.GET['MySong']
        if not song=="":
            tmp=song.split('\n')
            tmp=" ".join(tmp).split('\r')
            tmp="".join(tmp).split(' ')
            tmp = find_rhyme.DeletBlancks(tmp)
            list=find_rhyme.makeCategoriesList(" ".join(tmp))
            word='Words that rhymes with '+tmp[len(tmp)-1]
            x=tmp[len(tmp)-1]
            rhymeList=find_rhyme.its_rhyme1(list,x)
            return render_to_response('home.html',{'song':song,'rhymeList':rhymeList ,'word':word})
        else:
            song=""
            rhymeList=[]
            return render_to_response('home.html',{'song':song,'rhymeList':rhymeList})

    elif 'synonyms' in request.GET:
        song=request.GET['MySong']
        if not song=="":
            tmp=song.split('\n')
            tmp=" ".join(tmp).split('\r')
            tmp="".join(tmp).split(' ')
            tmp = find_rhyme.DeletBlancks(tmp)
            word=tmp[len(tmp)-1]+' synonyms'
            rhymeList=find_rhyme.Find_synonyms(tmp[len(tmp)-1])

            return render_to_response('home.html',{'song':song,'rhymeList':rhymeList ,'word':word})
        else:
            song=""
            rhymeList=[]
            return render_to_response('home.html',{'song':song,'rhymeList':rhymeList})

    else:
        song=""
        rhymeList=[]
        return render_to_response('home.html',{'song':song,'rhymeList':rhymeList})


def aboutUs(request):
        return render_to_response('aboutUs.html')