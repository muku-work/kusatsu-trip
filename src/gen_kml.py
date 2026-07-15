C = {
 "大東館": (36.62083,138.59583),
 "湯畑": (36.62194,138.59667),
 "西の河原通り": (36.62306,138.59250),
 "西の河原露天風呂": (36.62306,138.58944),
 "裏草津 地蔵の湯": (36.62139,138.59750),
 "白旗の湯": (36.62222,138.59639),
 "熱乃湯": (36.62222,138.59611),
 "大滝乃湯": (36.61972,138.60028),
 "草津温泉バスターミナル": (36.62472,138.59500),
}
DAYLABEL={"7/18":"1日目","7/19":"2日目"}

def kml(fname, title, days):
    b=['<?xml version="1.0" encoding="UTF-8"?>',
       '<kml xmlns="http://www.opengis.net/kml/2.2"><Document>',
       f'<name>{title}</name>']
    colors={"7/18":"ff2dc0ff","7/19":"ffe6944b"}
    for day, stops in days:
        dl=DAYLABEL[day]
        b.append(f'<Folder><name>{dl}（{day}）</name>')
        line=[]
        for spot,activity in stops:
            lat,lng=C[spot]
            b.append(f'<Placemark><name>{dl}-{spot}</name>'
                     f'<description>{activity}</description>'
                     f'<Point><coordinates>{lng},{lat},0</coordinates></Point></Placemark>')
            line.append(f'{lng},{lat},0')
        b.append(f'<Placemark><name>{dl} ルート</name>'
                 f'<Style><LineStyle><color>{colors[day]}</color><width>4</width></LineStyle></Style>'
                 f'<LineString><tessellate>1</tessellate><coordinates>{" ".join(line)}</coordinates></LineString></Placemark>')
        b.append('</Folder>')
    b.append('</Document></kml>')
    open(fname,"w",encoding="utf-8").write("\n".join(b))

machiaruki=[
 ("7/18",[
   ("大東館","荷物を預けて出発"),
   ("湯畑","昼食（居酒屋 水穂の手打ちうどん）"),
   ("西の河原通り","街歩き・食べ歩き"),
   ("西の河原露天風呂","日帰り温泉（大露天風呂・800円）"),
   ("裏草津 地蔵の湯","裏草津の街歩き（足湯・顔湯・目洗い地蔵）"),
   ("白旗の湯","共同浴場めぐり（無料）"),
   ("大東館","夕食・宿泊"),
 ]),
 ("7/19",[
   ("大東館","チェックアウト"),
   ("西の河原通り","朝の街歩き"),
   ("裏草津 地蔵の湯","共同浴場でひと風呂・裏草津散策（無料）"),
   ("湯畑","昼食＆お土産購入（本家ちちや）"),
   ("草津温泉バスターミナル","14:15 集合"),
 ]),
]

gourmet=[
 ("7/18",[
   ("大東館","荷物を預けて出発"),
   ("湯畑","昼食（湯畑 草庵の草津温泉バーガー）＋食べ歩き"),
   ("西の河原露天風呂","日帰り温泉でクールダウン（800円）"),
   ("熱乃湯","湯もみショー観覧（700円）"),
   ("裏草津 地蔵の湯","裏草津の街歩き・カフェ月の貌でスイーツ"),
   ("大東館","夕食・宿泊"),
 ]),
 ("7/19",[
   ("大東館","チェックアウト"),
   ("大滝乃湯","日帰り温泉（名物の合わせ湯）"),
   ("裏草津 地蔵の湯","裏草津の路地を散策"),
   ("湯畑","昼食＆お土産（温泉まんじゅう食べ比べ）"),
   ("草津温泉バスターミナル","14:15 集合"),
 ]),
]

kml("output/maps/草津_街歩き重視_ルート.kml","草津温泉 街歩き重視 散策ルート",machiaruki)
kml("output/maps/草津_グルメ重視_ルート.kml","草津温泉 グルメ重視 散策ルート",gourmet)
print("done")
