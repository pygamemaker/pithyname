import random
import pickle
import time
class Map(object):
    def __init__(self,nameinput):
        self.mapname = nameinput
        self.tilesize=int(raw_input("tilesize="))
        self.mapdata=[]
        self.mapwidth=int(raw_input("mapwidth="))
        self.mapheight=int(raw_input("mapheight="))
        self.mapgenerator(self.mapwidth,self.mapheight,self.mapname)
    def gridcontentgenerator(self):
        return ''.join([random.choice('0123456789abcdef') for x in range(6)])
    def mapgenerator(self,mapwidth,mapheight,mapname):
        print "pixelrange=%i,%i"%(self.tilesize*self.mapwidth,self.tilesize*self.mapheight)
        time.sleep(2)
        sizeinmb=(self.mapwidth*self.mapheight)/50697.0849
        print "estimated@:","%.2f"%sizeinmb," mb"
        time.sleep(2)
        print "commencing..."
        for row in range(self.mapwidth):
            self.mapdata.append([])
            #print "creating column:",len(self.mapdata)
            for column in range(self.mapheight):
                self.mapdata[row].append(self.gridcontentgenerator())
                #print "creating row:",len(self.mapdata[row])
    def printmap(self):
        print self.mapdata
    def savemap(self):
        filename = self.mapname+".csv"
        print "saving mapdata to %s" % filename
        with open(filename,"wb") as f:
            pickle.dump(self.mapdata,f)

newmap=Map(raw_input("mapname:"))
#newmap.printmap()
newmap.savemap()
