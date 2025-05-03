import sys
import math

def get_coefs():
    coefs = []
    try:
        help = sys.argv[1:]
        coefs = [float(i) for i in help]
        if (len(help)!=3):
            1/0
    except:
        coefs=[]
        for i in range(3):
            while(1):
                print(f"\nВведите {i+1} коэффициент")
                try:                        
                    coefs.append(float(input()))
                    break
                except:
                    print("\nНеправильный тип коэффициента.")    
    return coefs


def get_roots(coefs):
    result = []
    discr = pow(coefs[1],2)-4*coefs[0]*coefs[2]
    if (discr < 0):
        return result
    elif (discr == 0):
        result.append(-coefs[1]/(2*coefs[0]))
    else:
        result.append((-coefs[1]+math.sqrt(discr))/(2*coefs[0]))
        result.append((-coefs[1]-math.sqrt(discr))/(2*coefs[0]))
    for i in range(len(result)):
        try:
            result[i]=math.sqrt(result[i])
            if (result[i]!=0):
                result.append(-result[i])
        except:
            result.pop(i)
    return result

def main():
    answer = get_roots(get_coefs())
    if (len(answer) == 0):
        print("Нет корней.")
    else:
        print("Корни уравнения: ",*answer)
    


if __name__ == "__main__":
    main()