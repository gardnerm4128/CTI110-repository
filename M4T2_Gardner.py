#Ask usr for string
tag = input("Type Tag: ")
#Tags
#if one of tags, print what tag it is, give exmpl of use
if tag == "p":
    print("p is paragraph tag")
    print("example: <p>paragraph<p>")
elif tag == "h1":
    print("h1 is header tag")
    print("example: <h1>First Header<h1>")
elif tag == "b":
    print("b is bold text tag")
    print("example: <b>Bold Text<b>")
elif tag == "div":
    print("div tag defines a division in a webpage")
    print("example: <div style='colour:000dsw'")
else:
    print("tag not found")
#else print (Tag not found)


