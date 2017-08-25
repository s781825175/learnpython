class Codec:
    def __init__(self):
        self.tinyurl=[]

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.tinyurl.append(longUrl)
        return "http://tinyurl.com/"+str(len(self.tinyurl))

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        a=list(shortUrl.split('/'))
        return self.tinyurl[(int(a[-1])-1)]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

if __name__ == '__main__':
    longUrl="https://leetcode.com/problems/design-tinyurl"
    print(Codec().encode(longUrl))
