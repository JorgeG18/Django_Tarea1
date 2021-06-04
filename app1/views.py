from django.shortcuts import render

   
calculo = []
    #Monto = m, tasa = t, plazo = p

def index(request):
        if request.method == 'POST':
            m = int(request.POST.get('m')) 
            t = int(request.POST.get('t')) 
            p = int(request.POST.get('p')) 
            

            t = t / 100 / 12
            p = p * 12

            cuota = (m * t) / (1 - (1 + t) ** - p)
            total = cuota * p

            calculo.append({
                'm': m,
                't': t,
                'p': p,
                'cuota': cuota,
                'total': total
            })

            ctx = {
                'calculo':calculo
            }
            return render(request, 'calculo/index.html', ctx)
        else :
            ctx = {
                'calculo' : calculo
            }
            return render(request,'calculo/index.html',ctx)