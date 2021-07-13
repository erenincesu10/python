


import re

#usually returns search results after searching
#making a search with re module expressions

#result = dir(re)

str = "Python kursu : Python programlama rehberi | 40 saat"

#re.findall()

#result = re.findall("Python",str)
#result = len(result)

#re.split()

#result = re.split(" ",str)
#result = re.split("r",str)

#re.sub()

#result = re.sub(" ","-",str)
#result = re.sub("\s","-",str)

#re.search()

#result = re.search("Python",str)#first Python word

#result = result.span()
#result = result.start()
#result = result.end()
#result = result.group()
#result = result.string

"""
    [] - searched all characters that between the []
        
        [abc] => a      : 1 match
                 ac     : 2 match
                 Python : No matches
                 
        [a-e] => [abcde]
        [1-5] => [12345]
        [0-39] => [01239]
        
        [^abc] => all chars out of a
        [^0-9] => non-digit chars
        
"""

#result = re.findall("[abc]",str)
#result = re.findall("[sat]",str)
#result = re.findall("[a-e]",str)
#result = re.finall("[^0-9]",str)
#print(result)

"""
        . - specifies any single char
            
            .. => a     : No match
                  ab    : 1 match
                  abc   : 1 match
                  abcd  : 2 matches

"""

#result = re.findall("...",str)
#result = re.findall("Py..on",str)

"""
    ^ - is the string starting with specified chars ?
    
    ^a  => a: 1 match
           abc : 1 match
           bac : No match

"""
#result = re.findall("^P",str)

"""
    $ - is the string ending with specified chars ? 
    
    a$ => a     : 1 match
          lambda : 1 match
          Python : No match

"""
#result = re.findall("t$",str)

"""
     * - checks if a char is zero or more
     
        ma*n => mn      : 1 match
                man     : 1 match
                maaan   : 1 match
                main    : No match (n is not coming to a's behind)

"""

#result = re.findall("sa*t",str)

"""
    + - checks if a char is one or more
    
        ma+n => mn      : No match
                man     : 1 match
                maaan   : 1 match
                main    : No match (n is not coming to a's behind)

"""

#result = re.findall("sa+t",str)

"""
     ? - checks if a char occurs zero or once

        ma?n => mn      : No match
                man     : 1 match
                maaan   : 1 match
                main    : No match (n is not coming to a's behind)

"""
#result = re.findall("sa?t",str)
"""
     {} - checks the char number

        al{2} => The "l" character must be repeated 2 times after the "a" character.
        al{2,3} => The "l" character must be repeated min 2 times max 3 times after the "a" character.
        [0-9]{2-4} => min 2 max 4 digits numbers

"""

#result = re.findall("a{2}",str)
#result = re.findall("[0-9]{2}",str)

"""
     | - one of the alternative options must be realized.

        a|b => a or b
            cde => no match
            ade => 1 match
            acdbea => 3 match
"""
"""
     () - uses for gruping

        (a|b|c)xz => xz must comes to behind a,b,c characters
"""

"""
     \ - allows us to search for special characters
        \$a => searches "a" char to behind "$" char.
               so "$" is not interpreted by the regular expression engine
               
     \A - Is the specified char in the start of the string?
          \A the  => Is the "the" in the start of the string ?
          
     \Z - Is the specified char in the end of the string?
          the\Z  => Is the "the" in the end of the string ?
     
     \b - Is the specified char in the start or in the end of the string?
          \bthe  => Is the "the" in the start of the string ?
          the\b  => Is the "the" in the end of the string ?
          
     \B - Is not the specified char in the start or in the end of the string?
          \Bthe  => Is not the "the" in the start of the string ?
          the\B  => Is not the "the" in the end of the string ?
          
     \d - same means with the [0-9]. So searches the numbers.
          \d => 12abc34
          
     \D - same means with the [^0-9]. So searches the non-digits
          \D => 1ab44_50
     
     \s - searches to " " characters.
     \S - out of " " characters
     \w - alphabetical chars, numbers and "_" chars
     \W - opposite of "\w"
     
"""

