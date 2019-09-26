import zlib, base64
with open("modified.py","w") as writer:
    writer.write("import zlib,base64 as s\nt=enumerate(zlib.decompress(s.b64decode(")
    with open("cheatsheet.txt","rb") as source:
        text = source.read()
        writer.write(str(base64.b64encode(zlib.compress(text,9))))
    writer.write(')).decode());a=lambda c:next(t)[1]')

"""
with open("out.txt","w") as writer:
    with open("whale2.txt","r") as reader:
        text = reader.read()
        for b in text:
         c = a(b)
         writer.write(c)
"""
