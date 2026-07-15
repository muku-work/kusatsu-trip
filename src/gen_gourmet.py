C = {
 "大東館": (36.62083,138.59583),
 "湯畑": (36.62194,138.59667),
 "西の河原露天風呂": (36.62306,138.58944),
 "熱乃湯": (36.62222,138.59611),
 "裏草津 地蔵の湯": (36.62139,138.59750),
 "大滝乃湯": (36.61972,138.60028),
 "草津熱帯圏": (36.61639,138.60111),
 "草津温泉バスターミナル": (36.62472,138.59500),
}
DL={"7/18":"1日目","7/19":"2日目"}
def kml(fname,title,days):
    b=['<?xml version="1.0" encoding="UTF-8"?>','<kml xmlns="http://www.opengis.net/kml/2.2"><Document>',f'<name>{title}</name>']
    col={"7/18":"ff2dc0ff","7/19":"ffe6944b"}
    for day,stops in days:
        d=DL[day]; b.append(f'<Folder><name>{d}（{day}）</name>'); line=[]
        for spot,time,act in stops:
            lat,lng=C[spot]
            b.append(f'<Placemark><name>{d}-{spot}</name><description>{time} {act}</description><Point><coordinates>{lng},{lat},0</coordinates></Point></Placemark>')
            line.append(f'{lng},{lat},0')
        b.append(f'<Placemark><name>{d} ルート</name><Style><LineStyle><color>{col[day]}</color><width>4</width></LineStyle></Style><LineString><tessellate>1</tessellate><coordinates>{" ".join(line)}</coordinates></LineString></Placemark>')
        b.append('</Folder>')
    b.append('</Document></kml>')
    open(fname,"w",encoding="utf-8").write("\n".join(b))

gourmet=[
 ("7/18",[
   ("大東館","12:30","荷物を預けて出発"),
   ("湯畑","12:45","昼食（湯畑 草庵の草津温泉バーガー）＋食べ歩き"),
   ("西の河原露天風呂","15:00","日帰り温泉でクールダウン（800円）"),
   ("熱乃湯","16:00","湯もみショー観覧（700円）"),
   ("裏草津 地蔵の湯","16:45","裏草津の街歩き・カフェ月の貌でスイーツ"),
   ("大東館","17:45","大東館へ戻る → 18:00 夕食"),
 ]),
 ("7/19",[
   ("大東館","10:00","チェックアウト（荷物を預ける）"),
   ("大滝乃湯","10:30","朝の日帰り温泉（合わせ湯）"),
   ("草津熱帯圏","11:15","動物園（温泉熱ドーム・カピバラ・爬虫類）"),
   ("湯畑","12:30","昼食＆お土産（温泉まんじゅう食べ比べ）＋最後の食べ歩き"),
   ("大東館","13:45","手荷物の受け取り"),
   ("草津温泉バスターミナル","14:00","出発（14:15 集合）"),
 ]),
]
kml("output/maps/草津_グルメ重視_ルート.kml","草津温泉 グルメ重視 散策ルート",gourmet)

txt = """【草津温泉 グルメ重視プラン】

■ 7/18（土）
12:45 湯畑 草庵で草津温泉バーガー／上州牛ランチ（昼食）
https://rlx.jp/journal/kitakanto/gunma/176081
14:00 湯畑食べ歩き（本家ちちや・山びこ揚げまんじゅう・草津温泉プリン・上州牛まん）
https://honke-chichiya.com/
15:00 西の河原露天風呂でクールダウン（800円）※日帰り温泉めぐり
https://onsen-kusatsu.com/sainokawara/
16:00 熱乃湯 湯もみショー（16:00/16:30回・700円）
https://www.kusatsu-onsen.ne.jp/netsunoyu/show.html
16:45 裏草津を街歩き（月の貌でスイーツ＋足湯・顔湯）
https://www.kusatsu-onsen.ne.jp/ura-kusatsu_jizo/
17:45 大東館へ → 18:00 夕食

■ 7/19（日）
10:00 チェックアウト（荷物を預ける）
10:30 御座之湯 or 大滝乃湯で朝の日帰り温泉 ※温泉めぐり2湯目
https://onsen-kusatsu.com/
11:15 草津熱帯圏（動物園／8:30-17:00・大人1,300円）
http://nettaiken.com/index.html
12:30 名物ランチ（そば・ひもかわ・上州牛など）※昼食
https://rlx.jp/journal/kitakanto/gunma/176081
13:15 温泉まんじゅう食べ比べ土産＋地酒・花豆 ※お土産
https://honke-chichiya.com/
13:45 大東館で手荷物を受け取り
14:00 バスターミナルへ → 14:15 集合
https://www.kusatsu-onsen.ne.jp/
"""
open("output/草津_グルメ重視_予定_LINE用.txt","w",encoding="utf-8").write(txt)
print("done")
