import random
import time
import os

# //// TIMSORT PRO POLE /////////////////////////////////////////////////////////////////////// 
# 

def clearConsole(): # Čistění konzole
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

#

def InsertionSort(pole):    # Worst: O(n^2), Average: O(n^2)

    for j in range (1, len(pole)):
                    
        for i in range(j, 0, -1):           # prochazeni pole j a snizuju se
            if pole[i] < pole[i - 1]:       # porovnavani je-li element vetsi jak predchozi je-li vetsi tak se prehodi
                t = pole[i]
                pole[i] = pole[i - 1]
                pole[i - 1]= t
            else:                           # neni-li vetsi tak je uz ve roztridene casti > break
                break
            i = i - 1
    return pole

#
# pouze Merge

def Merge(aPole, bPole):  # Worst: O(n log(n)), Average: O(n log(n))

    # aPole je prvni pole ktere budeme spojovat
    # bPole je druhe
    
    a = 0           # pomocna promena pro delku prvniho pole
    b = 0           # druha pomocna promena
    cPole = []      # vysledne tridene pole

    while a < len(aPole) and b < len(bPole):    
        if aPole[a] < bPole[b]:                 # je-li prvek prvniho pole mensi nez druheho je prirazen do tretiho pole
            cPole.append(aPole[a])
            a = a + 1

        elif aPole[a] > bPole[b]:               # je-li prvek druheho pole mensi nez prvniho je prirazen do tretiho pole
            cPole.append(bPole[b])
            b = b + 1
        else:                                   # jsou-li stejne tak priradime do treho pole oba
            cPole.append(aPole[a])
            cPole.append(bPole[b])
            a = a + 1
            b = b + 1

    while a < len(aPole):                       # co zbylo v aPoli (je-li delsi) priradime do cPole
        cPole.append(aPole[a])
        a = a + 1
    
    while b < len(bPole):                       # co zbylo v bPoli (je-li delsi) priradime do cPole
        cPole.append(bPole[b])
        b = b + 1

    return cPole

#

def vypocetMinRun(n):
    # Tato funkce vypociva delku runu
    # Urcite neni optimalni, proste jsem se s tim jen nejak hral
    min_run = 32
    max_run = 64
    r = 0
    if n > 2*max_run:
        return max_run
    elif n <= max_run:
        return min_run
    else:
        while n/2 >= min_run:
            r |= n & 1
            n >>= 1
            return n + r

#

def TimSort(pole): # Worst: O( ), Average: O( )
    #
    RUN = 32
    #RUN = vypocetMinRun(len(pole))                                     # Urceni delky RUNu
    for x in range(0, len(pole), RUN):                                  # Rozdeleni pole do RUNu dle delky RUNu
        pole[x : x + RUN] = InsertionSort(pole[x : x + RUN])            # Pouziti Insertionsortu na RUN
        

    RUNplus = RUN                                                       # RUNplus je jen pomocny RUN co se muze menit
    while RUNplus < len(pole):                                          # Je-li vic jak jeden RUN aplikace Merge
        for i in range(0, len(pole), 2 * RUNplus):                      # Merge se aplikuje po RUNech (pro vetsi pole)
            pole[i : i + 2 * RUNplus] = Merge(pole[i : i + RUNplus], pole[i + RUNplus : i + 2 * RUNplus])
        RUNplus = RUNplus * 2

#
# //// Dalsi Sorting algoritmy
# // QuickSort

def QuickSort(pole, left, right):   # Worst: O(n^2), Average: O(n log(n))
    # Implementace quicksortu pro porovnani
    
    if left < right:
        partition_pos = partition(pole, left, right)
        QuickSort(pole, left, partition_pos - 1)
        QuickSort(pole, partition_pos + 1, right)

def partition(pole, left, right):
    i = left
    j = right - 1

    pivot = pole[right]

    while i < j:
        while i < right and pole[i] < pivot:
            i += 1
        while j > left and pole[j] >= pivot:
            j -= 1
        if i < j:
            pole[i], pole[j] = pole[j], pole[i]

    if pole[i] > pivot:
        pole[i], pole[right] = pole[right], pole[i]
    return i    

# // Bubble Sort

def BubbleSort(pole):   # Worst: O(n^2), Average: O(n^2)

    for i in range(0, len(pole)-1):
        for j in range(0, len(pole)-i-1):
            if pole[j] > pole[j+1]:
                pole[j],pole[j+1] = pole[j+1],pole[j]
            else:
                return

# // Selection Sort

def SelectionSort(pole):    # Worst: O(n^2), Average: O(n^2)
    a = 0

# // Heap Sort

def HeapSort(pole):     # Worst: O(n log(n)), Average: O(n log(n))
    a = 0 

# // Radix Sort

def RadixSort(pole):    # Worst: O(nk), Average: O(nk)
    a = 0

# // Bucket Sort

def BucketSort(pole):   # Worst: O(n^2), Average: O(n+k)
    a = 0

#
# Vytvoření random listu o délce n
def random_list(n):
    nums = list()

    for i in range(0, n):
        nums.append(round(random.uniform(0, n)))

    return nums

#

# MAIN -----------------------------------------------------------------------------------------------------------

def main():

    cas = time.thread_time()                      # Jako timer zvolen thread time, ukazuje asi nejlepsi vysledky
    print("\n\n\n\n\nSortingtime     : %.3f s" % (cas))
    print("\n\n\n\n")
    vizualization = 1

    if vizualization == 1:
        clearConsole()
        vel_pole = int(input("Zadejte velikost náhodného pole: "))
        if vel_pole > 10000:
            print("\nVAROVÁNÍ TŘÍDĚNÍ MŮŽE TRVAT DELŠÍ DOBU!")
        pole = random_list(vel_pole)

        print("-----------------------------------------------")
        print("IMPLEMENTOVANÉ TŘÍDÍCÍ METODY: \n")
        print("  => Timsort, spusten zadanim ts")
        print("  => Quicksort, spusten zadanim qs")
        print("  => Insertionsort, spusten zadanim is")
        print("  => Timsort z pythonu, spusten zadanim pts\n")

        metoda = input("Zadejte metodu třídění pole: ")
        metoda.lower
        clearConsole()
        print("\n\n\n#### PROBÍHÁ TŘÍDĚNÍ ####")   

        if metoda == "ts":
            TimSort(pole)
            
        elif metoda == "qs":
            QuickSort(pole, 0, len(pole) - 1)

        elif metoda == "is":    
            InsertionSort(pole)

        elif metoda == "pts":
            pole.sort

        else:
            print("Error 404: metoda nenalezena")

    if vizualization == 0:
        pole = random_list(1000000)
        TimSort(pole)
        # QuickSort(pole, 0, len(pole) - 1)
        # InsertionSort(pole)
        # pole.sort

main()




