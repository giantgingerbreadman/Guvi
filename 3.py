abra=input()
if(abra == 'a' or abra == 'e' or abra == 'i' or abra == 'o' or abra == 'u' or abra == 'A' or abra == 'E' or abra == 'I' or abra == 'O' or abra == 'U'):
    print("Vowel")
else:
    if(abra.isalpha()) == "True":
        print("Consonant")
    else:
        print("invalid")
        
