###
# 1. create only one code for each long url
# 2. Only offers a million codes with length 6 (or smaller). Using six digits or # lower or upper case letters would offer (10+26*2)6 = 
#    56,800,235,584 codes with length 6.
###
class Codec:
    def __init__(self):
        self.code2url = {}
        self.url2code = {}
        self.alphabet = string.ascii_letters + '0123456789'
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.url2code:
            code = ''.join(random.choice(self.alphabet) for i in xrange(6))
            self.code2url[code] = longUrl
            self.url2code[longUrl] = code
        return 'http://tinyurl.com/' + self.url2code[longUrl]
       
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.code2url[shortUrl[-6:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))