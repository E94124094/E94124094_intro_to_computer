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
class Dogs(Animals):#建立子類別
    def __init__(self, weight, mood):#初始化函式
        super().__init__(weight, mood)#使用父類別屬性
    def feed(self):#定義方法
        super().feed(self)#使用父類別方法
    def walk(self):
        super().walk(self)
    def bath(self):
        super().bath(self)
    def printf(self, n_feed, n_walk, n_bath):#定義方法
        print("狗狗現在的體重="+str(dog.weight+n_feed*0.2-n_walk*0.2)+"kg，心情 "+str(dog.mood+n_feed*1+n_walk*2-n_bath*2))#輸出狗狗變化後體重及心情
class Cats(Animals):#建立子類別
    def __init__(self, weight, mood):#初始化函式
        super().__init__(weight, mood)#使用父類別屬性
    def feed(self):#定義方法
        super().feed(self)#使用父類別方法
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
