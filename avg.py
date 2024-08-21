tel=55
hin=55
eng=55
mat=55
sci=55
soc=55
avg=(tel+hin+eng+mat+sci+soc)/6
if tel<35 or hin<35 or eng<35 or mat<35 or sci<35 or soc<35:
    print("Failed")
elif avg>=70 and avg<=100:
    print("A Grade")
elif avg>=50 and avg<70:
    print("B Grade")
else:
    print("C Grade")
