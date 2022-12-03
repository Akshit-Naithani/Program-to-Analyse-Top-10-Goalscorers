import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

a = 'yes'
a1 = 'NA'
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)
while a == 'Yes' or a== 'yes':
        print('__'*50)
        print(" "*30,"Most Prolific Goal Scorers Of This Decade")
        print()
        print("1. Analysis Based On Data")
        print("2. Data Representation")
        print("3. Manipulation Of Data")
        print("4. Exit")
        print('__'*50)
        b = int(input("Enter The Number: "))
        z = 'yes'
        while z == 'Yes' or z == 'yes':
                if b == 1 :
                        print('\n')
                        print('__'*50)
                        print(" "*30,"Analysis Based On Data")
                        print()
                        print("1. No. Of Top Records")
                        print("2. No. Of Bottom Records")
                        print("3. To Show Number Of Specific Column")
                        print("4. To Show Multiple Coloumn (Left To Right)")
                        print("5. To Show Multiple Coloumn (Right To Left)")
                        print("6. To Show Number Of Specific Row")
                        print("7. To Show Maximum Of A Column")
                        print("8. To Show Minimum Of A Column")
                        print("9. To Show All Records")
                        print("10. Go Back")
                        print('__'*50)
                        d = int(input("Enter The Number: "))
                        if d == 1 :
                                f = int(input("How Many Records From The Top ? (Max:10) : "))
                                if f > 10 :
                                        print("Error! You Entered A Number Greater Than 10")
                                else :
                                        cdf= pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv",nrows = f)
                                        print(cdf)
                                z = input("Want To Check Something Else In Analysis Based On Data ?(Yes/No):")
                        elif d == 2 :
                                f = int(input("How Many Records From The Bottom ? (Max: 10) : "))
                                if f > 10 :
                                        print("Error! You Entered A Number Greater Than 10")
                                else :
                                        cdf= pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv",)
                                        print(cdf.tail(f))
                                z = input("Want To Check Something Else In Analysis Based On Data ?(Yes/No):")
                        elif d == 3 :
                                f = pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv")
                                g = int(input("How Many Columns Do You Want To Check (Max:14) : "))
                                h = ['First',"Second","Third",'Fourth','Fifth','Sixth','Seventh','Eighth','Nineth','Tenth','Eleventh','Twelveth','Thirteenth','Fourteenth']
                                k = []
                                if g > 14 :
                                        print("Error! You Entered A Number Greater Than 14")
                                else :
                                        for i in range(0,g) :
                                                print('Enter The ',end = '')
                                                print(h[i],end = '')
                                                m = input(' Column You Want To Read [Column Names: Footballers,Goals,Expected Goals,Assists,Expected Assists,Games Played,Goals Per Games Played,Assists Per Games Played,Shots Per 90,Shot On Target Per 90,Shooting Accuracy(in %),Attempted Passes Per Game,Completed Passes Per Game,Progressive Passes Per Game (in yards)] : ')
                                                k.append(m)
                                        print(f[k])
                                z = input("Want To Check Something Else In Analysis Based On Data ?(Yes/No):")
                        elif d == 4 :
                                f = pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv")
                                g = int(input("How Many Columns From Left Do You Want To Check (Max:14) : "))
                                h = ['Footballers','Goals','Expected Goals','Assists','Expected Assists','Games Played','Goals Per Games Played','Assists Per Games Played','Shots Per 90','Shot On Target Per 90','Shooting Accuracy(in %)','Attempted Passes Per Game','Completed Passes Per Game','Progressive Passes Per Game (in yards)']
                                k = []
                                if g > 14 :
                                        print("Error! You Entered A Number Greater Than 14")
                                else :
                                        for i in range(0,g) :
                                                k.append(h[i])
                                        print(f[k])
                                z = input("Want To Check Something Else ?(Yes/No):")
                        elif d == 5 :
                                f = pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv")
                                g = int(input("How Many Columns From Left Do You Want To Check (Max:14) : "))
                                h = ['Progressive Passes Per Game (in yards)','Completed Passes Per Game','Attempted Passes Per Game','Shooting Accuracy(in %)','Shot On Target Per 90','Shots Per 90','Assists Per Games Played','Goals Per Games Played','Games Played','Expected Assists','Assists','Expected Goals','Goals']
                                k = []
                                if g > 14 :
                                        print("Error! You Entered A Number Greater Than 14")
                                else :
                                        for i in range(0,g) :
                                                k.append(h[i])
                                        print(f[k])
                                z = input("Want To Check Something Else In Analysis Based On Data ?(Yes/No):")
                        elif d == 6 :
                                p = []
                                c = []
                                q = []
                                e = []
                                f = []
                                g = []
                                p1 = []
                                c1 = []
                                q1 = []
                                e1 = []
                                f1 = []
                                g1 = []
                                p11 = []
                                c11 = []
                                h = ['First',"Second","Third",'Fourth','Fifth','Sixth','Seventh','Eighth','Nineth','Tenth','Eleventh','Twelveth','Thirteenth','Fourteenth']
                                o = 0
                                p = []
                                q = []
                                for i in range(1,11):
                                        for j in range(1,11):
                                                r = list(pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv",skiprows= i, nrows= j))
                                        p.append(r[0])
                                        c.append(r[1])
                                        q.append(r[2])
                                        e.append(r[3])
                                        f.append(r[4])
                                        g.append(r[5])
                                        p1.append(r[6])
                                        c1.append(r[7])
                                        q1.append(r[8])
                                        e1.append(r[9])
                                        f1.append(r[10])
                                        g1.append(r[11])
                                        p11.append(r[12])
                                        c11.append(r[13])

                                k = int(input("How Many Rows You Want To Check ?(Max 10): "))
                                print("Footballer = ")
                                for l in range(0,k):
                                        print('Enter The ',end = '')
                                        print(h[l],end = '')
                                        m = input(' Row You Want To Read (Names: Ronaldo, Messi, Aguero, Huntelaar, Cavani, Higuain, Suarez, Lewandowski, Ibrahimovic, Rooney)[Case Sensitive]: ')
                                        for n in range(1,11):
                                                if m == p[o] :
                                                        print(m,' = ',[c[o],q[o],e[o],f[o],g[o],p1[o],c1[o],q1[o],e1[o],f1[o],g1[o],p11[o],c11[o]])
                                                o = o + 1
                                        o = 0
                                z = input("Want To Check Something Else In Analysis Based On Data ?(Yes/No):")
                        elif d == 7 :
                                r = input("Enter The Column You Want The Maximum Of (Column Names: Goals, Expected Goals, Assists, Expected Assists, Games Played, Goals Per Games Played, Assists Per Games Played, Shots Per 90,Shot On Target Per 90, Shooting Accuracy(in %), Attempted Passes Per Game, Completed Passes Per Game, Progressive Passes Per Game(in yards))[Case Sensitive]: ")
                                cdf= pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv", header = None, skiprows = 1,names = ['Footballers','Goals','Expected Goals','Assists','Expected Assists','Games Played','Goals Per Games Played','Assists Per Games Played','Shots Per 90','Shot On Target Per 90','Shooting Accuracy(in %)','Attempted Passes Per Game','Completed Passes Per Game','Progressive Passes Per Game (in yards)'])
                                print(cdf)
                                if r == 'Goals' :
                                        print("Maximum Goals Scored Is ",cdf['Goals'].max())
                                        
                                elif r == 'Expected Goals' :
                                        print("Maximum Expected Goals Is ",cdf['Expected Goals'].max())
                                        
                                elif r == 'Assists' :
                                        print("Maximum Assists Scored Is ",cdf['Assists'].max())
                                        
                                elif r == 'Expected Assists' :
                                        print("Maximum Expected Assists Is ",cdf['Expected Assists'].max())
                                        
                                elif r == 'Games Played' :
                                        print("Maximum Games Played Is ",cdf['Games Played'].max())
                                        
                                elif r == 'Goals Per Games Played' :
                                        print("Maximum  Is ",cdf['Goals Per Games Played'].max())
                                        
                                elif r == 'Assists Per Games Played' :
                                        print("Maximum Games Played Is ",cdf['Assists Per Games Played'].max())
                                        
                                elif r == 'Shots Per 90' :
                                        print("Maximum Goals Per Games Played Is ",cdf['Shots Per 90'].max())
                                        
                                elif r == 'Shot On Target Per 90' :
                                        print("Maximum Shot On Target Per Match Is ",cdf['Shot On Target Per 90'].max())
                                        
                                elif r == 'Shooting Accuracy(in %)' or r == 'Shooting Accuracy' :
                                        print("Maximum Shot Accuracy Per Match Is ",cdf['Shooting Accuracy (in %)'].max())
                                        
                                elif r == 'Attempted Passes Per Game':
                                        print("Maximum Shot Accuracy Per Match Is ",cdf['Attempted Passes Per Game'].max())

                                elif r == 'Completed Passes Per Game':
                                        print("Maximum Shot Accuracy Per Match Is ",cdf['Completed Passes Per Game'].max())

                                elif r == 'Progressive Passes Per Game (in yards)' or r == 'Progressive Passes Per Game':
                                        print("Maximum Shot Accuracy Per Match Is ",cdf['Progressive Passes Per Game (in yards)'].max())
                                        
                                else :
                                        print("You Entered The Wrong Value")
                                z = input("Want To Check Something Else In Analysis Based On Data ?(Yes/No):")
                        elif d == 8 :
                                r = input("Enter The Column You Want The Minimum Of (Column Names: Footballers,Goals,Expected Goals,Assists,Expected Assists,Games Played,Goals Per Games Played,Assists Per Games Played,Shots Per 90,Shot On Target Per 90,Shooting Accuracy(in %),Attempted Passes Per Game,Completed Passes Per Game,Progressive Passes Per Game (in yards))[Case Sensitive]: ")
                                cdf= pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv", header = None, skiprows = 1,names = ['Footballers','Goals','Expected Goals','Assists','Expected Assists','Games Played','Goals Per Games Played','Assists Per Games Played','Shots Per 90','Shot On Target Per 90','Shooting Accuracy(in %)','Attempted Passes Per Game','Completed Passes Per Game','Progressive Passes Per Game (in yards)'])
                                print(cdf)
                                if r == 'Goals' :
                                        print("Minimum Goals Scored Is ",cdf['Goals'].min())
                                        
                                elif r == 'Expected Goals' :
                                        print("Minimum Expected Goals Is ",cdf['Expected Goals'].min())
                                        
                                elif r == 'Assists' :
                                        print("Minimum Assists Scored Is ",cdf['Assists'].min())
                                        
                                elif r == 'Expected Assists' :
                                        print("Minimum Expected Assists Is ",cdf['Expected Assists'].min())
                                        
                                elif r == 'Games Played' :
                                        print("Minimum Games Played Is ",cdf['Games Played'].min())
                                        
                                elif r == 'Goals Per Games Played' :
                                        print("Minimum  Is ",cdf['Goals Per Games Played'].min())
                                        
                                elif r == 'Assists Per Games Played' :
                                        print("Minimum Games Played Is ",cdf['Assists Per Games Played'].min())
                                        
                                elif r == 'Shots Per 90' :
                                        print("Minimum Goals Per Games Played Is ",cdf['Shots Per 90'].min())
                                        
                                elif r == 'Shot On Target Per 90' :
                                        print("Minimum Shot On Target Per Match Is ",cdf['Shot On Target Per 90'].min())
                                        
                                elif r == 'Shooting Accuracy(in %)' or r == 'Shooting Accuracy' :
                                        print("Minimum Shot Accuracy Per Match Is ",cdf['Shooting Accuracy (in %)'].min())
                                        
                                elif r == 'Attempted Passes Per Game':
                                        print("Minimum Shot Accuracy Per Match Is ",cdf['Attempted Passes Per Game'].min())

                                elif r == 'Completed Passes Per Game':
                                        print("Minimum Shot Accuracy Per Match Is ",cdf['Completed Passes Per Game'].min())

                                elif r == 'Progressive Passes Per Game (in yards)' or r == 'Progressive Passes Per Game':
                                        print("Minimum Shot Accuracy Per Match Is ",cdf['Progressive Passes Per Game (in yards)'].min())
                                        
                                else :
                                        print("You Entered The Wrong Value")
                                z = input("Want To Check Something Else In Analysis Based On Data ?(Yes/No):")
                        elif d == 9 :
                                cdf= pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv")
                                print(cdf)
                                z = input("Want To Check Something Else In Analysis Based On Data ?(Yes/No):")
                        elif d == 10 :
                                print()
                                break
                        else :
                                print("*"*100)
                                print("Oops... I Think You Entered The Wrong Value")
                                print("*"*100)
                elif b == 2 :
                        while a1 == 'NA':
                                if a1 == 'NA':
                                        print('\n')
                                        print('__'*50)
                                        a2 = input("Apply Anti Color-Blind Colors On Graphs ???(Yes/No) : ")
                                        print()
                                        if a2 == 'yes' or a2 == 'YES':
                                               w = input("Red-Green/Blue-Yellow(RG/BY): ")
                                               a1 = 'A'
                                               break
                                        elif a2 == 'no' or a2 == 'No' :
                                                w = 'else'
                                                a1 = 'A'
                                                break
                                        else :
                                                print("Oops! You Entered Something Wrong")
                        print('\n')
                        print('__'*50)
                        print(" "*30,"Data Representation")
                        print()
                        print("1. Line Chart Depicting Shots On Target Per 90")
                        print("2. Pie Chart Depicting Shot Accuracy")
                        print("3. Bar Chart Depicting Goals Scored")
                        print("4. Line Depicting Goals Per Games Played")
                        print("5. Bar Chart Depicting Assists")
                        print("6. Bar Chart Depicting Expected Assists")
                        print("7. Line Chart Depicting Assists Per Games Played")
                        print("8. Bar Chart Depicting Shots Per 90")
                        print("9. Bar Chart Depicting Attempted Pass Per 90")
                        print("10. Bar Chart Depicting Completed Pass Per 90")
                        print("11. Barh Chart Depicting Progessive Passes Per 90")
                        print("12. Bar Chart Depicting Expected Goals")
                        print("13. Bar Chart Depicting Games Played")
                        print('14. Go Back')
                        print('__'*50)
                        c = int(input("Enter The Number: "))
                        if c == 1 :
                                g = []
                                h = []
                                for i in range(1,11):
                                        for j in range(1,11):
                                                f = list(pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv",skiprows= i, nrows= j))
                                        d = g.append(float(f[9]))
                                        e = h.append(f[0])
                                        X = np.arange(10)
                                if w == 'BY':
                                        pt.plot(X,g,color='red')
                                elif w == 'RG':
                                        pt.plot(X,g,color='blue')
                                else :
                                        pt.plot(X,g,color='red')
                                pt.xticks(X,h)
                                pt.ylabel("Shots On Target Per 90")
                                pt.xlabel("Footballers")
                                pt.title("Shots On Target By Footballer P90")
                                pt.show()
                                z = input("Want To Check Something Else In Data Representation ?(Yes/No):")
                        elif c == 2 :
                                g = []
                                h = []
                                if w == 'BY':
                                        col = ['darkgreen','grey','maroon','violet','darkred','green','pink','silver','red','beige']
                                elif w == 'RG':
                                        col = ['blue','cyan','gold','violet','darkblue','grey','orange','silver','beige','yellow']
                                else :
                                        col = ['blue','cyan','gold','violet','darkblue','green','pink','silver','red','yellow']
                                for i in range(1,11):
                                        for j in range(1,11):
                                                f = list(pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv",skiprows= i, nrows= j))
                                        d = g.append(float(f[10]))
                                        e = h.append(f[0])
                                        X = np.arange(10)
                                pt.pie(g,labels= h,colors= col,autopct= "%5.3f%%")
                                pt.axis("equal")
                                pt.title("Shot Accuary (in %)")
                                pt.show()
                                z = input("Want To Check Something Else In Data Representation ?(Yes/No):")
                        elif c == 3 :
                                g = []
                                h = []
                                if w == 'BY':
                                        col = ['darkgreen','grey','maroon','violet','darkred','green','pink','silver','red','beige']
                                elif w == 'RG':
                                        col = ['blue','cyan','gold','violet','darkblue','grey','orange','silver','beige','yellow']
                                else :
                                        col = ['blue','cyan','gold','violet','darkblue','green','pink','silver','red','yellow']
                                for i in range(1,11):
                                        for j in range(1,11):
                                                f = list(pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv",skiprows= i, nrows= j))
                                        d = g.append(float(f[1]))
                                        e = h.append(f[0])
                                X = np.arange(10)
                                pt.bar(h,g,color = col)
                                pt.title("Goals Scored In Their Carrers(Till 2021-22 Season)")
                                pt.ylabel('Goals')
                                pt.xlabel('Footballers')
                                pt.show()
                                z = input("Want To Check Something Else In Data Representation ?(Yes/No):")
                        elif c == 4 :
                                g = []
                                h = []
                                for i in range(1,11):
                                        for j in range(1,11):
                                                f = list(pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv",skiprows= i, nrows= j))
                                        d = g.append(float(f[6]))
                                        e = h.append(f[0])
                                        X = np.arange(10)
                                if w == 'BY':
                                        pt.plot(h,g,color='red')
                                elif w == 'RG':
                                        pt.plot(h,g,color='blue')
                                else :
                                        pt.plot(h,g,color='red')
                                pt.title("Total Goals Per Total Games Played")
                                pt.ylabel('Goals Per Games Played')
                                pt.xlabel('Footballers')
                                pt.show()
                                z = input("Want To Check Something Else In Data Representation ?(Yes/No):")
                        elif c == 5 :
                                g = []
                                h = []
                                if w == 'BY':
                                        col = ['darkgreen','grey','maroon','violet','darkred','green','pink','silver','red','beige']
                                elif w == 'RG':
                                        col = ['blue','cyan','gold','violet','darkblue','grey','orange','silver','beige','yellow']
                                else :
                                        col = ['blue','cyan','gold','violet','darkblue','green','pink','silver','red','yellow']
                                for i in range(1,11):
                                        for j in range(1,11):
                                                f = list(pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv",skiprows= i, nrows= j))
                                        d = g.append(float(f[3]))
                                        e = h.append(f[0])
                                        X = np.arange(10)
                                pt.bar(h,g,color = col)
                                pt.title("Assists Given In Their Carrers(Till 2021-22 Season)")
                                pt.ylabel('Assists')
                                pt.xlabel('Footballers')
                                pt.show()
                                z = input("Want To Check Something Else In Data Representation ?(Yes/No):")
                        elif c == 6 :
                                g = []
                                h = []
                                if w == 'BY':
                                        col = ['darkgreen','grey','maroon','violet','darkred','green','pink','silver','red','beige']
                                elif w == 'RG':
                                        col = ['blue','cyan','gold','violet','darkblue','grey','orange','silver','beige','yellow']
                                else :
                                        col = ['blue','cyan','gold','violet','darkblue','green','pink','silver','red','yellow']
                                for i in range(1,11):
                                        for j in range(1,11):
                                                f = list(pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv",skiprows= i, nrows= j))
                                        d = g.append(float(f[4]))
                                        e = h.append(f[0])
                                        X = np.arange(10)
                                pt.bar(h,g,color = col)
                                pt.title("Expected Assists Of Their Carrers(Till 2021-22 Season)")
                                pt.ylabel('Expected Assists')
                                pt.xlabel('Footballers')
                                pt.show()
                                z = input("Want To Check Something Else In Data Representation ?(Yes/No):")
                        elif c == 7 :
                                g = []
                                h = []
                                for i in range(1,11):
                                        for j in range(1,11):
                                                f = list(pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv",skiprows= i, nrows= j))
                                        d = g.append(float(f[7]))
                                        e = h.append(f[0])
                                        X = np.arange(10)
                                if w == 'BY':
                                        pt.plot(h,g,color='red')
                                elif w == 'RG':
                                        pt.plot(h,g,color='blue')
                                else :
                                        pt.plot(h,g,color='red')
                                pt.title("Assists Per 90")
                                pt.ylabel('Assists Per 90')
                                pt.xlabel('Footballers')
                                pt.show()
                                z = input("Want To Check Something Else In Data Representation ?(Yes/No):")
                        elif c == 8 :
                                g = []
                                h = []
                                if w == 'BY':
                                        col = ['darkgreen','grey','maroon','violet','darkred','green','pink','silver','red','beige']
                                elif w == 'RG':
                                        col = ['blue','cyan','gold','violet','darkblue','grey','orange','silver','beige','yellow']
                                else :
                                        col = ['blue','cyan','gold','violet','darkblue','green','pink','silver','red','yellow']
                                for i in range(1,11):
                                        for j in range(1,11):
                                                f = list(pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv",skiprows= i, nrows= j))
                                        d = g.append(float(f[8]))
                                        e = h.append(f[0])
                                        X = np.arange(10)
                                pt.bar(h,g,color = col)
                                pt.title("Shots Taken Per 90")
                                pt.ylabel('Shots Per 90')
                                pt.xlabel('Footballers')
                                pt.show()
                                z = input("Want To Check Something Else In Data Representation ?(Yes/No):")
                        elif c == 9 :
                                g = []
                                h = []
                                if w == 'BY':
                                        col = ['darkgreen','grey','maroon','violet','darkred','green','pink','silver','red','beige']
                                elif w == 'RG':
                                        col = ['blue','cyan','gold','violet','darkblue','grey','orange','silver','beige','yellow']
                                else :
                                        col = ['blue','cyan','gold','violet','darkblue','green','pink','silver','red','yellow']
                                for i in range(1,11):
                                        for j in range(1,11):
                                                f = list(pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv",skiprows= i, nrows= j))
                                        d = g.append(float(f[11]))
                                        e = h.append(f[0])
                                        X = np.arange(10)
                                pt.bar(h,g,color = col)
                                pt.title("Attempted Passes Per 90")
                                pt.ylabel('Attempted Passes P90')
                                pt.xlabel('Footballers')
                                pt.show()
                                z = input("Want To Check Something Else In Data Representation ?(Yes/No):")
                        elif c == 10 :
                                g = []
                                h = []
                                if w == 'BY':
                                        col = ['darkgreen','grey','maroon','violet','darkred','green','pink','silver','red','beige']
                                elif w == 'RG':
                                        col = ['blue','cyan','gold','violet','darkblue','grey','orange','silver','beige','yellow']
                                else :
                                        col = ['blue','cyan','gold','violet','darkblue','green','pink','silver','red','yellow']
                                for i in range(1,11):
                                        for j in range(1,11):
                                                f = list(pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv",skiprows= i, nrows= j))
                                        d = g.append(float(f[12]))
                                        e = h.append(f[0])
                                        X = np.arange(10)
                                pt.bar(h,g,color = col)
                                pt.title("Completed Passes Per 90")
                                pt.ylabel('Completed Passes P90')
                                pt.xlabel('Footballers')
                                pt.show()
                                z = input("Want To Check Something Else In Data Representation ?(Yes/No):")
                        elif c == 11 :
                                g = []
                                h = []
                                if w == 'BY':
                                        col = ['darkgreen','grey','maroon','violet','darkred','green','pink','silver','red','beige']
                                elif w == 'RG':
                                        col = ['blue','cyan','gold','violet','darkblue','grey','orange','silver','beige','yellow']
                                else :
                                        col = ['blue','cyan','gold','violet','darkblue','green','pink','silver','red','yellow']
                                for i in range(1,11):
                                        for j in range(1,11):
                                                f = list(pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv",skiprows= i, nrows= j))
                                        d = g.append(float(f[13]))
                                        e = h.append(f[0])
                                        X = np.arange(10)
                                pt.barh(h,g,color = col)
                                pt.title("Prgressive Passes Per 90 (in Yards)")
                                pt.ylabel('Progressive Pass P90')
                                pt.xlabel('Footballers')
                                pt.show()
                                z = input("Want To Check Something Else In Data Representation ?(Yes/No):")
                        elif c == 12 :
                                g = []
                                h = []
                                if w == 'BY':
                                        col = ['darkgreen','grey','maroon','violet','darkred','green','pink','silver','red','beige']
                                elif w == 'RG':
                                        col = ['blue','cyan','gold','violet','darkblue','grey','orange','silver','beige','yellow']
                                else :
                                        col = ['blue','cyan','gold','violet','darkblue','green','pink','silver','red','yellow']
                                for i in range(1,11):
                                        for j in range(1,11):
                                                f = list(pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv",skiprows= i, nrows= j))
                                        d = g.append(float(f[2]))
                                        e = h.append(f[0])
                                        X = np.arange(10)
                                pt.bar(h,g,color = col)
                                pt.title("Expected Carrer Goals")
                                pt.ylabel('Expected Goals')
                                pt.xlabel('Footballers')
                                pt.show()
                                z = input("Want To Check Something Else In Data Representation ?(Yes/No):")
                        elif c == 13 :
                                g = []
                                h = []
                                if w == 'BY':
                                        col = ['darkgreen','grey','maroon','violet','darkred','green','pink','silver','red','beige']
                                elif w == 'RG':
                                        col = ['blue','cyan','gold','violet','darkblue','grey','orange','silver','beige','yellow']
                                else :
                                        col = ['blue','cyan','gold','violet','darkblue','green','pink','silver','red','yellow']
                                for i in range(1,11):
                                        for j in range(1,11):
                                                f = list(pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv",skiprows= i, nrows= j))
                                        d = g.append(float(f[5]))
                                        e = h.append(f[0])
                                        X = np.arange(10)
                                pt.bar(h,g,color = col)
                                pt.title("Games Played In Their Carrers(Till 2021-22 Season)")
                                pt.ylabel('Games Played')
                                pt.xlabel('Footballers')
                                pt.show()
                                z = input("Want To Check Something Else In Data Representation ?(Yes/No):")
                        

                        
                        elif c == 14 :
                                print()
                                break
                        else :
                                print("*"*100)
                                print("Oops... I Think You Entered The Wrong Value. Try Again")
                                print("*"*100)
                
                elif b == 3:
                        print('\n')
                        print('__'*50)
                        print(' '* 25,'Manipulation')
                        print()
                        print("1. Add A Column")
                        print("2. Remove A Column")
                        print("3. Add A Row")
                        print('4. Remove A Row')
                        print('5. Go Back')
                        print('__'*50)
                        c = int(input("Enter The Number: "))
                        if c == 1 :
                                cdf= pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv")
                                print(cdf)
                                e = pd.Series([],dtype = 'str')
                                g = input("Enter The Column Name: ")
                                h = ['First','Second','Third','Fourth','Fifith','Sixth','Seventh','Eighth','Nineth','Tenth']
                                for i in range(len(cdf)):
                                        print("Enter The ",end = '')
                                        print(h[i],end ='')
                                        f = input(" Value: ")
                                        e[i] = f
                                j = int(input("Enter The Position Where You Want To Insert The Column (0-14)[0 Meaning Farthest Left]: "))
                                cdf.insert(j,g,e)
                                print(cdf)
                                z = input("Want To Manipulate Something Else ?(Yes/No):")
                        elif c == 2 :
                                cdf= pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv")
                                print(cdf)
                                e = int(input("How Many Columns You Want To Delete (Max : 14): "))
                                g = ['First','Second','Third','Fourth','Fifith','Sixth','Seventh','Eighth','Nineth','Tenth']
                                for i in range(e):
                                        print('Enter The ',end = '')
                                        print(g[i],end = '')
                                        f = input(' [Column Names: Footballers,Goals,Expected Goals,Assists,Expected Assists,Games Played,Goals Per Games Played,Assists Per Games Played,Shots Per 90,Shot On Target Per 90,Shooting Accuracy(in %),Attempted Passes Per Game,Completed Passes Per Game,Progressive Passes Per Game (in yards)](Case Sensitive): ')
                                        cdf.drop([f],axis = 1, inplace = True)
                                print(cdf)
                                z = input("Want To Manipulate Something Else ?(Yes/No):")
                        elif c == 3 :
                                cdf = pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv")
                                print(cdf)
                                e = pd.Series([],dtype = 'str')
                                g = int(input("Enter How Many Rows: "))
                                h = ['Footballers','Goals','Expected Goals','Assists','Expected Assists','Games Played','Goals Per Games Played','Assists Per Games Played','Shots Per 90','Shot On Target Per 90','Shooting Accuracy(in %)','Attempted Passes Per Game','Completed Passes Per Game','Progressive Passes Per Game (in yards)']
                                l = []
                                for i in range(g):
                                        for j in range(0,6):
                                                print("Enter The ",end = '')
                                                print(h[j],end ='')
                                                f = input(" : ")
                                                l.append(f)
                                        m = cdf.append({h[0] : l[0], h[1] : l[1], h[2] : l[2], h[3] : l[3], h[4] : l[4], h[5] : l[5]},ignore_index= True,verify_integrity=False)
                                        l = []
                                print(m)
                                z = input("Want To Manipulate Something Else ?(Yes/No):")
                        elif c == 4 :
                                cdf= pd.read_csv("C:\Python Files\Python Project College\Prolific Scorers Of This Decade.csv",index_col ="Footballers")
                                print(cdf)
                                e = int(input("How Many Rows You Want To Delete (Max : 10): "))
                                g = ['First','Second','Third','Fourth','Fifith','Sixth','Seventh','Eighth','Nineth','Tenth']
                                for i in range(e):
                                        print('Enter The ',end = '')
                                        print(g[i],end = '')
                                        f = input(" Row (Footballer's Name [Case Sensitive]): ")
                                        cdf.drop([f],axis = 0, inplace = True)
                                print(cdf)
                                z = input("Want To Manipulate Something Else ?(Yes/No):")
                        elif c == 5 :
                                print()
                                break
                        else :
                                print("*"*100)
                                print("Oops... I Think You Entered The Wrong Value. Try Again")
                                print("*"*100)
                elif b > 4 :
                        print('\n')
                        print("*"*100)
                        print("Oops... I Think You Entered The Wrong Value. Try Again")
                        print("*"*100)
                        print('\n')
                        a = input("Want To Try Again ?(Yes/No):")
                        break
                elif b == 4:
                        print("Goodbye. Thank You For Checking It Out")
                        break                      
        if b == 4:
                break
        print("Goodbye. Thank You For Checking It Out")
