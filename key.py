import hashlib,time
from os import device_encoding
print('加密层数：你密码在最终加密前的复杂程度，层数越高计算越慢')
time.sleep(0.1)
num=int(input('加密层数:\n'))
if num>=500000:
    print('此层数计算时间可能略长')
time.sleep(0.1)
print(f'当前加密层数：{num}')
time.sleep(0.1)
print('KEY：你需要进行加密的密码，无论长短与类型')
key=input('KEY\n').encode(encoding='utf_8')
key2=str(key).replace("b'",'').replace("'",'')
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
d=b
b=str(b).encode(encoding='utf_8')
b=hashlib.sha256(b).hexdigest()[0:-1]
def dd():
    global n,b,d
    last_bfb=0
    x=input('加密已完成\nA:加倍加密 B:得出结果\n')
    if x=='B' or x=='b':
        mb=f'=====================================================================\n{b}\n====================================================================='
        print(mb)
        end_time=time.time()
        x=input(f'加密结束，干翻一切密码\n本次加密时长{int(end_time-start_time)}秒\nA:getlogoutput\n')
        if x=='A' or x=='a':
            msg=f'加密层数：{num}\n关键秘钥：{key2}\n加密后密码：{b}\n密码位数：{len(b)}位\n加密时长：{int(end_time-start_time)}秒\n了解部分算法暴力破解有{36**(num)}种组合\n\n\n\n\n真暴力破解有{36**(num*63)}种组合'
            with open('wlan.log','w',encoding='utf-8') as f:
                f.write(msg)
                f.close()
            with open('key_output.log','w',encoding='utf-8') as f:
                f.write(f'{d}')
                f.close()
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
        time.sleep(0.1)
        c=str(c).encode('utf-8')
        c=str(hashlib.md5(c).hexdigest())
        r=c
        print('弱密码：\n'+c)
        time.sleep(0.1)
        print('弱密码长度：'+str(len(c)))
        time.sleep(0.1)
        c=hashlib.sha1(c.encode('utf-8')).hexdigest()
        z=c
        print('中密码：\n'+c)
        time.sleep(0.1)
        print('中密码长度：'+str(len(c)))
        time.sleep(0.1)
        c=str(hashlib.sha256(c.encode('utf-32')).hexdigest())[0:-1]
        q=c
        print('强密码：\n'+c)
        time.sleep(0.1)
        print('强密码长度：'+str(len(c)))
        time.sleep(0.1)
        end_time=time.time()
        x=input(f'加密结束，干翻一切密码\n本次加密时长{int(end_time-start_time)}秒\nA:getlogoutput\n')
        if x=='a' or x=='A':
            msg=f'加密层数：{num*2}\n关键秘钥：{key2}\n加密后：\n弱密码：{r}\n弱密码长度：{len(r)}\n中密码：{z}\n中密码长度{len(z)}\n强密码：{q}\n强密码长度：{len(q)}\n加密时长：{int(end_time-start_time)}秒\n了解算法暴力破解有{36**(num*2)}种组合\n\n\n\n\n真暴力破解有{36**(num*2*63)}种组合'
            with open('wlan.log','w',encoding='utf-8') as f:
                f.write(msg)
                f.close()
            with open('key_output.log','w',encoding='utf-8') as f:
                f.write(f'{d}')
                f.close()
    else:
        dd()

dd()