import requests
import time

time.sleep(0.3)
print('************************************')
time.sleep(0.3)
print('*                                  *')
time.sleep(0.3)
print('*   Welcome to Net Worker 1.1      *')
time.sleep(0.3)
print('*   Create by Apinut Chompoonuch   *')
time.sleep(0.3)
print('*   Use "help" to see command      *')
time.sleep(0.3)
print('*                Be nice!          *')
time.sleep(0.3)
print('*                                  *')
time.sleep(0.3)
print('************************************')

def path(url,w):
    if w != '':
        pathurl = url+(w.strip())+'/'
        indexweb = requests.get(pathurl[:-1])
        indexhtml = indexweb.text
        web = requests.get(pathurl)
        if show_all == True:
            print(pathurl[:-1])
        html = web.text
        if '//' in pathurl[6:]:
            pass
        else:
            if grep == '':
                if '<title>404 Not Found</title>' not in indexhtml and '<title>403 Forbidden</title>' not in indexhtml and indexhtml != html:
                    print('FOUND  :  '+pathurl[:-1])
                if '<title>404 Not Found</title>' not in html and '<title>403 Forbidden</title>' not in html:
                    print('FOUND  :  '+pathurl)
                    zlist = open(wrdlst,'r')
                    for z in zlist:
                        try:
                            path(pathurl,z)
                        except OSError as e:
                            pass
            else:
                if indexhtml.find(grep) > 0  and indexhtml != html:
                    print('FOUND  :  '+pathurl[:-1])
                if html.find(grep) > 0:
                    print('FOUND  :  '+pathurl)
                    zlist = open(wrdlst,'r')
                    for z in zlist:
                        try:
                            path(pathurl,z)
                        except OSError as e:
                            pass
    else:
        web = requests.get(url)
        html = web.text
        if show_all == True:
            print(url)
        if grep == '':
            if '<title>404 Not Found</title>' not in html and '<title>403 Forbidden</title>' not in html:
                print('FOUND  :  '+url)
        else:
            if html.find(grep) > 0:
                print('FOUND  :  '+url)


def getbrute(url,list_key,count):
    if count == len(list_key):
        return
    key = list_key[count]
    wrdlst = bcookies[key]
    wl = open(wrdlst,'r')
    for w in wl:
        w = w.strip()
        bfurl = url+key+'='+w
        if count == len(list_key)-1:
            bfweb = requests.get(bfurl)
            bfhtml = bfweb.text
            if len(bfhtml) - len(html) > len(w) or len(html) - len(bfhtml) > len(w):
                print('FOUND  :  '+bfurl+'\n')
                print(bfhtml)
            else:
                if show_all == True:
                    print(bfurl)
        new_count = count+1
        nexturl = bfurl+'&'
        getbrute(nexturl,list_key,new_count)

def postbrute(url,list_key,count):
    if count == len(list_key):
        return
    key = list_key[count]
    wrdlst = bcookies[key]
    wl = open(wrdlst,'r')
    for w in wl:
        w = w.strip()
        bfcook.update({key:w})
        if count == len(list_key)-1:
            bfweb = requests.post(url,bfcook)
            bfhtml = bfweb.text
            if len(bfhtml) - len(html) > len(w) or len(html) - len(bfhtml) > len(w):
                print('FOUND  :  ',bfcook,'\n')
                print(bfhtml)
            else:
                if show_all == True:
                    print(bfcook)
        new_count = count+1
        postbrute(url,list_key,new_count)
            

show_all = False
wrdlst = 'common.txt'
url = ''
req = 'GET'
cookies = {}
bcookies = {}
grep = ''

while True:
    inp = input('>>')
    key = str(inp).strip().lower()
    if key == 'help':
        print('***Use these key to command***\n')
        print('url [ip]            To set URL to you want to action with')
        print('                    (url http://[url or ip address]/)')
        print('wrdlst [file]       To set wordlist to brute force or to find path')
        print('show (-t/-f)        To show all path or all word that was finding')
        print('                    (-t = true/-f = false)(-t may be run slower but less Error)')
        print('req (-g/-p)         To request as GET or POST(-g = GET/-p = post)')
        print('key [key] [word]    To add key value')
        print('key reset           To reset all key value')
        print('bkey [key] [file]   To set wordlist to brute force key')
        print('bkey reset          To reset all wordlist to brute force key\n')
        print('grep [word]         To set word you find in each path that is finding')
        print('grep reset          To reset the word you find')
        print('src                 To view page source')
        print('run                 To start find path(without key)')
        print('srun                To start find path without directory(less Error)')
        print('bf                  To brute force key')
        print('status              To show all setting')
        print('\nexit                To end this program')
    elif key == 'src':
        try:
            if req == 'GET':
                geter = ''
                for i in cookies:
                    geter += (i+'='+cookies[i])
                    geter += '&'
                geter = geter[:-1]
                web = requests.get(url+'?'+geter)
                html = web.text
                print(html)
            else:
                web = requests.post(url,cookies)
                html = web.text
                print(html)
        except requests.exceptions.MissingSchema as e:
            print('Wrong URL!!!',url)
    elif key == 'srun':
        try:
            wlist = open(wrdlst,'r')
            if url[-1] == '/':
                runurl = url
            else:
                runurl = url+'/'
            for w in wlist:
                try:
                    if w != '':
                        pathurl = runurl+(w.strip())+'/'
                        indexweb = requests.get(pathurl[:-1])
                        indexhtml = indexweb.text
                        web = requests.get(pathurl)
                        if show_all == True:
                            print(pathurl[:-1])
                        html = web.text
                        if '//' in pathurl[6:]:
                            pass
                        else:
                            if grep == '':
                                if '<title>404 Not Found</title>' not in indexhtml and '<title>403 Forbidden</title>' not in indexhtml and indexhtml != html:
                                    print('FOUND  :  '+pathurl[:-1])
                                if '<title>404 Not Found</title>' not in html and '<title>403 Forbidden</title>' not in html:
                                    print('FOUND  :  '+pathurl)
                            else:
                                if indexhtml.find(grep) > 0  and indexhtml != html:
                                    print('FOUND  :  '+pathurl[:-1])
                                if html.find(grep) > 0:
                                    print('FOUND  :  '+pathurl)
                    else:
                        web = requests.get(runurl)
                        html = web.text
                        if show_all == True:
                            print(url)
                        if grep == '':
                            if '<title>404 Not Found</title>' not in html and '<title>403 Forbidden</title>' not in html:
                                print('FOUND  :  '+runurl)
                        else:
                            if html.find(grep) > 0:
                                print('FOUND  :  '+runurl)
                except OSError as e:
                    print('Error!!! Please reset URL or restart program.')
                    break  
        except IndexError as e:
            print('Wrong URL!!!',url)
        except requests.exceptions.MissingSchema as e:
            print('Wrong URL!!!',url)
        except FileNotFoundError as e:
            print('Wrong Wordlist!!!',wrdlst)
    elif key == 'run':
        try:
            wlist = open(wrdlst,'r')
            if url[-1] == '/':
                runurl = url[:-1]
            else:
                runurl = url
            for w in wlist:
                try:
                    path(runurl,w)
                except OSError as e:
                    print('Error!!! Please reset URL or restart program.')
                    break
        except IndexError as e:
            print('Wrong URL!!!',url)
        except requests.exceptions.MissingSchema as e:
            print('Wrong URL!!!',url)
        except FileNotFoundError as e:
            print('Wrong Wordlist!!!',wrdlst)
    elif key == 'bf':
        if req == 'GET':
            geter = ''
            for i in cookies:
                geter += (i+'='+cookies[i])
                geter += '&'
            geter = geter[:-1]
            if len(geter) > 0:
                geturl = url+'?'+geter+'&'
            else:
                geturl = url+'?'
        list_key = []
        bfcook = cookies
        for j in bcookies:
            list_key.append(j)
        count = 0
        try:
            if len(list_key) == 0:
                print('bkey [key] [file]   To set wordlist to brute force key')
            elif req == 'GET':
                web = requests.get(geturl)
                html = web.text
                getbrute(geturl,list_key,count)          
            else:
                web = requests.post(url)
                html = web.text
                postbrute(url,list_key,count)   
        except requests.exceptions.MissingSchema as e:
            print('Wrong URL!!!',url)
        except FileNotFoundError as e:
            print("Wrong Wordlist!!! in bruteforce key's value")
        except requests.exceptions.ConnectionError as e:
            print('Stop finding...')
        except OSError as e:
            print('Stop finding...')
    elif key == 'key reset':
        cookies = {}
        print('Your key was reset')
        print('Key =',cookies)
    elif key == 'bkey reset':
        bcookies = {}
        print('Your wordlist to brute force key was reset')
        print('Brute force key =',bcookies)
    elif key[:3] == 'key':
        if len(key) == 3:
            print('key [key] [word]  To add key value')
        elif key[3] == ' ':
            inplist = key.split(' ')
            if len(inplist) == 3:
                cook = inplist[1]
                word = inplist[2]
                cookies[cook] = word
                print('Key =',cookies)
            else:
                print('key [key] [word]  To add key value')
        else:
            print('no command "'+ inp +'"\nTry to use "help" to see command')
    elif key[:4] == 'bkey':
        if len(key) == 4:
            print('bkey [key] [file] To set wordlist to brute force key')
        elif key[4] == ' ':
            inplist = key.split(' ')
            if len(inplist) == 3:
                cook = inplist[1]
                word = inplist[2]
                bcookies[cook] = word
                print('Brute force key =',bcookies)
            else:
                print('bkey [key] [file] To set wordlist to brute force key')
        else:
            print('no command "'+ inp +'"\nTry to use "help" to see command')
    elif key[:6] == 'wrdlst':
        if len(key) == 6:
            print('wrdlst [file]  To set wordlist to brute force or to find path')
        elif key[6] == ' ':
            wrdlst = key[7:]
            print('Wordlist = '+wrdlst)
        else:
            print('no command "'+ inp +'"\nTry to use "help" to see command')
    elif key[:3] == 'url':
        if len(key) == 3:
            print('url [ip]       To set URL to you want to action with(http://[url or ip address]/)')
        elif key[3] == ' ':
            url = key[4:]
            print('URL = '+url)
        else:
            print('no command "'+ inp +'"\nTry to use "help" to see command')
    elif key[:4] == 'show':
        if len(key) == 4:
            print('show (-t/-f)  To show all path or all word that was finding(-t = true/-f = false)("-t" may be run slower)')
        elif key[4] == ' ':
            if key[5:] == '-t':
                show_all = True
                print('Show all running = True(may be run slower)')
            elif key[5:] == '-f':
                show_all = False
                print('Show all running = False')
            else:
                print("Use -t to show all path or all word that was finding or -f to don't show")
        else:
            print('no command "'+ inp +'"\nTry to use "help" to see command')
    elif key[:3] == 'req':
        if len(key) == 3:
            print('req (-g/-p)    To request as GET or POST(-g = GET/-p = post)')
        elif key[3] == ' ':
            if key[4:] == '-g':
                req = 'GET'
                print('Request as = GET')
            elif key[4:] == '-p':
                req = 'POST'
                print('Request as = POST')
            else:
                print("Use -g to request as GET or -p to as POST")
        else:
            print('no command "'+ inp +'"\nTry to use "help" to see command')
    elif key == 'grep reset':
        grep = ''
        print('The word you find was reset')
        print('The word you find = '+grep)
    elif key[:4] == 'grep':
        if len(key) == 4:
            print('grep [word]         To set word you find')
        elif key[4] == ' ':
            grep = key[5:]
            print('The word you find = '+grep)
        else:
            print('no command "'+ inp +'"\nTry to use "help" to see command')
    elif key == 'status':
        print('URL or IP address = '+url)
        print('Wordlist          = '+wrdlst)
        print('Request as        = '+req)
        print('Key               =',cookies)
        print('Brute force key   =',bcookies)
        print('Show all running  =',show_all)
        print('The word you find = '+grep)
    elif key == 'exit':
        print('closing',end = '')
        time.sleep(0.3)
        for i in range(3):
            time.sleep(0.3)
            print('.',end = '')
        break
    else:
        print('no command "'+ inp +'"\nTry to use "help" to see command')
