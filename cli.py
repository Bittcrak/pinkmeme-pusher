import argparse
from script import pinkmeth
import time

def main():

    parser=argparse.ArgumentParser(description="Push on pinkspace.")
    parser.add_argument('-p','--proxy',type=str, help='Path/to/proxy.txt', required=True)
    parser.add_argument('-u','--url',type=str,help='URL of your listing page', required=True)


    args=parser.parse_args()
    launch(args.url,args.proxy)

def launch(x,y):
    with open(y,'r') as f:
        line_1=f.readline()
        parts=line_1.split(':')
        uname=parts[2]
        pwd=parts[3]
        proxy_list=f.readlines()
        proxy_list=[proxi.strip() for proxi in proxy_list]

        print(proxy_list)
        print(uname, pwd)

    cycle(proxy_list,uname,pwd,x)


def cycle(l,u,p,url):
    for i in l:
        prox=f'https://{u}:{p}@{i}'
        drv=pinkmeth.proxy_req(prox)
        pinkmeth.scroll(drv,url)
        time.sleep(10)
    pinkmeth.leave(drv)     

    
if __name__=="__main__":
    main()