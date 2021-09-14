import hashlib,time
print('加密层数：你密码在最终加密前的复杂程度，层数越高计算越慢')
time.sleep(0.5)
num=int(input('加密层数:\n'))
if num>=500000:
    print('此层数计算时间可能略长')
time.sleep(0.5)
print(f'当前加密层数：{num}')
time.sleep(0.5)
print('KEY：你需要进行加密的密码，无论长短与类型')
key=input('KEY\n').encode(encoding='utf_8')
time.sleep(0.1)
print('正在进行加密')
start_time=time.time()
b=''
last_bfb=0
n=0
for i in range(num):
    try:
        a=str(hashlib.sha256(key).hexdigest())[n]
        key=str(hashlib.sha256(key).hexdigest()).encode(encoding='utf_8')
        b=b+a
        if n==63:
            n=0
        else:
            n+=1
        bfb=int(i/num*100)
        if bfb!=last_bfb:
            print(f'当前加密进度为：{bfb}%')
        last_bfb=int(i/num*100)
    except:
        print(n,num)
        break
    
b=str(b).encode(encoding='utf_8')
b=hashlib.sha256(b).hexdigest()[0:-1]
def dd():
    global n,b
    last_bfb=0
    x=input('加密已完成\nA:加倍加密 B:得出结果\n')
    if x=='B' or x=='b':
        mb=f'=====================================================================\n{b}\n====================================================================='
        print(mb)
        end_time=time.time()
        input(f'加密结束，干翻一切密码\n本次加密时长{int(end_time-start_time)}秒')
    elif x=='A' or x=='a':
        print('正在翻倍加密中')
        time.sleep(0.1)
        print(f'当前结果：{b}')
        c=''
        b=b.encode('utf-8')
        for i in range(num):
            a=hashlib.sha512(b).hexdigest()[n]
            b=str(hashlib.sha512(b).hexdigest()).encode('utf-8')
            c=c+a
            if n==63:
                n=0
            else:
                n+=1
            bfb=int(i/num*100)
            if bfb!=last_bfb:
                print(f'当前翻倍加密进度为：{bfb}%')
            last_bfb=int(i/num*100)
        time.sleep(0.1)
        print('统计中...')
        time.sleep(0.3)
        c=str(c).encode('utf-8')
        c=str(hashlib.md5(c).hexdigest())
        print('弱密码：\n'+c)
        time.sleep(0.1)
        print('弱密码长度：'+str(len(c)))
        time.sleep(0.1)
        c=hashlib.sha1(c.encode('utf-8')).hexdigest()
        print('中密码：\n'+c)
        time.sleep(0.1)
        print('中密码长度：'+str(len(c)))
        time.sleep(0.1)
        c=str(hashlib.sha256(c.encode('utf-32')).hexdigest())[0:-1]
        print('强密码：\n'+c)
        time.sleep(0.1)
        print('强密码长度：'+str(len(c)))
        time.sleep(0.1)
        end_time=time.time()
        input(f'加密结束，干翻一切密码\n本次加密时长{int(end_time-start_time)}秒')
    else:
        dd()

dd()
