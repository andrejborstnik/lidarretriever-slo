#evode
import urllib.request as url
import urllib.error
import sys 
import getopt

def urlExists(urladdr):
    print("Trying ... {0}".format(urladdr))
    try:
        code = url.urlopen(urladdr).getcode()
        return(True)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("Missing ...")
    
    return(False)

"""retrieveLidar"""
def retrieveLidar(x1, y1, x2, y2):
    xmin = min(x1, x2)
    ymin = min(y1, y2)

    xmax = max(x1, x2)
    ymax = max(y1, y2)

    lastblok = 10

    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            print(x, y)
            b = lastblok            
            urladdr = "http://gis.arso.gov.si/lidar/dmr1/b_{2}/D48GK/GK1_{0}_{1}.asc".format(x, y, b)
            if urlExists(urladdr):
                urlE = True;
                print("Found!")
            else:
                b = 9
                urlE = False

                while b < 100 and urlE == False:                    
                    b = b + 1
                    urladdr = "http://gis.arso.gov.si/lidar/dmr1/b_{2}/D48GK/GK1_{0}_{1}.asc".format(x, y, b)
                    urlE = urlExists(urladdr)                    
                
                if urlE == True:                    
                    lastblok = b
                    print("Found!")
                else:
                    print("\n\n\nFile NOT FOUND!\n\n\n")
            
            # download
            if (urlE == True):
                print("Retrieving file ...")
                downfile = url.URLopener()
                downfile.retrieve(urladdr, "raw/GK_{0}_{1}.asc".format(x, y))
            # http://gis.arso.gov.si/lidar/gkot/laz/b_22/D48GK/GK_519_124.laz

"""main"""
def main(argv):   
    try:
        opts, args = getopt.getopt(argv, "hx:y:w:z:", ["x1=", "x2=", "y1=", "y2="])
    except getopt.GetoptError:
        print('lidar-evode.py -x <minX> -y <minY> -w <maxX> -z <maxY>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('lidar-evode.py -x1 <minX> -x2 <maxX> -y1 <minY> -y2 <maxY>')
            sys.exit()
        elif opt in ("-x", "--x1"):
            x1 = int(arg)
        elif opt in ("-y", "--x2"):
            x2 = int(arg)
        elif opt in ("-w", "--y1"):
            y1 = int(arg)
        elif opt in ("-z", "--y2"):
            y2 = int(arg)

    if 'x1' in vars() and 'x2' in vars() and 'y1' in vars() and 'y2' in vars():
        print('X = ', x1, x2, '   Y = ', y1, y2)
        retrieveLidar(x1, y1, x2, y2)
    else:
        print('lidar-evode.py -x1 <minX> -x2 <maxX> -y1 <minY> -y2 <maxY>')

main(sys.argv[1:])
