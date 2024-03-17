alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

shifted=[]
for position in range (len(alphabet)):
  if (position+shift)>=(len(alphabet)):
    letter= alphabet[(position+shift)-len(alphabet)]
  else:
    letter=alphabet[position+shift]
  
  


def encrypt(text, shift):
  new_index=[]
  for letter in text:
    position= alphabet.index(letter)
    new_position= position+shift
    if ((new_position)<len(alphabet)):
      new_letter=alphabet[new_position]
      new_index.append(new_letter)
    else :
      new_letter=alphabet[(new_position)-len(alphabet)]
      
  print(f'the encoded text is {new_index}')
    
encrypt(text, shift)
   