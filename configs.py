'''
configs.py
'''

class ChainDict(dict):
    '''
    if we look up a setting in the settings variable
    and it doesn't exist, instead of throwing a KeyError
    we will look into the defaults variable instead
    (fallback dictionary)
    '''
    def __init__(self, fallback, *args, **kwargs):
        #args is a tuple, in order of additional arguments
        #kwargs is a dictionary, keyword > value pairs
        #Then we send those args to the dictionary class (parent)
        #dict.__init__(self, *args, **kwargs)
        self.fallback = fallback
        # self.update allows us to send the arguments to the
        # dictionary # __init__
        self.update(*args, **kwargs)

    def __missing__(self, key):
        #import pdb; pdb.set_trace() #Puts you in python debugger during an exception
        return self.fallback[key]

defaults = {'bg': 'black', 'fg': 'green', 'h': 40}
settings = ChainDict(defaults, {'fg': 'cyan', 'h': 80})
user = ChainDict(settings, {'fg': 'magenta'})

