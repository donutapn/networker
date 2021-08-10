# networker
- Web pen-testing with Networker!
- For Education

# Usage
>> help

to see all command
>> status

to view all setting
>> show -t

to show all running(run slower but less error)
>> show -f

show only the thing you want(easy to see but easy to error too)(default is False)
>> status

to see all setting
- First Step
>> url http://example.com/

The first ,you should set URL
- View page source
>> src
- Find web path
>> wrdlst wordlist.txt

set wordlist (default is common.txt)
>> grep word

to set the word you find if you didn't set grep, it find all path or directories
>> run

to start find path and sub directories
>> srun

to find only path but less error
- Add key value
>> req -g

to request as GET or
>> req -p

to request as POST(default is GET)
>> key key1 value1

>> key key2 value2

>> key key3 value3

to add key value
>> src

to view page source
- Brute force key value
>> req -g

to request as GET or
>> req -p

to request as POST(default is GET)
>>bkey key1 wordlist.txt

>>bkey key2 wordlist.txt

>>bkey key3 wordlist.txt

to add wordlist to brute force key
>>bf

to brute force and find the result

- Reset setting
>> key reset

>> bkey reset

>> grep reset
