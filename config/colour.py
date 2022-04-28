class end:
    def __str__(self): return '\33[0m'

class effect:
    class bold: 
        def __str__(self): return '\33[1m'
    class italic: 
        def __str__(self): return '\33[3m'
    class url: 
        def __str__(self): return '\33[4m'
    class blink1:
        def __str__(self): return '\33[5m'
    class blink2: 
        def __str__(self): return '\33[6m'
    class select: 
        def __str__(self): return '\33[7m'

class text:
    class black  : 
        def __str__(self): return '\33[30m'
    class red    : 
        def __str__(self): return '\33[31m'
    class green  : 
        def __str__(self): return '\33[32m'
    class yellow : 
        def __str__(self): return '\33[33m'
    class blue   : 
        def __str__(self): return '\33[34m'
    class violet : 
        def __str__(self): return '\33[35m'
    class beige  : 
        def __str__(self): return '\33[36m'
    class white  : 
        def __str__(self): return '\33[37m'

class back:
    class black  : 
        def __str__(self): return '\33[40m'
    class red    : 
        def __str__(self): return '\33[41m'
    class green  : 
        def __str__(self): return '\33[42m'
    class yellow : 
        def __str__(self): return '\33[43m'
    class blue   : 
        def __str__(self): return '\33[44m'
    class violet : 
        def __str__(self): return '\33[45m'
    class beige  : 
        def __str__(self): return '\33[46m'
    class white  : 
        def __str__(self): return '\33[47m'