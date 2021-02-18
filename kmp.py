# KMP naive algorithme
def kmp(str, searchWord):
    flag = True
    for i in range(0, len(str)-1):
        y = i
        for j in range(i, i+len(searchWord)-1):
            j = y
            for k in range(0, len(searchWord)):
                try :
                    if str[j] == searchWord[k]:
                        flag = True
                    else :
                        flag = False
                    j = j+1
                except:
                    flag = False
                    break
                if not flag:
                    flag2 = False
                    for l in range(j+1, i+len(searchWord)-1):
                        try:
                            if str[l] == searchWord[0]:
                                y = l
                                flag2 = True
                                break
                        except:
                            break
                    if not flag2:
                        y = j+1
                    break

            if flag:
                return True, y

            if not flag:
                break
    if not flag:
        return False, 0

# ------------------------------------------------------------------------------

# KMP with table
class KMP:
    # ref : wikipedia (en)
    def partial(self, pattern):
        ret = [-1]
        i=1
        j=0
        for i in range(1, len(pattern)):
            if pattern[i] == pattern[j]:
                ret.append(ret[j])
            else:
                ret.append(j)
                while j >= 0 and pattern[j] != pattern[i]:
                    j = ret[j]
            j = j+1
        ret.append(j)
        return ret

    # c'est pris sur un repo git trouvé sur les internets \o/
    def search(self, str, keyWord):
        partial = self.partial(keyWord)
        ret = []
        j = 0
        for i in range(len(str)):
            while j > 0 and str[i] != keyWord[j]:
                j = partial[j - 1]
            if str[i] == keyWord[j]: j += 1
            if j == len(keyWord):
                ret.append(i - (j - 1))
                j = partial[j - 1]

        return ret
