import xml.etree.ElementTree as ET
namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
tree = ET.parse('docx_unpacked/word/styles.xml')
for style in tree.getroot().findall('w:style', namespaces):
    style_id = style.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}styleId')
    if 'Heading' in style_id:
        sz = style.find('.//w:sz', namespaces)
        b = style.find('.//w:b', namespaces)
        jc = style.find('.//w:jc', namespaces)
        fonts = style.find('.//w:rFonts', namespaces)
        print(f"{style_id}:")
        print(f"  Size: {int(sz.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val'))/2 if sz is not None else 'Default'} pt")
        print(f"  Font: {fonts.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}ascii') if fonts is not None else 'Default'}")
        print(f"  Bold: {b is not None}")
        print(f"  Align: {jc.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val') if jc is not None else 'Default'}")
        spacing = style.find('.//w:spacing', namespaces)
        if spacing is not None:
            before = spacing.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}before')
            after = spacing.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}after')
            print(f"  Spacing: Before {before}, After {after}")
