import csv
import random
import string

class cromosome:# cromosome
    def __init__(self,emptyplan,pm):
        self.emptyplan = emptyplan
        self.pm = pm
        sl=len(self.emptyplan)
        chromosomestring = ','.join([random.choice(possiblereg()) for n in range(sl)])
        self.chromosomestring = chromosomestring
    def getcromosomestring(self):
        return self.chromosomestring

    def setcromosomestring(self,inpstring):
        self.chromosomestring = inpstring

    def getcromosomefitness(self):
        if constraintpass(self,self.emptyplan)== True:
            # a correct cromosome is generated
            # the position of evaluator function f(emptyplan, self)
            rtt =regtotype()
            ttv =typetovalue()
            genes = self.chromosomestring
            if type(genes)==str:
                out = 0
                for i in range(len((genes.split(",")))):
                    temp = (genes.split(","))[i]
                    out = out + float(ttv[rtt[temp]])
            else:
                for i in range(len((genes))):
                    print(type(genes))
                    print(len((genes)))
                    print(((genes)))
                    temp = genes.__getitem__(i)
                    print(temp)
                    out =out+float(ttv[rtt[temp]])
                print('type non str')
                print('incorrect cromosome is created')


        else:
            # a bad cromosome is generated
            # the fitness of a bad gene is equal to -1
            out=-1
        return out


    def domutation(self):
        x=self.chromosomestring.split(",")
        for i in range(len(x)):
            inlinepro=random.random()
            if inlinepro<=float(self.pm) :
               x[i] = random.choice(possiblereg())
               self.chromosomestring = ','.join(x)
          #  print('mutation occured')

    def docrossover(self, cromosome2):
        temp=self.chromosomestring.split(",")
        randindex=random.randint(2,len(temp))
        temp2 = cromosome2.getcromosomestring().split(",")
        for i in range(randindex,len(temp)):
            temp[i]=temp2[i]
        self.chromosomestring=','.join(temp)
def constraintpass(self, emptyplan):# define constraint?????????????????????????
    return True

def possiblereg():
    with open('initial_reg.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        possibleregisters = []
        for row in readCSV:
            possibleregisters.append(row[0])
    return possibleregisters

def constraint():
    with open('constrain_DOM_1APR2017.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        constraint = {}
        for row in readCSV:
            csize = len(constraint) + 1
            constraint.update({csize: (
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12],
            row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24],
            row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36],
            row[37], row[38], row[39], row[40], row[41], row[42], row[43], row[44], row[45], row[46], row[47], row[48],
            row[49], row[50], row[51], row[52], row[53], row[54])})
    return constraint

def emptyplancalculator():
    islt={}
    with open('sample_plan.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            size = len(islt) + 1
            islt.update({size: (row[0], row[1], row[2], row[3])})
    return islt

def cromosomeselector(cp):
    temparrey = dict(cp.poolarry)
    upperboundcromosome = max(temparrey, key=lambda k: temparrey[k])
    upperbound = temparrey[upperboundcromosome]
    lowerboundcromosome = min(temparrey, key=lambda k: temparrey[k])
    lowerbound = temparrey[lowerboundcromosome]
    pivotrand = random.uniform(lowerbound, upperbound)
    for string, value in temparrey.items():
        temparrey[string] = abs(temparrey[string] - pivotrand)
    selectedcromosome = cromosome(cp.emptyplan, cp.pm)
    selectedcromosome.setcromosomestring(min(temparrey, key=lambda k: temparrey[k]))
    return selectedcromosome

def regtotype():
    rtt={}
    with open('type_reg.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            size = len(rtt) + 1
            rtt.update({row[0]: row[1]})
    return rtt

def typetovalue():
    ttv={}
    with open('type_val.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            size = len(ttv) + 1
            ttv.update({row[0]: row[1]})
    return ttv

class cromosomepool:# cromosomepool
    def __init__(self, popsize,emptyplan,pm):
        self.poolarry = {}
        self.pm = pm
        self.popsize = popsize
        self.emptyplan = emptyplan
        self.cromosomesize = len(emptyplan)
        for i in list(range(int(popsize))):
            inlinecro= cromosome(emptyplan,pm)
            self.poolarry.update({inlinecro.getcromosomestring(): inlinecro.getcromosomefitness()})
    def getoptimumcromosome(self):
        optcromosome=min(self.poolarry, key=lambda k: self.poolarry[k])
        return optcromosome
    def getoptimumvalue(self):
        opco=self.getoptimumcromosome()
        return float(self.poolarry[opco])

    def evolve(self,emptyplan):
        # initialization
        temppool= dict(self.poolarry)
        cafter = 0
        for stringx,valuex in temppool.items():
            cromosome1= cromosome(emptyplan,self.pm)
            cromosome1.setcromosomestring(stringx)
            tempcromosome1=cromosome1
            cromosome2=cromosomeselector(self)
            cbefore=float(tempcromosome1.getcromosomefitness())
            tempcromosome1.docrossover(cromosome2)
            tempcromosome1.domutation()
            cafter=float(cromosome1.getcromosomefitness())

            if (cafter<cbefore) :
            #    print('before')
            #    print(self.poolarry)
                t3 = {tempcromosome1.getcromosomestring(): float(cafter)}


                self.poolarry.update(t3)
            #    print('update')
            #    print(self.poolarry)

                del (self.poolarry[stringx])
             #   print(self.poolarry)
             #   print('after')
        optcromosome = min(self.poolarry, key=lambda k: self.poolarry[k])
        return optcromosome





def main():

        # get number of iterations
        iteration = input("enter number of iterations >>")
        # get probability of mutation
        pm =0.001# input("mutation probability >>")
        # get probability of crossOver
        pc = 0.1#input("crossover probability >>")

        # initialize constraint matrix(dictionary)
        newconstraint = constraint()
        print('constrant matrix was initialized')

        # initialize emptyplan matrix(dictionary)
        emptyplan = emptyplancalculator()
        print('emptyplan matrix was initialized')

        # generate population
        populationSize = input("enter size of population >>")
        pool=cromosomepool(populationSize,emptyplan,pm)
        print('population was initialized')

        # genetic evolution
        print('evolution started')
        for h in range(int(iteration)):
            pool.evolve(emptyplan)
            print('cost per iteration=' + str(float(pool.getoptimumvalue())))
        print('evolution stoped')

        print('optimum cromosome='+pool.getoptimumcromosome())
        print('optimum cost='+str(float(pool.getoptimumvalue())))


if __name__ == "__main__": main()
