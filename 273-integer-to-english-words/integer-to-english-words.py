class Solution:
    def numberToWords(self, num: int) -> str:
        if not num: return 'Zero'

        units = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
        tens = ['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        midrange = ['Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']

        p1,p2,p3,p4 = num%1000, num//1000%1000, num//1000000%1000, num//1000000000

        res = []
        def convert(num):
            if num//100:
                res.append(units[num//100])
                res.append('Hundred')
                num%=100
            if num<20 and num>10:
                res.append(midrange[num-11])
                return
            if num//10:
                res.append(tens[num//10])
            if num%10:
                res.append(units[num%10])

        if p4:
            res.append(units[p4])
            res.append('Billion')
        if p3:
            convert(p3)
            res.append('Million')
        if p2:
            convert(p2)
            res.append('Thousand')
        convert(p1)

        return " ".join(res)