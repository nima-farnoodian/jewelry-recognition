import sys
def post_image(img_file):
    print(img_file)    
    img = open(img_file, 'rb').read()
    new_file_name=img_file[:-4]+".byte"
    bimg=open(new_file_name,"wb")
    bimg.write(img)

if __name__ == '__main__':
    #print('test')
    #print(sys.argv[0])
    post_image(sys.argv[1])
