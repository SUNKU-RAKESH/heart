from django.shortcuts import render
from django.http import HttpResponse
from joblib import load

model = load('./savedModels/model.joblib')


def predictor(request):
    if request.method == 'POST':
        param1 = float(request.POST.get('param1'))
        param2 = float(request.POST.get('param2'))
        param3 = float(request.POST.get('param3'))
        param4 = float(request.POST.get('param4'))
        param5 = float(request.POST.get('param5'))
        param6 = float(request.POST.get('param6'))
        param7 = float(request.POST.get('param7'))
        param8 = float(request.POST.get('param8'))
        param9 = float(request.POST.get('param9'))
        param10 = float(request.POST.get('param10'))
        param11 = float(request.POST.get('param11'))
        param12 = float(request.POST.get('param12'))
        param13 = float(request.POST.get('param13'))

        y_pred = model.predict([[param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, param11, param12, param13]])
        print(y_pred)
        if(y_pred[0] == 0):
            result = "The Person does not have a Heart Disease"
        elif(y_pred[0] == 1):
            result = "The Person has Heart Disease"
        #result1 = Blood_test_result[pred[0]]
        #result2 = Genetic_Disorder[pred[1]]
        #result3 = Disorder_Subclass[pred[2]]

        return render(request, 'main.html', {'result': result})

    return render(request, 'main.html')
