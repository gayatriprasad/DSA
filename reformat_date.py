# 1507. Reformat Date

class Solution:
    def reformatDate(self, date: str) -> str:
        # split date by space ; returns a list 
        dateList = date.split(' ')
        
        # gets date 
        dateVar = dateList[0][:-2]

        # gets month 
        monthVar = dateList[1] 
        monthDict = {'Jan': '01', 'Feb': '02', 
                     'Mar': '03', 'Apr': '04', 
                     'May': '05', 'Jun': '06', 
                     'Jul': '07', 'Aug': '08', 
                     'Sep': '09', 'Oct': '10', 
                     'Nov': '11', 'Dec': '12'}

        # gets year 
        yearVar = dateList[2]

        if int(dateVar) < 10: # Adds 0 to the front of day if day < 10
            dateVar = '0' + dateVar
