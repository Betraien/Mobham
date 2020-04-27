import pyarabic.araby as araby
alphapet = "ابتثجحخدذرزسشصضطظعغفقكلمنهوي"
def modInverse(a, m) : 
    a = a % m
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

def fixTheText(text_array):
    for i in range(len(text_array)):
        if (text_array[i]=="ة"):
            text_array[i] = "ه"
        if (text_array[i]=="ى"):
            text_array[i] = "ي"
        if (text_array[i]=="ئ"):
            text_array[i] = "ي"
        if (text_array[i]=="إ"):
            text_array[i] = "ا"
        if (text_array[i]=="أ"):
            text_array[i] = "ا"
        if (text_array[i]=="آ"):
            text_array[i] = "ا"
        if (text_array[i]=="ء"):
            text_array[i] = "ا"
        if (text_array[i]=="ؤ"):
            text_array[i] = "و"
        
    return text_array
        

def handleInput(text): 
    y = araby.strip_tashkeel(text)
    inputArray = []
    for i in y:
         inputArray.append(i)
    return inputArray
        
def convertInputToArabicPosition(input):
    inputToNumber = []
    for i in input:
        if i == " ":
            inputToNumber.append(-1)
        for x in range(len(alphapet)):
            if i == alphapet[x]:
                inputToNumber.append(x)
    return inputToNumber

def cypher(input, key, key2):
    processed_input=convertInputToArabicPosition(fixTheText(handleInput(input)))
    keysA = [1, 3, 5, 9, 11, 13, 15, 17, 19, 23, 25, 27]#
    keyB = key%28
    encryptedTextArray= []
    for i in range(len(processed_input)):
        if processed_input[i] != -1:
             processed_input[i] = ((processed_input[i] * keysA[key2%len(keysA)])+(keyB))%(28)
    for x in processed_input:
        if x != -1:
            for y in range(len(alphapet)):
                if x == y:
                    encryptedTextArray.append(alphapet[y])
                    break
        else:
            encryptedTextArray.append(" ")
    print("before",str(encryptedTextArray),len(encryptedTextArray))
    encryptedText = ""
    encryptedText = encryptedText.join(encryptedTextArray)
    return encryptedTextArray

def decypher(text, key, key2):
    encrypted_text_Array=convertInputToArabicPosition(fixTheText(text))
    keyB = key%28
    keysInverse = [1, 19, 17, 25, 23, 13, 15, 5, 3, 11, 9, 27]
    decryptedTextArray= []
    for i in range(len(encrypted_text_Array)):
        if encrypted_text_Array[i] != -1:
             encrypted_text_Array[i] = ((encrypted_text_Array[i] - (keyB) ) * keysInverse[key2%len(keysInverse)])%(28)
    for x in encrypted_text_Array:
        if x != -1:
            decryptedTextArray.append(alphapet[x])
        else:
            decryptedTextArray.append(" ")
    decryptedText = ""
    decryptedText = decryptedText.join(decryptedTextArray)
    return decryptedText

