import xml.etree.ElementTree as ET
namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
tree = ET.parse('docx_unpacked/word/document.xml')
for p in tree.getroot().findall('.//w:p', namespaces):
    text = "".join([t.text for t in p.findall('.//w:t', namespaces) if t.text])
    if text.startswith('Расми') or text.startswith('Таблица') or text.startswith('Ҷадвали'):
        pPr = p.find('w:pPr', namespaces)
        rPr = p.find('.//w:rPr', namespaces)
        
        style = pPr.find('w:pStyle', namespaces) if pPr is not None else None
        jc = pPr.find('w:jc', namespaces) if pPr is not None else None
        sz = rPr.find('w:sz', namespaces) if rPr is not None else None
        b = rPr.find('w:b', namespaces) if rPr is not None else None
        
        print(f"Caption: {text[:40]}...")
        print(f"  Style: {style.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val') if style is not None else 'None'}")
        print(f"  Align: {jc.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val') if jc is not None else 'None'}")
        print(f"  Size: {int(sz.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val'))/2 if sz is not None else 'Default'} pt")
        print(f"  Bold: {b is not None}")
