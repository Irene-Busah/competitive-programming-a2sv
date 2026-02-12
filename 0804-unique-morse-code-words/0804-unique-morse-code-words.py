class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",
".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        morseCodeMap = {}
        for i in range(len(alphabets)):
            morseCodeMap[alphabets[i]] = morse_codes[i]
        
        res = {}
        for word in words:
            morseCode = ''
            for char in word:
                if char in morseCodeMap:
                    morseCode += morseCodeMap[char]
                
            if morseCode not in res:
                res[morseCode] = 1
            else:
                res[morseCode] += 1
                
            # res.append(morseCode)
        

        
        return len(res.keys())