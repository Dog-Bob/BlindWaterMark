import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
from myMark import *
from PIL import Image,ImageTk

class GUI():
    originPic=''
    markPic=''
    scaleFactor=0
    widthPic=200
    alpha=3.0

    def __init__(self):
        self.__window=tk.Tk()
        self.__window.title('加加林   ——加数字水印')
        self.width=800
        self.height=650
        self.__window.geometry(str(self.width)+'x'+str(self.height))

        pass

    #选择文件框
    def select(self):
        filePath=filedialog.askopenfile(title='选择要加水印的图片',filetypes=[('','.png'),('','.jpeg'),('','.tif'),('','.bmp'),('','.jpg'),('','.raw')])
        if(filePath):
            # print(filePath)
            # print(filePath.name)
            self.originPic=filePath.name
            self.originPic=self.originPic.split('/')[-1]#取文件名
            print(self.originPic)
            #展示选择的图片
            image=Image.open(self.originPic)
            Width=self.widthPic#先缩放
            scaleFactor=Width/float(image.width)
            newWidth=int(image.width*scaleFactor)
            newHeight=int(image.height*scaleFactor)
            resizeImage=image.resize((newWidth,newHeight))
            self.photoOrigin=ImageTk.PhotoImage(resizeImage)#photo会被回收，要设置为不会被回收的
            l0=tk.Label(self.__window,image=self.photoOrigin)
            l0.grid(row=2,column=0)
    def selectMark(self):
        filePath=filedialog.askopenfile(title='选择要加的水印',filetypes=[('','.png'),('','.jpeg'),('','.tif'),('','.bmp'),('','.jpg'),('','.raw')])
        if(filePath):
            self.markPic=filePath.name
            self.markPic=self.markPic.split('/')[-1]#取文件名
            print(self.markPic)
            #展示选择的水印
            #缩放scaleFactor倍
            imageMark=Image.open(self.markPic)
            Width=self.widthPic
            scaleFactor=Width/float(imageMark.width)
            newWidth=int(imageMark.width*scaleFactor)
            newHeight=int(imageMark.height*scaleFactor)
            resizeImageMark=imageMark.resize((newWidth,newHeight))
            self.photoMark=ImageTk.PhotoImage(resizeImageMark)#photo会被回收，要设置为不会被回收的
            l1=tk.Label(self.__window,image=self.photoMark)
            l1.grid(row=2,column=1)
            encode(self.originPic,self.markPic,self.alpha)
            tk.messagebox.showinfo(title='添加完成', message='水印添加完成,请在当前目录查看')

            #加完水印的图片
            image=Image.open('encoded.png')
            Width=self.widthPic*3
            scaleFactor=Width/float(image.width)
            newWidth=int(image.width*scaleFactor)
            newHeight=int(image.height*scaleFactor)
            resizeImage=image.resize((newWidth,newHeight))
            self.photoEncodePic=ImageTk.PhotoImage(resizeImage)#photo会被回收，要设置为不会被回收的
            l2=tk.Label(self.__window,image=self.photoEncodePic)
            l2.grid(row=3,column=0,columnspan=3,pady=10)

    def decode(self):
        filePath=filedialog.askopenfile(title='选择要提取水印的图片',filetypes=[('','.png'),('','.jpeg'),('','.tif'),('','.bmp'),('','.jpg'),('','.raw')])
        if(filePath):
            # print(filePath)
            # print(filePath.name)
            self.encodePic=filePath.name
            self.encodePic=self.encodePic.split('/')[-1]#取文件名
            print(self.encodePic)
            decode(self.originPic,self.encodePic,self.alpha)
            #展示选择的图片
            image=Image.open(self.encodePic)
            Width=self.widthPic#先缩放
            scaleFactor=Width/float(image.width)
            newWidth=int(image.width*scaleFactor)
            newHeight=int(image.height*scaleFactor)
            resizeImage=image.resize((newWidth,newHeight))
            self.photoEncode=ImageTk.PhotoImage(resizeImage)#photo会被回收，要设置为不会被回收的
            l3=tk.Label(self.__window,image=self.photoEncode)
            l3.grid(row=2,column=2)
            tk.messagebox.showinfo(title='提取完成', message='水印提取完成,请在当前目录查看')
            #提取的水印
            image_extract_mark=Image.open('markExtract.png')
            Width=self.widthPic*3
            scaleFactor=Width/float(image_extract_mark.width)
            newWidth=int(image_extract_mark.width*scaleFactor)
            newHeight=int(image_extract_mark.height*scaleFactor)
            resizeImage2=image_extract_mark.resize((newWidth,newHeight))
            self.photo_extract_mark=ImageTk.PhotoImage(resizeImage2)#photo会被回收，要设置为不会被回收的
            l4=tk.Label(self.__window,image=self.photo_extract_mark)
            l4.grid(row=3,column=0,columnspan=3,pady=10)

    def show(self):
        self.s=tk.Scale(self.__window,label=f'',from_=3,to=20,orient=tk.HORIZONTAL,length=300,showvalue=False,tickinterval=2,resolution=0.1,command=self.slite_mark)
        self.s.grid(row=1,column=1,columnspan=2)
        self.slite_l=tk.Label(self.__window,text='水印能量系数:3.0')
        self.slite_l.grid(row=1,column=0)
        k=9
        btn=tk.Button(self.__window,text='选择原图',command=self.select)
        btn.grid(row=0,column=0,padx=self.width//k,pady=5)
        btn2=tk.Button(self.__window,text='选择水印',command=self.selectMark)
        btn2.grid(row=0,column=1,padx=self.width//(k-2),pady=5)
        btn3=tk.Button(self.__window,text='选择要提取的图片',command=self.decode)
        btn3.grid(row=0,column=2,padx=self.width//k,pady=5)
        self.__window.mainloop()

    def slite_mark(self,v):
        #print(type(v))
        self.alpha=float(v)
        self.slite_l.config(text="水印能量系数:"+str(v))
        print(self.alpha)


if __name__=='__main__':
    g=GUI()
    g.show()






