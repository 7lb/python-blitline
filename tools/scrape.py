import re
import string
import urllib2
from datetime import datetime
from lxml import etree

def function_name(text, rex=re.compile(r'"name"\s*:\s*"([^"]+)"')):
    match = rex.search(text)
    if match:
        return match.group(1)
    return None

parser = etree.HTMLParser()
tree = etree.parse(urllib2.urlopen("http://www.blitline.com/docs/functions"), parser)

functions = tree.xpath("""//div[contains(@class, 'thumbnail')]/div""")
functions_data = []
for f in functions:
    code_nodes = f.xpath("div[contains(@class, 'hideable')]/pre")
    if not code_nodes:
        continue
    elif len(code_nodes) > 1:
        raise ValueError("HTML mismatch, too many codes")
    else:
        code = code_nodes[0].text
    fname = function_name(code)
    if not fname:
        raise ValueError("HTML mismatch, function name not found")

    doc_nodes = f.xpath("div[@class='caption']/p[contains(@class,'alert')]")
    if not doc_nodes:
        doc = ''
    elif len(doc_nodes) > 1:
        raise ValueError("HTML mismatch, too many descriptions")
    else:
        doc = doc_nodes[0].text.strip()

    functions_data.append((fname, doc))

# some functions not listed in the online page
functions_data.extend([
    ('vintage', 'Vintage Filter'),
    ('lomo', 'Lomo Filter'),
    ('photograph', 'Photograph Filter'),
    ('savannah', 'Savannah Filter'),
    ('xpro', 'Xpro Filter'),
    ('celsius', 'Celsius Filter'),
    ('stackhouse', 'Stackhouse Filter'),
])

fragments = [
    "#autogenerated on %s" % datetime.now(),
    "from blitline import Function",
]
tpl = '''
class {cname}(Function):
    """
    {doc}
    """
    function_name = "{fname}"
'''
for fname, doc in functions_data:
    cname = string.capwords(fname, '_').replace('_', '')
    fragments.append(tpl.format(cname=cname, fname=fname, doc=doc))

print '\n'.join(fragments)

