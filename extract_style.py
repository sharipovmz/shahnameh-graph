import xml.etree.ElementTree as ET

namespaces = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
}

def parse_styles(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()
    styles = {}
    
    # Get default styles
    doc_defaults = root.find('w:docDefaults', namespaces)
    if doc_defaults is not None:
        rpr = doc_defaults.find('.//w:rPrDefault/w:rPr', namespaces)
        if rpr is not None:
            sz = rpr.find('w:sz', namespaces)
            rFonts = rpr.find('w:rFonts', namespaces)
            print(f"Default Font: {rFonts.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}ascii') if rFonts is not None else 'Unknown'}")
            print(f"Default Size: {int(sz.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val'))/2 if sz is not None else 'Unknown'} pt")
            
        ppr = doc_defaults.find('.//w:pPrDefault/w:pPr', namespaces)
        if ppr is not None:
            spacing = ppr.find('w:spacing', namespaces)
            if spacing is not None:
                line = spacing.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}line')
                print(f"Default Line Spacing: {int(line)/240 if line else 'Unknown'} lines")
            
            jc = ppr.find('w:jc', namespaces)
            print(f"Default Justification: {jc.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val') if jc is not None else 'Unknown'}")

    for style in root.findall('w:style', namespaces):
        style_id = style.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}styleId')
        name = style.find('w:name', namespaces)
        name_val = name.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val') if name is not None else 'Unknown'
        
        # Check if it's a heading
        if 'heading' in style_id.lower() or name_val.startswith('heading'):
            sz = style.find('.//w:sz', namespaces)
            b = style.find('.//w:b', namespaces)
            jc = style.find('.//w:jc', namespaces)
            spacing = style.find('.//w:spacing', namespaces)
            
            sz_val = int(sz.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val'))/2 if sz is not None else 'Default'
            jc_val = jc.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val') if jc is not None else 'Default'
            
            space_before = spacing.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}before') if spacing is not None else '0'
            space_after = spacing.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}after') if spacing is not None else '0'
            
            print(f"Style: {name_val} ({style_id})")
            print(f"  Size: {sz_val} pt")
            print(f"  Bold: {b is not None}")
            print(f"  Alignment: {jc_val}")
            print(f"  Spacing Before: {space_before}, After: {space_after}")

parse_styles('docx_unpacked/word/styles.xml')
