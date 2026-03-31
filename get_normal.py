import xml.etree.ElementTree as ET
namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
tree = ET.parse('docx_unpacked/word/styles.xml')
for style in tree.getroot().findall('w:style', namespaces):
    if style.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}styleId') == 'Normal':
        sz = style.find('.//w:sz', namespaces)
        fonts = style.find('.//w:rFonts', namespaces)
        print(f"Normal Size: {int(sz.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val'))/2 if sz is not None else 'Default'} pt")
        print(f"Normal Font: {fonts.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}ascii') if fonts is not None else 'Default'}")
