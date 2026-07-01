# write vowels and consonants from "hi hello ravi garu" using composition
s="hi hello ravi garu"
vowels ="aeiou"
l=[[ch for ch in s if ch in vowels],[ch for ch in s if ch not in vowels and ch.isalpha()]]
print("1:",1)
vowels=[]
consonants=[]
l1=[[vowels.append(ch) for ch in s if ch in vowels],[consonants.append(ch) for ch in s if ch not in vowels and ch.isalpha()]]
print("vowels:",vowels)
print("consonants:",consonants)

