class comic:
    def __init__(self):
        self.name = None    #作品名称
        self.author = None  #作者
        self.area = None    #作家所属地区
        self.status = None  #作品连载状态
        self.date = None    #最新更新日期
        self.tags = []       #标签
        self.latest=None    #最新话
        self.url=""
    def save_to_file(self):
        with open(self.url+"./"+self.name+"/info.txt","w+") as f:
            f.write(self.author+"\n");
            f.write(self.area + "\n");
            f.write(self.status + "\n");
            f.write(self.date + "\n");
            for t in self.tags:
                f.write(t+" ")
            f.write("\n")
            f.write(self.latest + "\n");
