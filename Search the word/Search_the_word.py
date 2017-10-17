strfromuser = input('enter the string here : ')
wordfromuser = input ('enter the word here :  ')
strfromuser = strfromuser.upper()
wordfromuser = wordfromuser.upper()
if wordfromuser in strfromuser:
    print (f'This word ({wordfromuser}) exists in the given string!')
    spliting = strfromuser.split(wordfromuser)
    wordlength = len(wordfromuser)
    length = len(spliting)
    print(spliting)
    totilength = 0
    i = 0
    for spliter in spliting:
      i += 1
      totilength += len(spliter)
      start = totilength  + 1
      totilength += wordlength
      print (f"{i}.  '{wordfromuser}' starts from {start} and ends at {totilength}")
else:
    print (f'Sorry we are ubale to find the ({wordfromuser}) in the given string')
