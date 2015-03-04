import csv

def write_footprint(s,codigo):
     name='Leaded_Varistor_StandarD_Series-'+'S'+codigo[4:6]+'K'+str(int(codigo[8:10])*10**int(codigo[10]))
     f=open('SIOV.pretty/'+name+'.kicad_mod','w')
     f.write(s)
     f.close()
def encabezado(codigo,x,y,descripcion,tags,reference,Rx,Ry,Vx,Vy):
    name='Leaded_Varistor_StandarD_Series-'+'S'+codigo[4:6]+'K'+str(int(codigo[8:10])*10**int(codigo[10]))
    #f=open('SIOV.pretty/'+name+'.mod','w')
    s="""(module {0} (layer F.Cu)
  (at {1:.2f} {2:.2f})
  (descr "{3}")
  (tags "{4}")
  (fp_text reference {5} (at {6:.2f} {7:.2f}) (layer F.SilkS)
    (effects (font (thickness 0.15)))
  )
  (fp_text value {0} (at {8:.2f} {9:.2f}) (layer F.SilkS)
    (effects (font (thickness 0.15)))
  )""".format(name,x,y,descripcion,tags,reference,Rx,Ry,Vx,Vy)
    #s='(module {0} (layer F.Cu)'.format(name)
    s+='\n'
    #s+='  (at 0 0)'
    
    #f.write(s)
    #f.close()
    return s
#def add_description(s,decription):
def draw_line(Xi,Xf,Yi,Yf):
    s='  (fp_line (start {0:.2f} {1:.2f}) (end {2:.2f} {3:.2f}) (layer F.SilkS) (width 0.15))'.format(Xi,Yi,Xf,Yf)
    s+='\n'
    return s
def add_pad_thru_hole(pad,x,y,sizeX,sizeY,drill):
    s='  (pad {0} thru_hole circle (at {1:.2f} {2:.2f}) (size {3:.2f} {4:.2f}) (drill {5:.2f}) (layers *.Cu *.Mask F.SilkS))'.format(pad,x,y,sizeX,sizeY,drill)
    s+='\n'
    return s
with open('siov_dimension.csv') as csvfile:
          spamreader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
          for row in spamreader:
              #codigo=row[0]
              width=float(row[3])
              th=float(row[4])
              x=float(row[1])/2
              y=float(row[2])/2
              hole=float(row[7])
              anchorX=x
              anchorY=y
              description="Varistor, Vrms="+row[9]+"V, Vdc="+row[10]+"V, Imax="+row[11]+"A"
              content= encabezado(row[0],0,0,description,"","VAR",anchorX,anchorY+th/2+1,anchorX,anchorY-th/2-1)
              
              content+=draw_line(anchorX-width/2,anchorX+width/2,anchorY+th/2,anchorY+th/2)
              content+=draw_line(anchorX-width/2,anchorX+width/2,anchorY-th/2,anchorY-th/2)
              content+=draw_line(anchorX+width/2,anchorX+width/2,anchorY-th/2,anchorY+th/2)
              content+=draw_line(anchorX-width/2,anchorX-width/2,anchorY-th/2,anchorY+th/2)
              
              content+=add_pad_thru_hole(1,anchorX-x,anchorY-y,hole+1,hole+1,hole)
              content+=add_pad_thru_hole(2,anchorX+x,anchorY+y,hole+1,hole+1,hole)
              #content+='\n'
              content+=')'
              #print(content)
              write_footprint(content,row[0])
              #break
              #description=""
              #tags=""
              #s+='(descr "{0}")'.format(description)
              #s+='(tags "{0}")'.format(description)
              #s+
              #print(name)