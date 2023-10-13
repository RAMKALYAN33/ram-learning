# Strig Methods
# if using is method it shows true or false
# upper,lower and casefold are same,
# cap-first letter captial,swapcase--small to capti, capti to small

pyt = "THis IS a New PROject"

print(pyt.upper())
print(pyt.lower())
print(pyt.capitalize())
print(pyt.casefold())
print(pyt.swapcase())

# index,count,title
str="car is a red colour"
print(str.index("a",4,10))
print(str.count("a",1,10))
print(str.title())

# center,isalnum,endswith
name = "james006@"
print(name.center(20,"#"))
print(name.isalnum())
print(name.isalpha())
print(name.endswith("@"))

# expandtabs

val = "c\ta\tr\ts"
print(val.expandtabs())
print(val.expandtabs(3))

# decimal,numeric,digit,zfill--zerofill

num = "34"
print(num.isnumeric())
print(num.isdecimal())
print(num.isdigit())
print(num.zfill(5))

# identifer = starts with a-z or underscores not starts with num
str1 = "_demo87"
print(str1.isidentifier())

# printable, space--only space, title--first letter should in capital
str2 = "Ram"
print(str2.isprintable())
print(str2.istitle())
print(str2.isspace())

# joins

str3 = ("cena","orton","big")
sep = "*"
print(sep.join(str3, ))

# split

str8 = "one##two##thre##four"
print(str8.split("##",2))

# splitlines
st = "one\ntwo\nthree\nfour"
print(st.splitlines(False))

# lstrip--remove starting symbol,rstrip--remove ending symbol
str4 = "@@animated world$$$"
print(str4.lstrip("@"))
print(str4.rstrip("$"))

# replace,rfind,rindex
str5 = "this is w a demo,this is w a expand demo, this a demo value"
print(str5.replace("demo","value",2))
print(str5.rfind("w"))
print(str5.rindex("expand"))

# rjust,startswith
str6 = "stranger things"
print(str6.rjust(30,"B"))
print(str6.startswith("st"))


# rsplit
str7 = "football,cricket,volleyball,hockey,tennis"
print(str7.rsplit(",",2))








