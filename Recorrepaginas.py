import pdfplumber as pdfp

#Esta funcion recorre todas las paginas del PDF y las guarda con su texto íntegro en una lista, por cada mitad de pagina.
def TextoCompleto(File):
    print(File)
    ListOut=[]
    i=0
    with pdfp.open(File) as pdf:
        Num=0
        for page in pdf.pages:

#cropea las paginas por la mitad porque sino lo lee linea por linea ; codigo extraido de https://stackoverflow.com/questions/55100037/how-to-extract-text-from-two-column-pdf-with-python
            i=i+1
            width = page.width
            height = page.height
            left_bbox = (0*float(width), 0.1*float(height), 0.5*float(width), 0.95*float(height))
            page_crop = page.crop(left_bbox)
            left_text = page_crop.extract_text()
            left_bbox = (0.5*float(width), 0.1*float(height), 1*float(width), 0.95*float(height))
            page_crop = page.crop(left_bbox)
            right_text = page_crop.extract_text()

            if i==1:
                upper_bbox=(0*float(width), 0*float(height), 0.25*float(width), 0.08*float(height))
                page_crop= page.crop(upper_bbox)
                upper_text=page_crop.extract_text()

                grupo= upper_text

            ListOut.append(left_text)
            ListOut.append(right_text)
            
    print("Páginas Extraidas",i)
    return (ListOut, grupo)
