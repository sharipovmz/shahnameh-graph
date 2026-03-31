import xml.etree.ElementTree as ET

namespaces = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
}

tree = ET.parse('docx_unpacked/word/document.xml')
root = tree.getroot()

body = root.find('w:body', namespaces)

for p in body.findall('w:p', namespaces)[:30]:
    pPr = p.find('w:pPr', namespaces)
    rPr = p.find('.//w:rPr', namespaces)
    
    text = "".join([t.text for t in p.findall('.//w:t', namespaces) if t.text])
    if not text.strip():
        continue
        
    print(f"Text: {text[:50]}...")
    
    if pPr is not None:
        style = pPr.find('w:pStyle', namespaces)
        if style is not None:
            print(f"  Style: {style.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val')}")
            
        jc = pPr.find('w:jc', namespaces)
        if jc is not None:
            print(f"  Alignment: {jc.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val')}")
            
        ind = pPr.find('w:ind', namespaces)
        if ind is not None:
            firstLine = ind.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}firstLine')
            print(f"  Indent first line: {firstLine}")
            
        spacing = pPr.find('w:spacing', namespaces)
        if spacing is not None:
            line = spacing.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}line')
            lineRule = spacing.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}lineRule')
            print(f"  Line spacing: {line} ({lineRule})")
            
    if rPr is not None:
        fonts = rPr.find('w:rFonts', namespaces)
        if fonts is not None:
            print(f"  Font: {fonts.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}ascii')}")
        sz = rPr.find('w:sz', namespaces)
        if sz is not None:
            print(f"  Size: {int(sz.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val'))/2} pt")
        b = rPr.find('w:b', namespaces)
        if b is not None:
            print(f"  Bold: True")

# Also get page margins
sectPr = body.find('.//w:sectPr', namespaces)
if sectPr is not None:
    pgMar = sectPr.find('w:pgMar', namespaces)
    if pgMar is not None:
        top = pgMar.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}top')
        bottom = pgMar.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}bottom')
        left = pgMar.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}left')
        right = pgMar.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}right')
        # Twips to cm: 1 cm = 567 twips
        print(f"\nMargins:")
        print(f"  Top: {int(top)/567:.2f} cm")
        print(f"  Bottom: {int(bottom)/567:.2f} cm")
        print(f"  Left: {int(left)/567:.2f} cm")
        print(f"  Right: {int(right)/567:.2f} cm")

