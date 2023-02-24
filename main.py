import time,sys,re,random

def a(text,velocity):#无用
    sys.stdout.flush() #把缓冲区全部输出
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(velocity)
    print()

def oboprint(text,velocity):#横向逐字输出 text:输出内容 velocity:速度（输出每字间隔时间 单位：秒）
    sys.stdout.flush()
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(velocity)
    print()
def oboprint(text):#横向逐字输出（速度：每字间隔0.5秒） text:输出内容
    sys.stdout.flush()
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.5)
    print()
def vprint_instent(text,quantity):#竖向快速输出 text:输出内容 quantity:每行字数
    s = text
    quantity = str(quantity)
    s = re.sub(r"(.{"+quantity+"})", "\\1\r", s)
    print(s)
def vprint_instent(text):#竖向快速输出（每行1字符） text:输出内容
    s = text
    s = re.sub(r"(.{1})", "\\1\r", s)
    print(s)
def vprint_obo(text,quantity,velocity):#竖向逐字输出 text:输出内容 quantity:每行字数 velocity:速度（输出每行间隔时间 单位：秒）
    s = text
    quantity = str(quantity)
    s = re.sub(r"(.{"+quantity+"})", "\\1\r", s)
    oboprint(s,velocity)
def underline(text):
    underline = '\033[4m'
    end = '\033[0m'
    print(underline + text + end)

def underline(text,velocity): #下划线文字 text:输出内容 velocity:速度（每字间隔时间 单位：秒）
    underline = '\033[4m'
    end = '\033[0m'
    oboprint(underline + text + end,velocity)

def bigword(text): #英文艺术字 text:英文内容
    # 仅支持输入英文
    name = text

    lngth = len(name)
    
    l = ""
    
    for x in range(0, lngth):
    
        c = name[x]
        
        c = c.upper()
    
        if (c == "A"):
        
            print("..######..\n..#....#..\n..######..", end = " ")
            
            print("\n..#....#..\n..#....#..\n\n")
        
        elif (c == "B"):
        
            print("..######..\n..#....#..\n..#####...", end = " ")
            
            print("\n..#....#..\n..######..\n\n")
        
        elif (c == "C"):
        
            print("..######..\n..#.......\n..#.......", end = " ")
            
            print("\n..#.......\n..######..\n\n")
        
        elif (c == "D"):
        
            print("..#####...\n..#....#..\n..#....#..", end = " ")
            
            print("\n..#....#..\n..#####...\n\n")
        
        elif (c == "E"):
        
            print("..######..\n..#.......\n..#####...", end = " ")
            
            print("\n..#.......\n..######..\n\n")
        
        elif (c == "F"):
        
            print("..######..\n..#.......\n..#####...", end = " ")
            
            print("\n..#.......\n..#.......\n\n")
        
        elif (c == "G"):
        
            print("..######..\n..#.......\n..#.####..", end = " ")
            
            print("\n..#....#..\n..#####...\n\n")
        
        elif (c == "H"):
        
            print("..#....#..\n..#....#..\n..######..", end = " ")
            
            print("\n..#....#..\n..#....#..\n\n")
        
        elif (c == "I"):
        
            print("..######..\n....##....\n....##....", end = " ")
            
            print("\n....##....\n..######..\n\n")
        
        elif (c == "J"):
        
            print("..######..\n....##....\n....##....", end = " ")
            
            print("\n..#.##....\n..####....\n\n")
        
        elif (c == "K"):
        
            print("..#...#...\n..#..#....\n..##......", end = " ")
            
            print("\n..#..#....\n..#...#...\n\n")
        
        elif (c == "L"):
        
            print("..#.......\n..#.......\n..#.......", end = " ")
            
            print("\n..#.......\n..######..\n\n")
        
        elif (c == "M"):
        
            print("..#....#..\n..##..##..\n..#.##.#..", end = " ")
            
            print("\n..#....#..\n..#....#..\n\n")
        
        elif (c == "N"):
            
            print("..#....#..\n..##...#..\n..#.#..#..", end = " ")
            
            print("\n..#..#.#..\n..#...##..\n\n")
        
        elif (c == "O"):
        
            print("..######..\n..#....#..\n..#....#..", end = " ")
            
            print("\n..#....#..\n..######..\n\n")
        
        elif (c == "P"):
        
            print("..######..\n..#....#..\n..######..", end = " ")
            
            print("\n..#.......\n..#.......\n\n")
        
        elif (c == "Q"):
            
            print("..######..\n..#....#..\n..#.#..#..", end = " ")
            
            print("\n..#..#.#..\n..######..\n\n")
        
        elif (c == "R"):
        
            print("..######..\n..#....#..\n..#.##...", end = " ")
            
            print("\n..#...#...\n..#....#..\n\n")
        
        elif (c == "S"):
        
            print("..######..\n..#.......\n..######..", end = " ")
            
            print("\n.......#..\n..######..\n\n")
        
        elif (c == "T"):
            
            print("..######..\n....##....\n....##....", end = " ")
            
            print("\n....##....\n....##....\n\n")
        
        elif (c == "U"):
        
            print("..#....#..\n..#....#..\n..#....#..", end = " ")
            
            print("\n..#....#..\n..######..\n\n")
        
        elif (c == "V"):
            
            print("..#....#..\n..#....#..\n..#....#..", end = " ")
            
            print("\n...#..#...\n....##....\n\n")
        
        elif (c == "W"):
        
            print("..#....#..\n..#....#..\n..#.##.#..", end = " ")
            
            print("\n..##..##..\n..#....#..\n\n")
        
        elif (c == "X"):
        
            print("..#....#..\n...#..#...\n....##....", end = " ")
            
            print("\n...#..#...\n..#....#..\n\n")
        
        elif (c == "Y"):
        
            print("..#....#..\n...#..#...\n....##....", end = " ")
            
            print("\n....##....\n....##....\n\n")
        
        elif (c == "Z"):
        
            print("..######..\n......#...\n.....#....", end = " ")
            
            print("\n....#.....\n..######..\n\n")
        
        elif (c == " "):
        
            print("..........\n..........\n..........", end = " ")
            
            print("\n..........\n\n")
        
        elif (c == "."):
            
            print("----..----\n\n")
        
        

# 一大堆字体颜色代码
def black(text,front):
    print("\033[30m" + text + "\033[0m")
def black(text,back,velocity):
    a("\033[30m" + text + "\033[0m",velocity)
def black(text,back):
    print("\033[40m" + text + "\033[0m")
def black(text,front,velocity):
    a("\033[30m" + text + "\033[0m",velocity)
def red(text,back):
    print("\033[31m"+text+"\033[0m")
def red(text,back,velocity):
    a("\033[31m"+text+"\033[0m",velocity)
def red(text,front):
    print("\033[41m"+text+"\033[0m")
def red(text,front,velocity):
    a("\033[41m"+text+"\033[0m")
def green(text,back):
    print("\033[32m"+text+"\033[0m")
def green(text,back,velocity):
    a("\033[32m"+text+"\033[0m",velocity)
def green(text,front):
    print("\033[42m"+text+"\033[0m")
def green(text,front,velocity):
    a("\033[42m"+text+"\033[0m",velocity)
def yellow(text,back):
    print("\033[33m"+text+"\033[0m")
def yellow(text,back,velocity):
    a("\033[33m"+text+"\033[0m",velocity)
def yellow(text,front):
    print("\033[43m"+text+"\033[0m")
def yellow(text,front,velocity):
    a("\033[43m"+text+"\033[0m",velocity)
def blue(text,back):
    print("\033[34m"+text+"\033[0m")
def blue(text,back,velocity):
    a("\033[34m"+text+"\033[0m",velocity)
def blue(text,front):
    print("\033[44m"+text+"\033[0m")
def blue(text,front,velocity):
    a("\033[44m"+text+"\033[0m",velocity)
def purple(text,back):
    print("\033[35m"+text+"\033[0m")
def purple(text,back,velocity):
    a("\033[35m"+text+"\033[0m",velocity)
def purple(text,front):
    print("\033[45m"+text+"\033[0m")
def purple(text,front,velocity):
    a("\033[45m"+text+"\033[0m",velocity)
def cyan(text,back):
    print("\033[36m"+text+"\033[0m")
def cyan(text,back,velocity):
    a("\033[36m"+text+"\033[0m",velocity)
def cyan(text,front):
    print("\033[46m"+text+"\033[0m")
def cyan(text,front,velocity):
    a("\033[46m"+text+"\033[0m",velocity)
def white(text,back):
    print("\033[37m"+text+"\033[0m")
def white(text,back,velocity):
    a("\033[37m"+text+"\033[0m",velocity)
def white(text,front):
    print("\033[47m"+text+"\033[0m")
def white(text,front,velocity):
    a("\033[47m"+text+"\033[0m",velocity)
#随机颜色（单句）
def pdcs(text,t):
    col=random.randint(1,2)
    if col==1:
        co=str(random.randint(1,6))
        for a in text:
            sleep(t)
            print("\033[3"+co+"m"+a+"\033[0m",end="",flush = True)
            sys.stdout.flush()
        print("",end="\n")
            
    if col==2:
        co=str(random.randint(1,6))
        for a in text:
            time.sleep(t)
            print("\033[9"+co+"m"+a+"\033[0m",end="",flush = True)
            sys.stdout.flush()
        print("",end="\n")
#随机颜色（每字）
def pen(text=None):
    if text == None:
        print()
    else:
        for i in text:
            print("\033[1;%sm"%random.randint(31,36)+i+"\033[0m",end="")
            sys.stdout.flush()
            time.sleep(0.1/2)
        print()
        time.sleep(1)
