from PIL import Image,ImageDraw,ImageFont
import math,random,os
random.seed(9)
out=os.path.join(os.path.dirname(__file__),'assets')
W,H=480,155
stars=[(random.randrange(10,470),random.randrange(6,72)) for _ in range(38)]
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',9)
frames=[]
for t in range(16):
 im=Image.new('RGB',(W,H));d=ImageDraw.Draw(im)
 # background wall gradient
 for y in range(H):
  k=y/H;d.line((0,y,W,y),fill=(int(7+11*k),int(15+9*k),int(39+25*k)))
 # window
 d.rounded_rectangle((17,8,118,95),radius=3,fill='#0a1231',outline='#37548a',width=3)
 d.rectangle((25,14,110,85),fill='#07152c')
 for i,(x,y) in enumerate(stars):
  if 24<x<110 and 15<y<80 and (i+t//3)%5!=0:d.rectangle((x,y,x+1,y+1),fill='#bddbff')
 d.ellipse((74,24,95,45),fill='#d6edff');d.ellipse((82,19,101,41),fill='#07152c')
 for x,h in [(26,20),(39,31),(58,18),(80,23),(100,29)]:d.rectangle((x,84-h,x+12,84),fill='#14284c')
 # shelving with plant books
 d.rectangle((360,33,463,37),fill='#6c4975');d.rectangle((370,18,377,33),fill='#6472a7');d.rectangle((379,15,389,33),fill='#b678ad');d.rectangle((392,19,401,33),fill='#38b7c9')
 d.rectangle((9,40,45,44),fill='#614e87')
 for q in range(7):
  xx=14+(q*7)%29;yy=7+(q*9)%35;d.rectangle((xx,yy,xx+7,yy+5),fill=['#215b57','#307b6d','#397f85'][q%3])
 # neon AI panel
 d.rectangle((405,54,458,100),fill='#121735',outline='#754ec4',width=2)
 d.ellipse((422,66,441,85),outline='#bc83ff',width=2)
 d.line((430,65,430,85),fill='#bc83ff',width=2)
 # desk
 d.rectangle((0,112,480,122),fill='#302346');d.rectangle((0,112,480,115),fill='#9364a2')
 d.rectangle((33,123,42,154),fill='#1d1d3c');d.rectangle((438,123,448,154),fill='#1d1d3c')
 # monitor and code
 d.rounded_rectangle((145,28,327,111),radius=6,fill='#091128',outline='#347cdb',width=4)
 d.rectangle((152,35,320,104),fill='#0b1f38')
 d.rectangle((152,35,320,45),fill='#162f54')
 for i in range(3): d.ellipse((158+i*8,39,161+i*8,42),fill=['#ff7bae','#ffc981','#75dede'][i])
 for j in range(11):
  yy=50+j*5;length=18+((j*17+t*3)%77);x=162+((j%3)*12)
  d.rectangle((x,yy,x+length,yy+2),fill=['#5dd7eb','#a28bff','#f8a7da','#456dae'][j%4])
  if j%3==1:d.rectangle((x+length+4,yy,x+length+16,yy+2),fill='#edc583')
 # cpu box
 d.rectangle((347,76,389,112),fill='#151b37',outline='#5367a2',width=2)
 for i in range(3):d.rectangle((353+i*8,103,357+i*8,105),fill='#52ffd2' if (t+i)%4 else '#186653')
 # small laptop left
 d.polygon([(53,80),(120,80),(126,112),(46,112)],fill='#1d3766');d.rectangle((58,83,118,106),fill='#123153')
 d.text((65,90),'hello, ai!',font=font,fill='#65e8d5')
 # girl shoulder silhouette hoodie
 d.ellipse((217,81,293,158),fill='#6b4d9d')
 d.polygon([(223,100),(206,143),(238,154),(258,115)],fill='#7756b5')
 d.polygon([(285,99),(309,140),(288,154),(270,120)],fill='#5f4697')
 # hair with bun
 d.ellipse((232,49,282,104),fill='#25142e')
 d.ellipse((249,39,280,68),fill='#25142e')
 d.rectangle((237,88,276,105),fill='#25142e')
 # face profile right
 d.polygon([(273,69),(287,79),(283,91),(274,95)],fill='#e6a2a0')
 # earphones
 d.ellipse((261,76,281,96),fill='#7045be',outline='#a77afe',width=3)
 d.text((263,80),'<>',font=font,fill='#b8f3ff')
 # mug & cat
 d.rectangle((332,100,349,113),fill='#d887b3');d.arc((343,99,355,110),-90,90,fill='#d887b3',width=2)
 for p in range(2):
  sy=(t+p*4)%13;d.point((337+p*5,93-sy),fill='#ffdbed')
 d.ellipse((68,114,100,127),fill='#dccce6');d.polygon([(73,115),(78,106),(85,114)],fill='#dccce6');d.polygon([(91,115),(97,107),(99,119)],fill='#dccce6')
 d.line((78,120,82,120),fill='#6c5a80');d.line((89,120,93,120),fill='#6c5a80')
 # plant floor
 d.rectangle((451,107,468,122),fill='#995574')
 for j in range(7):
  x=459+int(7*math.sin(j*1.8));y=103-j*7
  d.line((459,111,x,y),fill='#287e80',width=2);d.ellipse((x-4,y-2,x+4,y+3),fill='#339e82')
 # small text top
 d.text((344,133),'BUILD  |  LEARN  |  CREATE',font=font,fill='#8a95c7')
 # glowing monitor light subtly via palette accents
 frames.append(im.resize((960,310),Image.Resampling.NEAREST))
frames[0].save(os.path.join(out,'coding-night.gif'),save_all=True,append_images=frames[1:],duration=110,loop=0,optimize=False,disposal=2)
frames[0].save(os.path.join(out,'coding-night-preview.png'))
print('GIF saved')
