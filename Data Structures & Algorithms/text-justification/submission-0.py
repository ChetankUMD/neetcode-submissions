class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        n = len(words)
        line, length = [], 0
        i=0
        while i < n:
            if length + len(line) + len(words[i]) > maxWidth:
                extra_space = maxWidth - length
                space = extra_space // max(1, (len(line)-1))
                rem = extra_space % max(1,len(line)-1)

                for j in range(max(1, len(line)-1)):
                    line[j] += " "*space
                    if rem:
                        line[j] += " "
                        rem -=1
                
                res.append("".join(line))
                line,length = [],0
        
            line.append(words[i])
            length +=len(words[i])
            i+=1

        last_line = " ".join(line)
        trial = maxWidth - len(last_line)
        res.append(last_line + " "* trial)

        return res  
            