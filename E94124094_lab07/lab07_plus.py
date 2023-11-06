class Animals():#建立父類別
    def __init__(self, weight, mood):#初始化函式
        self.weight=weight#定義屬性
        self.mood=mood
    def feed(self):#定義方法
        pass#不執行動作
    def walk(self):
        pass
    def bath(self):
        pass
class Dogs(Animals):#建立Animals的子類別
    def __init__(self, weight, mood):#初始化函式
        super().__init__(weight, mood)#繼承父類別屬性
    def feed(self):#定義方法
        super().feed(self)#繼承父類別方法
    def walk(self):
        super().walk(self)
    def bath(self):
        super().bath(self)
    def printf(self, n_feed, n_walk, n_bath):#定義方法
        print("狗狗現在的體重="+str(dog.weight+n_feed*0.2-n_walk*0.2)+"kg，心情 "+str(dog.mood+n_feed*1+n_walk*2-n_bath*2))#輸出狗狗變化後體重及心情
class Cats(Animals):#建立Animals的子類別
    def __init__(self, weight, mood):#初始化函式
        super().__init__(weight, mood)#繼承父類別屬性
    def feed(self):#定義方法
        super().feed(self)#繼承父類別方法
    def walk(self):
        super().walk(self)
    def bath(self):
        super().bath(self)
    def printf(self, n_feed, n_walk, n_bath):#定義方法
        print("貓貓現在的體重="+str(cat.weight+n_feed*0.1-n_walk*0.1)+"kg，心情 "+str(cat.mood+n_feed*1-n_walk*1-n_bath*2))#輸出貓貓變化後體重及心情
dog=Dogs(4.8, 65)#建立物件並執行其屬性
cat=Cats(8.2, 60)#建立物件並執行其屬性
dog.printf(18, 10, 4)#令物件執行其方法
cat.printf(40, 7, 1)#令物件執行其方法

class Shiba(Dogs):#建立Dogs的子類別
    def __init__(self, weight, mood):#初始化函式
        super().__init__(weight, mood)#繼承父類別屬性
    def feed(self, n_feed):#定義方法
        self.n_feed=n_feed
    def walk(self, n_walk):
        self.n_walk=n_walk
    def bath(self, n_bath):
        self.n_bath=n_bath
    def printf(self, n_feed, n_walk, n_bath):#定義方法
        shiba.weight = shiba.weight+n_feed*0.3-n_walk*0.2#定義參數
        shiba.mood = shiba.mood+n_feed*5+n_walk*2-n_bath*2
        print("柴犬現在的體重="+str(shiba.weight)+"kg，心情 "+str(shiba.mood))#輸出柴犬變化後體重及心情
    def mood_constraint(self, constr):#定義方法
        self.constr = constr
        print("mood最高只能為" ,self.constr )#輸出mood上限
        if shiba.mood>90:#用if判斷mood值
            shiba.mood = 90
            print("所以，柴犬現在的心情為", self.mood)#輸出最終mood值

shiba = Shiba(5, 70) #建立物件並執行其屬性
shiba.printf(20, 10, 3) #令物件執行其方法
shiba.mood_constraint(90)
