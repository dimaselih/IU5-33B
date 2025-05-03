import sys
import math

class Equation:
    coefs=[]
    def __init__(self):
        try:
            help = sys.argv[1:]
            Equation.coefs = [float(i) for i in help]
            if (len(help)!=3):
                1/0
        except:
            coefs=[]
            for i in range(3):
                while(1):
                    print(f"\nВведите {i+1} коэффициент")
                    try:                        
                        Equation.coefs.append(float(input()))
                        break
                    except:
                        print("\nНеправильный тип коэффициента.")   

    def get_roots(coefs):
        result = []
        discr = pow(Equation.coefs[1],2)-4*Equation.coefs[0]*Equation.coefs[2]
        if (discr < 0):
            return result
        elif (discr == 0):
            result.append(-Equation.coefs[1]/(2*Equation.coefs[0]))
        else:
            result.append((-Equation.coefs[1]+math.sqrt(discr))/(2*Equation.coefs[0]))
            result.append((-Equation.coefs[1]-math.sqrt(discr))/(2*Equation.coefs[0]))
        for i in range(len(result)):
            try:
                result[i]=math.sqrt(result[i])
                if (result[i]!=0):
                    result.append(-result[i])
            except:
                result.pop(i)
        return result

def main():
    answer = Equation().get_roots()
    if (len(answer) == 0):
        print("Нет корней.")
    else:
        print("Корни уравнения: ",*answer)
    


if __name__ == "__main__":
    main()