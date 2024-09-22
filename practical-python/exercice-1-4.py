import urllib.request
import ssl

context = ssl._create_unverified_context()

u = urllib.request.urlopen('https://ctabustracker.com/bustime/api/v3/getpredictions?requestType=getpredictions&locale=en&stpid=14791&rtpidatafeed=bustime&top=20&key=Qskvu4Z5JDwGEVswqdAVkiA5B&format=xml&xtime=1707755378135', context=context)

from xml.etree.ElementTree import parse

doc = parse(u)
for pt in doc.findall('.//pt'):
    print(pt.text)
    
    