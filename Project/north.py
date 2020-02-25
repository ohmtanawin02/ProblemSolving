import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
# เชื่อมจังหวัดทุกจังหวัดเข้ามากัน

# north
G.add_edge('Chiangrai', 'Phayao', weight=94)
G.add_edge('Chiangrai', 'Chiang mai', weight=182)
G.add_edge('Chiangrai', 'Lampang', weight=225)
G.add_edge('Phayao', 'Chiangrai', weight=94)
G.add_edge('Phayao', 'Lampang', weight=131)
G.add_edge('Phayao', 'Nan', weight=176)
G.add_edge('Phayao', 'Phrae', weight=141)
G.add_edge('Maehongson', 'Chiangmai', weight=349)
G.add_edge('Maehongson', 'Tak', weight=499)
G.add_edge('Chiangmai', 'Chiangrai', weight=182)
G.add_edge('Chiangmai', 'Lampang', weight=92)
G.add_edge('Chiangmai', 'Lampoon', weight=21)
G.add_edge('Chiangmai', 'Tak', weight=265)
G.add_edge('Chiangmai', 'Maehongson', weight=349)
G.add_edge('Lampoon', 'Lampang', weight=71)
G.add_edge('Lampoon', 'Chiangmai', weight=21)
G.add_edge('Lampoon', 'Tak', weight=244)
G.add_edge('Lampang', 'Chiangrai', weight=97)
G.add_edge('Lampang', 'Chiangmai', weight=92)
G.add_edge('Lampang', 'Phayao', weight=131)
G.add_edge('Lampang', 'Phrae', weight=109)
G.add_edge('Lampang', 'Sukhothai', weight=207)
G.add_edge('Lampang', 'Tak', weight=174)
G.add_edge('Lampang', 'Lampoon', weight=71)
G.add_edge('Phrae', 'Phayao', weight=141)
G.add_edge('Phrae', 'Nan', weight=118)
G.add_edge('Phrae', 'Lampang', weight=109)
G.add_edge('Phrae', 'Uttaradit', weight=74)
G.add_edge('Phrae', 'Sukhothai', weight=165)
G.add_edge('Nan', 'Phrae', weight=118)
G.add_edge('Nan', 'Uttaradit', weight=191)
G.add_edge('Nan', 'Phayao', weight=118)
G.add_edge('Tak', 'Maehongson', weight=499)
G.add_edge('Tak', 'Chiangmai', weight=265)
G.add_edge('Tak', 'Lampoon', weight=244)
G.add_edge('Tak', 'Lampang', weight=174)
G.add_edge('Tak', 'Sukhothai', weight=79)
G.add_edge('Tak', 'Kamphaengphet', weight=68)
G.add_edge('Tak', 'Nakhonsawan', weight=185)
G.add_edge('Tak', 'Uthaithani', weight=234)
G.add_edge('Sukhothai', 'Phrae', weight=165)
G.add_edge('Sukhothai', 'Uttaradit', weight=100)
G.add_edge('Sukhothai', 'Phitsanulok', weight=59)
G.add_edge('Sukhothai', 'Kamphaengphet', weight=77)
G.add_edge('Sukhothai', 'Tak', weight=79)
G.add_edge('Sukhothai', 'Lampang', weight=207)
G.add_edge('Uttaradit', 'Phrae', weight=74)
G.add_edge('Uttaradit', 'Nan', weight=191)
G.add_edge('Uttaradit', 'Sukhothai', weight=100)
G.add_edge('Uttaradit', 'Phitsanulok', weight=118)
G.add_edge('Phitsanulok', 'Phetchabun', weight=170)
G.add_edge('Phitsanulok', 'Sukhothai', weight=59)
G.add_edge('Phitsanulok', 'Kamphaengphet', weight=103)
G.add_edge('Phitsanulok', 'Phichit', weight=73)
G.add_edge('Phitsanulok', 'Uttaradit', weight=118)
G.add_edge('Kamphaengphet', 'Tak', weight=68)
G.add_edge('Kamphaengphet', 'Phichit', weight=90)
G.add_edge('Kamphaengphet', 'Nakhonsawan', weight=117)
G.add_edge('Kamphaengphet', 'Sukhothai', weight=77)
G.add_edge('Kamphaengphet', 'Phitsanulok', weight=103)
G.add_edge('Phichit', 'Phitsanulok', weight=73)
G.add_edge('Phichit', 'Kamphaengphet', weight=90)
G.add_edge('Phichit', 'Nakhonsawan', weight=113)
G.add_edge('Phichit', 'Phetchabun', weight=129)
G.add_edge('Nakhonsawan', 'Phichit', weight=113)
G.add_edge('Nakhonsawan', 'Phetchabun', weight=184)
G.add_edge('Nakhonsawan', 'Kamphaengphet', weight=117)
G.add_edge('Nakhonsawan', 'Uthaithani', weight=50)
G.add_edge('Nakhonsawan', 'Tak', weight=185)
G.add_edge('Phetchabun', 'Phichit', weight=129)
G.add_edge('Phetchabun', 'Phitsanulok', weight=170)
G.add_edge('Phetchabun', 'Nakhonsawan', weight=184)
G.add_edge('Uthaithani', 'Tak', weight=234)
G.add_edge('Uthaithani', 'Nakhonsawan', weight=50)

G.add_edge('Phitsanulok', 'Loey', weight=269)
G.add_edge('Phetchabun', 'Loey', weight=190)
G.add_edge('Phetchabun', 'Khonkaen', weight=240)
G.add_edge('Phetchabun', 'Chaiyaphum', weight=240)

# esan
G.add_edge('Nakornphanom', 'Bungkal', weight=176)
G.add_edge('Nakornphanom', 'Sakonnakhon', weight=93)
G.add_edge('Nakornphanom', 'Mookdaharn', weight=104)
G.add_edge('Bungkal', 'Nongkay', weight=143)
G.add_edge('Bungkal', 'Sakonnakhon', weight=194)
G.add_edge('Nongkay', 'Loey', weight=202)
G.add_edge('Nongkay', 'Udonthani', weight=51)
G.add_edge('Loey', 'Udonthani', weight=152)
G.add_edge('Loey', 'Nongbualamphu', weight=106)
G.add_edge('Loey', 'Khonkaen', weight=206)
G.add_edge('Nongbualamphu', 'Udonthani', weight=46)
G.add_edge('Nongbualamphu', 'Khonkaen', weight=181)
G.add_edge('Udonthani', 'Sakonnakhon', weight=159)
G.add_edge('Udonthani', 'Khonkaen', weight=115)
G.add_edge('Udonthani', 'Kallasin', weight=192)
G.add_edge('Sakonnakhon', 'Kallasin', weight=128)
G.add_edge('Sakonnakhon', 'Mookdaharn', weight=119)
G.add_edge('Mookdaharn', 'Kallasin', weight=172)
G.add_edge('Mookdaharn', 'Royied', weight=162)
G.add_edge('Mookdaharn', 'Yasotorn', weight=166)
G.add_edge('Mookdaharn', 'Amnajcharoen', weight=88)
G.add_edge('Kallasin', 'Khonkaen', weight=77)
G.add_edge('Kallasin', 'Mahasarakham', weight=44)
G.add_edge('Kallasin', 'Royied', weight=47)
G.add_edge('Khonkaen', 'Chaiyaphum', weight=150)
G.add_edge('Khonkaen', 'Mahasarakham', weight=73)
G.add_edge('Khonkaen', 'Buriram', weight=200)
G.add_edge('Khonkaen', 'Nakhonrachasima', weight=190)
G.add_edge('Chaiyaphum', 'Nakhonrachasima', weight=119)
G.add_edge('Mahasarakham', 'Royied', weight=40)
G.add_edge('Mahasarakham', 'Buriram', weight=145)
G.add_edge('Royied', 'Buriram', weight=146)
G.add_edge('Royied', 'Surin', weight=137)
G.add_edge('Royied', 'Srisaket', weight=230)
G.add_edge('Royied', 'Yasotorn', weight=71)
G.add_edge('Yasotorn', 'Amnajcharoen', weight=54)
G.add_edge('Yasotorn', 'Srisaket', weight=159)
G.add_edge('Amnajcharoen', 'Ubonrachathani', weight=75)
G.add_edge('Ubonrachathani', 'Srisaket', weight=61)
G.add_edge('Srisaket', 'Surin', weight=105)
G.add_edge('Surin', 'Buriram', weight=50)
G.add_edge('Buriram', 'Nakhonrachasima', weight=124)

G.add_edge('Lopburi', 'Chaiyaphum', weight=243)
G.add_edge('Lopburi', 'Nakhonrachasima', weight=298)
G.add_edge('Saraburi', 'Nakhonrachasima', weight=152)
G.add_edge('Nakhon Nayok', 'Nakhonrachasima', weight=213)
G.add_edge('Prachinburi', 'Nakhonrachasima', weight=194)
G.add_edge('Sa Kaeo', 'Nakhonrachasima', weight=174)
G.add_edge('Sa Kaeo', 'Buriram', weight=221)

G.add_edge('Tak', 'Kanchanaburi', weight=554)
G.add_edge('Uthai Thani', 'Kanchanaburi', weight=234)
G.add_edge('Uthai Thani', 'Suphan Buri', weight=319)
G.add_edge('Uthai Thani', 'Chai Nat', weight=42)
G.add_edge('Nakhonsawan', 'Chai Nat', weight=64)
G.add_edge('Nakhonsawan', 'Lopburi', weight=130)
G.add_edge('Phetchabun', 'Lopburi', weight=251)


# mid

G.add_edge('Bangkok', 'Samutprakan', weight=29)
G.add_edge('Bangkok', 'Samutsakhon', weight=36)
G.add_edge('Bangkok', 'Nakhonpathom', weight=56)
G.add_edge('Bangkok', 'Nonthaburi', weight=20)
G.add_edge('Bangkok', 'Pathumthani', weight=46)
G.add_edge('Bangkok', 'Prachinburi', weight=136)
G.add_edge('Bangkok', 'Chachoengsao', weight=82)
G.add_edge('Trat', 'Chanthaburi', weight=70)
G.add_edge('Chanthaburi', 'Rayong', weight=110)
G.add_edge('Chanthaburi', 'Chonburi', weight=164)
G.add_edge('Chanthaburi', 'Chachoengsao', weight=228)
G.add_edge('Chanthaburi', 'Sakaeo', weight=258)
G.add_edge('Rayong', 'Chonburi', weight=98)
G.add_edge('Chonburi', 'Samutprakan', weight=64)
G.add_edge('Chonburi', 'Chachoengsao', weight=43)
G.add_edge('Samutprakan', 'Chachoengsao', weight=71)
G.add_edge('Sakaeo', 'Chachoengsao', weight=245)
G.add_edge('Sakaeo', 'Prachinburi', weight=98)
G.add_edge('Prachinburi', 'Nakhonnayok', weight=29)
G.add_edge('Nakhonnayok', 'Saraburi', weight=58)
G.add_edge('Nakhonnayok', 'Pathumthani', weight=101)
G.add_edge('Saraburi', 'Lopburi', weight=46)
G.add_edge('Saraburi', 'Phranakhonsiayutthaya', weight=63)
G.add_edge('Saraburi', 'Pathumthani', weight=101)
G.add_edge('Saraburi', 'Angthong', weight=58)
G.add_edge('Saraburi', 'Singburi', weight=79)
G.add_edge('Samutsakhon', 'Samutprakan', weight=65)
G.add_edge('Samutsongkhram', 'Samutsakhon', weight=37)
G.add_edge('Prachuapkhirikhan', 'Phetchaburi', weight=158)
G.add_edge('Phetchaburi', 'Ratchaburi', weight=54)
G.add_edge('Phetchaburi', 'Samutsongkhram', weight=53)
G.add_edge('Ratchaburi', 'Samutsongkhram', weight=43)
G.add_edge('Ratchaburi', 'Samutprakan', weight=129)
G.add_edge('Ratchaburi', 'Nakhonpathom', weight=41)
G.add_edge('Ratchaburi', 'Suphanburi', weight=147)
G.add_edge('Ratchaburi', 'Kanchanaburi', weight=87)
G.add_edge('Kanchanaburi', 'Suphanburi', weight=91)
G.add_edge('Suphanburi', 'Chainat', weight=294)
G.add_edge('Suphanburi', 'Singburi', weight=1056)
G.add_edge('Suphanburi', 'Angthong', weight=44)
G.add_edge('Suphanburi', 'Phranakhonsiayutthaya', weight=176)
G.add_edge('Suphanburi', 'Nakhonpathom', weight=105)
G.add_edge('Nakhonpathom', 'Samutsakhon', weight=85)
G.add_edge('Chainat', 'Singburi', weight=53)
G.add_edge('Chainat', 'Angthong', weight=92)
G.add_edge('Lopburi', 'Singburi', weight=33)
G.add_edge('Angthong', 'Sing Buri', weight=40)
G.add_edge('Angthong', 'Lopburi', weight=67)
G.add_edge('Angthong', 'Phranakhonsiayutthaya', weight=31)
G.add_edge('Phranakhonsiayutthaya', 'Pathumthani', weight=122)
G.add_edge('Phranakhonsiayutthaya', 'Nonthaburi', weight=96)
G.add_edge('Phranakhonsiayutthaya', 'Nakhonpathom', weight=132)

# south
G.add_edge('Narathiwat', 'Yala', weight=128)
G.add_edge('Narathiwat', 'Pattani', weight=35)
G.add_edge('Pattani', 'Yala', weight=94)
G.add_edge('Pattani', 'Songkhla', weight=99)
G.add_edge('Yala', 'Songkhla', weight=128)
G.add_edge('Songkhla', 'Satun', weight=125)
G.add_edge('Songkhla', 'Phatthalung', weight=121)
G.add_edge('Satun', 'Trang', weight=140)
G.add_edge('Trang', 'Phatthalung', weight=56)
G.add_edge('Trang', 'Krabi', weight=131)
G.add_edge('Trang', 'Nakhonsithammarat', weight=123)
G.add_edge('Phatthalung', 'Nakhon Si Thammarat', weight=99)
G.add_edge('Nakhonsithammarat', 'Krabi', weight=223)
G.add_edge('Nakhonsithammarat', 'Suratthani', weight=134)
G.add_edge('Krabi', 'Suratthani', weight=211)
G.add_edge('Krabi', 'Phangnga', weight=86)
G.add_edge('Phangnga', 'Suratthani', weight=196)
G.add_edge('Phangnga', 'Phuket', weight=87)
G.add_edge('Suratthani', 'Chumphon', weight=193)
G.add_edge('Suratthani', 'Ranong', weight=219)
G.add_edge('Phangnga', 'Ranong', weight=226)
G.add_edge('Ranong', 'Chumphon', weight=117)
G.add_edge('Chumphon', 'Prachuapkhirikhan', weight=183)
G.add_edge('Prachuapkhirikhan', 'Phetchaburi', weight=158)
G.add_edge('Phetchaburi', 'Ratchaburi', weight=54)
G.add_edge('Ranong', 'Chumphon', weight=117)
G.add_edge('Chumphon', 'Prachuapkhirikhan', weight=183)


again = 'Y'
while again == 'Y' or again == 'y':  # loop while เพื่อเลือกเงื่อนไข
    print('1.No visit')
    print('2. 1 visit')
    print('3. 2 visit')
    print('4.Exit')
    key = int(input("Enter the chioce :"))
    if key == 1:  # ไม่แวะ
        location1 = input("Enter your location : ")
        location2 = input("Where do you want to go :  ")
        print('Shorttest path from ', location1, 'to', location2, 'is', nx.shortest_path(
            G, source=location1, target=location2, weight='weight'))
        d = (nx.shortest_path_length(G, source=location1,
                                     target=location2, weight='weight'))
        print("The distance is ", d, "km")
        print("The time is about", d//80, "hours")
        edge_labels = nx.get_edge_attributes(G, 'weight')
        #print (edge_labels)
        pos = nx.spring_layout(G)  # วาดกกราฟ
        plt.figure(8, figsize=(20, 20))
        nx.draw(G, pos, with_labels=True, font_color='yellow', node_size=2000)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()

    if key == 2:  # แวะ1จุด
        location1 = input("Enter your location :  ")
        location2 = input("Where do you want to visit :  ")
        location3 = input("Where do you want to go :  ")
        a = (nx.shortest_path_length(G, source=location1,
                                     target=location2, weight='weight'))
        b = (nx.shortest_path_length(G, source=location2,
                                     target=location3, weight='weight'))
        c = (nx.shortest_path_length(G, source=location1,
                                     target=location3, weight='weight'))
        d = (nx.shortest_path(G, source=location1,
                              target=location2, weight='weight'))
        e = (nx.shortest_path(G, source=location3,
                              target=location2, weight='weight'))
        f = (nx.shortest_path(G, source=location1,
                              target=location3, weight='weight'))
        A = (nx.shortest_path(G, source=location2,
                              target=location3, weight='weight'))
        if a+c <= a+b:
            g = (f+e)
            h = c+b
            print("Shorttest path from ", location1, "to", location3, "is", g)
            print("The distance is ", h, "km")
            print("The time is about", h//80, "hours")
        else:
            i = (a+b)
            j = d+A
            print("Shorttest path from ", location1, "to", location3, "is", j)
            print("The distance is ", i, "km")
            print("The time is about", i//80, "hours")
        edge_labels = nx.get_edge_attributes(G, 'weight')
        #print (edge_labels)
        pos = nx.spring_layout(G)  # วาดกกราฟ
        plt.figure(8, figsize=(20, 20))
        nx.draw(G, pos, with_labels=True, font_color='yellow', node_size=2000)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()

    if key == 3:  # แวะ2จุด
        location1 = input("Enter your location :  ")
        location2 = input("Where do you want to visit :  ")
        location3 = input("Where do you want to visit :  ")
        location4 = input("Where do you want to go :  ")
        a = (nx.shortest_path_length(G, source=location1,
                                     target=location2, weight='weight'))
        b = (nx.shortest_path_length(G, source=location2,
                                     target=location3, weight='weight'))
        c = (nx.shortest_path_length(G, source=location3,
                                     target=location4, weight='weight'))
        d = (nx.shortest_path_length(G, source=location1,
                                     target=location3, weight='weight'))
        e = (nx.shortest_path_length(G, source=location1,
                                     target=location4, weight='weight'))
        f = (nx.shortest_path_length(G, source=location2,
                                     target=location4, weight='weight'))
        g = (nx.shortest_path_length(G, source=location1,
                                     target=location2, weight='weight'))
        h = (nx.shortest_path_length(G, source=location2,
                                     target=location3, weight='weight'))
        i = (nx.shortest_path_length(G, source=location3,
                                     target=location4, weight='weight'))
        j = (nx.shortest_path_length(G, source=location1,
                                     target=location3, weight='weight'))
        k = (nx.shortest_path_length(G, source=location1,
                                     target=location4, weight='weight'))
        l = (nx.shortest_path_length(G, source=location2,
                                     target=location4, weight='weight'))
        m = (nx.shortest_path_length(G, source=location4,
                                     target=location3, weight='weight'))
        n = (nx.shortest_path_length(G, source=location4,
                                     target=location2, weight='weight'))
        o = (nx.shortest_path_length(G, source=location3,
                                     target=location2, weight='weight'))
        a1 = (nx.shortest_path(G, source=location1,
                               target=location2, weight='weight'))
        a2 = (nx.shortest_path(G, source=location3,
                               target=location2, weight='weight'))
        a3 = (nx.shortest_path(G, source=location1,
                               target=location3, weight='weight'))
        a4 = (nx.shortest_path(G, source=location2,
                               target=location3, weight='weight'))
        a5 = (nx.shortest_path(G, source=location1,
                               target=location4, weight='weight'))
        a6 = (nx.shortest_path(G, source=location2,
                               target=location4, weight='weight'))
        a7 = (nx.shortest_path(G, source=location4,
                               target=location2, weight='weight'))
        a8 = (nx.shortest_path(G, source=location3,
                               target=location2, weight='weight'))
        a8 = (nx.shortest_path(G, source=location4,
                               target=location3, weight='weight'))
        a9 = (nx.shortest_path(G, source=location3,
                               target=location4, weight='weight'))
        A = g+h+i
        B = g+l+m
        C = j+o+l
        D = j+i+n
        E = k+m+o
        F = k+n+h
        list1 = [A, B, C, D, E, F]

        if min(list1) == A:
            print('Shorttest path from ', location1,
                  'to', location4, 'is', a1+a4+a8)
        if min(list1) == B:
            print('Shorttest path from ', location1,
                  'to', location4, 'is', a1+a6+a9)
        if min(list1) == C:
            print('Shorttest path from ', location1,
                  'to', location4, 'is', a3+a8+a6)
        if min(list1) == D:
            print('Shorttest path from ', location1,
                  'to', location4, 'is', a3+a8+a7)
        if min(list1) == E:
            print('Shorttest path from ', location1,
                  'to', location4, 'is', a5+a9+a8)
        if min(list1) == F:
            print('Shorttest path from ', location1,
                  'to', location4, 'is', a5+a7+a4)
        print('The distance is  :', min(list1), "km")
        print("The time is about", (min(list1))//80, "hours")
        edge_labels = nx.get_edge_attributes(G, 'weight')
        #print (edge_labels)
        pos = nx.spring_layout(G)  # วาดกกราฟ
        plt.figure(8, figsize=(20, 20))
        nx.draw(G, pos, with_labels=True, font_color='yellow', node_size=2000)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()

    if key == 4:  # หยุดโปรแกรม
        break
    else:
        again == 'Y'
    again = input('Enter Y to do again :')
