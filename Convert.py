wt=int(input())
ht=float(input())
res=wt / float (ht * ht)
if res < 18.5:
 print("Underweight")
elif res>=18.5 and  res<25:
 print("Normal")
elif res>=25 and res<30:
  print("Overweight")
else:
 print("Obesity")