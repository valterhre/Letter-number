start=97
need_letter=int(input())
def num_to_letter(need_letter):
    li=[]
    li2=[]
    name=[]
    while need_letter:
        li2.append(need_letter%26)
        need_letter=need_letter//26 #целая часть
        li.append(need_letter)
    for ch in li2[::-1]:
        name.append(chr(ch+64))
        abc="".join(name)
    print(abc)
    return abc
def letter_to_num(letter):
    let=[]
    var=0
    for k in letter:
        let.append(ord(k)-64)
    for k in let:
        var=k*26+var*26
    num=int(var/26)
    print(num)
    return num
letter= num_to_letter(need_letter)
letter_to_num(letter)