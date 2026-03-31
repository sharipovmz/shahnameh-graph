import xml.etree.ElementTree as ET
namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
tree = ET.parse('docx_unpacked/word/document.xml')
tables = tree.getroot().findall('.//w:tbl', namespaces)
if tables:
    for row in tables[0].findall('.//w:tr', namespaces)[:2]:
        for cell in row.findall('.//w:tc', namespaces)[:2]:
            p = cell.find('.//w:p', namespaces)
            if p is not None:
                text = "".join([t.text for t in p.findall('.//w:t', namespaces) if t.text])
                pPr = p.find('w:pPr', namespaces)
                rPr = p.find('.//w:rPr', namespaces)
                jc = pPr.find('w:jc', namespaces) if pPr is not None else None
                sz = rPr.find('w:sz', namespaces) if rPr is not None else None
                b = rPr.find('w:b', namespaces) if rPr is not None else None
                print(f"Cell text: {text}")
                print(f"  Align: {jc.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val') if jc is not None else 'Default'}")
                print(f"  Size: {int(sz.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val'))/2 if sz is not None else 'Default'} pt")
                print(f"  Bold: {b is not None}")
