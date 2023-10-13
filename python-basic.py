# Strig Methods
# if using is method it shows true or false
# upper():Python String upper () method converts all lowercase characters in a string into uppercase characters and returns it.
# lower():The lower () method is a string method that returns a new string, completely lowercase.
# casefold():The .casefold () method returns a copy of a string with all characters in lowercase.
# capitalize():capitalize()is a string method used to convert the first character of the input string to uppercase, and rest to lowercase, if any.
# swapcase():swapcase () method converts all uppercase characters to lowercase and vice versa of the given string and returns it.

pyt = "THis IS a New PROject"

print(pyt.upper())
print(pyt.lower())
print(pyt.capitalize())
print(pyt.casefold())
print(pyt.swapcase())

# index():The index () method in Python is a string method that is used to find the position of a substring within a string.
# count():count () function is an inbuilt function in Python programming language that returns the number of occurrences of a substring in the given string.
# title():The title () method is a built-in Python string method that returns a new string with the first character of each word capitalized, and all other characters in lowercase. It is used to convert a string into title case format.
str="car is a red colour"
print(str.index("a",4,10))
print(str.count("a",1,10))
print(str.title())

# center(): center () method creates and returns a new string that is padded with the specified character.
# isalnum():The .isalnum () string method takes in a string and returns True if all the characters are alphanumeric ( A-Z, a-z, 0-9 ). Otherwise, it returns False if the string contains any non-alphanumeric characters (e.g. @ # $ % - * ). This method does not have any parameters.
# endswith():The endswith () is a string method that returns True if a string ends with another string. Otherwise, it returns False.
name = "james006@"
print(name.center(20,"#"))
print(name.isalnum())
print(name.isalpha())
print(name.endswith("@"))

# expandtabs():The expandtabs () method sets the tab size to the specified number of whitespaces. Optional. A number specifying the tabsize. Default tabsize is 8

val = "c\ta\tr\ts"
print(val.expandtabs())
print(val.expandtabs(3))

# isdecimal():String isdecimal () function returns true if all characters in a string are decimal, else it returns False.
# isnumeric(): The isnumeric() method checks if all the characters in the string are numeric.
# isdigit():Python String isdigit() method The stringisdigit()method returns Trueif: 1. All characters in the string are digits and 2. The string has at least one character. Otherwise, it returns False.
# zfill():Python String zfill () method returns a copy of the string with ‘0’ characters padded to the left side of the given string.

num = "34"
print(num.isnumeric())
print(num.isdecimal())
print(num.isdigit())
print(num.zfill(5))

# isidentifer():string isidentifier () method to check whether a string is a valid identifier or not. It cannot be a reserved python keyword. It should not contain white space. It can be a combination of A-Z, a-z, 0-9, or underscore. It should start with an alphabet character or an underscore ( _ ).
# starts with a-z or underscores not starts with num
str1 = "_demo87"
print(str1.isidentifier())

# isprintable():String isprintable () is a built-in method used for string handling. The isprintable () method returns “True” if all characters in the string are printable or the string is empty, Otherwise, It returns “False”.
# isspace():String isspace () is a built-in method used for string handling. The isspace () method returns “True” if all characters in the string are whitespace characters, Otherwise, It returns “False”.
# title():String istitle () Method is a built-in string function that returns True if all the words in the string are title cased, otherwise returns False.
str2 = "Ram"
print(str2.isprintable())
print(str2.istitle())
print(str2.isspace())

# joins():The string join () method returns a string by joining all the elements of an iterable (list, string, tuple), separated by the given separator.

str3 = ("cena","orton","big")
sep = "*"
print(sep.join(str3, ))

# split():String split () method in Python split a string into a list of strings after breaking the given string by the specified separator.

str8 = "one##two##thre##four"
print(str8.split("##",2))

# splitlines():This method returns a list with all the lines in string, optionally including the line breaks (if num is supplied and is true). When the method is called on the string containing the line breaks, the output is returned as the split string.
st = "one\ntwo\nthree\nfour"
print(st.splitlines(False))

# lstrip():String lstrip () method returns a copy of the string with leading characters removed (based on the string argument passed). If no argument is passed, it removes leading spaces.
# remove starting symbol,
# rstrip():he rstrip () method in Python is used to remove right-side whitespace characters from a string, such as \ , \\r, \, \\f, space.
# remove ending symbol
str4 = "@@animated world$$$"
print(str4.lstrip("@"))
print(str4.rstrip("$"))

# replace():replace () in Python returns a copy of the string where occurrences of a substring are replaced with another substring.
# rfind():String rfind () Method - The Python String rfind () method searches for the starting index of a last occurrence of a specified substring is found in an original string.
# rindex():String rindex () method is a built-in function that returns the substring’s highest index (last occurrence) in a given string.
str5 = "this is w a demo,this is w a expand demo, this a demo value"
print(str5.replace("demo","value",2))
print(str5.rfind("w"))
print(str5.rindex("expand"))

# rjust():String rjust () method returns a new string of a given length after substituting a given character on the left side of the original string.
# startswith(): String startswith () method returns True if a string starts with the specified prefix (string). If not, it returns False using Python.
str6 = "stranger things"
print(str6.rjust(30,"B"))
print(str6.startswith("st"))


# rsplit():String.rsplit () is used to split this string by given separator string into specified maximum number of items. rsplit () splits the string from right side. rsplit () method returns the parts as a list of strings.
str7 = "football,cricket,volleyball,hockey,tennis"
print(str7.rsplit(",",2))








