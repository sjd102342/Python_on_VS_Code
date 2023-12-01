def calculateNTetrahedralNumber(startvalue, endvalue):
    # Write your code here
    if startvalue >= 1 and (startvalue+1) <= endvalue:
        a = []
        while startvalue <=  endvalue:
            t  =  (startvalue*(startvalue+1)*(startvalue+2))/6
            a.append(int(t))
            startvalue  =  startvalue + 1
        return(a)

startvalue  =  int(input("enter Startvalue: ").strip())
endvalue  =  int(input("enter endvalue: ").strip())
result  =  calculateNTetrahedralNumber(startvalue, endvalue)
print(result)