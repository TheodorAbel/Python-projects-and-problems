
name=["Adieu, adieu, to "]
while True:
    try:
        name.append(input("Name: "))
    except EOFError:
       x=len(name)
       song=""
       if x==1:
           break
       elif x==2:
            print(name[0]+name[1])
            break
       elif x==3:
           print(name[0]+" and ".join(name[1:]))
           break

       else:

           song+=name[0]+", ".join(name[1:-1])
           song+=", and "+name[-1]
           print(song)
       break






