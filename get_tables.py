import xml.etree.ElementTree as ET
namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
tree = ET.parse('docx_unpacked/word/document.xml')
for tbl in tree.getroot().findall('.//w:tbl', namespaces)[:1]:
    for p in tbl.findall('.//w:p', namespaces)[:2]:
        text = "".join([t.text for t in p.findall('.//w:t', namespaces) if t.text])
        pPr = p.find('w:pPr', namespaces)
        rPr = p.find('.//w:rPr', namespaces)
        sz = rPr.find('w:sz', namespaces) if rPr is not None else None
        print(f"Table text: {text[:40]}...")
        print(f"  Size: {int(sz.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val'))/2 if sz is not None else 'Default'} pt")
        spacing = pPr.find('w:spacing', namespaces) if pPr is not None else None
        if spacing is not None:
            line = spacing.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}line')
            print(f"  Spacing: {int(line)/240 if line else 'Default'}")
