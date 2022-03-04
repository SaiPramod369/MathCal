from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
import statistics
from datetime import date
import math
import cmath

# Create your views here.
def home(request):
    return render(request,'home.html')
def binary(request):
    return render(request,'binary.html')
def decimalToBinary(n):
    return bin(n).replace("0b", "")
def bi(request):
    a=int(request.POST["num"])
    b=decimalToBinary(a)
    return render(request,'bi.html',{"nu":b,"num":a})
def decimal(request):
    return render(request,'decimal.html')
def binaryToDecimal(n):
    return int(n,2)
def dl(request):
    a=request.POST["num"]
    b=binaryToDecimal(a)
    return render(request,'dl.html',{"nu":b,"num":a})
def masd(request):
    return render(request,'MaSD.html')
def variance(data):
  n = len(data)
  mean = sum(data) / n
  deviations = [(x - mean) ** 2 for x in data]
  variance = sum(deviations) / n
  return variance


def cal(request):
    a=request.POST["values"]
    b=list(a.split(","))
    b = [int(i) for i in b]
    m=statistics.mean(b)
    m = float("{:.4f}".format(m))
    sd=statistics.stdev(b)
    sd = float("{:.4f}".format(sd))
    v=variance(b)
    v = float("{:.4f}".format(v))
    
    return render(request,'cal.html',{"list":b,"mean":m,"std":sd,"vac":v})
def agecal(request):
    return render(request,'agecal.html')
def calculateAge(birthDate,today):
    age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
    return age
def age(request):
    a=request.POST["dob"]
    b=request.POST["aad"]
    a1=int(a[:4])
    a2=int(a[5:7])
    a3=int(a[8:])
    b1=int(b[:4])
    b2=int(b[5:7])
    b3=int(b[8:])

    age=calculateAge(date(a1,a2,a3),date(b1,b2,b3))
    a=str(a3)+"/"+str(a2)+"/"+str(a1)
    b=str(b3)+"/"+str(b2)+"/"+str(b1)
    return render(request,'age.html',{"dob":a,"aad":b,"age":age})
def calbmi(request):
    return render(request,'calbmi.html')
def bmipos(BMI):
    if BMI <= 18.4:
        return("You are underweight.")
    elif BMI <= 24.9:
         return("You are healthy.")
    elif BMI <= 29.9:
         return ("You are over weight.")
    elif BMI <= 34.9:
         return("You are severely over weight.")
    elif BMI <= 39.9:
        return ("You are obese.")
    else:
        return ("You are severely obese.")

def bmi(request):
    a=int(request.POST["heg"])
    b=int(request.POST["weg"])
    bmi=b/(a/100)**2
    bmi=float("{:.4f}".format(bmi))
    pos=bmipos(bmi)
    
    return render(request,'bmi.html',{"bmi":bmi,"pos":pos,"weg":b,"heg":a})
def logcal(request):
    return render(request,'logcal.html')
def log(request):
    a=int(request.POST["x"])
    base=int(request.POST["b"])
    c=math.log(a,base)
    c=float("{:.4}".format(c))
    return render(request,'log.html',{"x":a,"base":base,"ans":c})
def ctop(request):
    return render(request,'ctop.html')
def cp(request):
    a=int(request.POST["a"])
    b=int(request.POST["b"])
    z=complex(a,b)
    p,q=cmath.polar(z)
    
    p= float("{:.4}".format(p))
    q= float("{:.4}".format(q))
    return render(request,'cp.html',{"a":a,"b":b,"ans1":p,"ans2":q})
def ptoc(request):
    return render(request,'ptoc.html')
def pc(request):
    a=int(request.POST["a"])
    b=int(request.POST["b"])
    p=str(cmath.rect(a,b))
    p=p.split('+')
    q=(p[1])
    q=q[:6]
    p=(p[0])
    p=p[1:7]
   
    return render(request,'pc.html',{"a":a,"b":b,"ans1":p,"ans2":q})