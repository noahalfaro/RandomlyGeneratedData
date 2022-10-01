def benfordness(series):
    """
    DEPENDENCIES: 
    pandas, matplotlib.pytlot, seaborn.
    
    SUMMARY:
    BENFORDS LAW
    The probability of a given digit d to be a leading digit is given by the below expression:
    
    probability(d) = sympy.log(1 + (1/d),10)
    
    =>probability[list(range(1,10))] = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
    
    The idea is that in a complete dataset (One that covers at least one full magnitude of 10),
    there is a relationship between the frequencies of certain numbers being the leading digit.
    In other words, there is a certain probability assigned to each digit 1-9 for the likelihood of 
    it being a leading digit. NOTE: this is a REPORT function, so nothing is returned.
    
    INPUTS:
    pandas.DataFrame['column_name'], LISTS, such iterables.
    
    REPORT COMPONENTS:
    1) The Mean Absolute Error of the input series digit frequencies and the Benford digit frequencies.
    
    2) The Benford digit Frequencies 1-9, including 9.
    
    3) The input series digit Frequencies 1-9, including 9.
    
    4) A matplotlib graph by seaborn showing the Benford curve and Input series line plot.
    
    Example:
    >>>benfordness(df['Location_Northing_OSGR'])
    
    The Mean Absolute Error from the Benford Frequencies is 3.42

    Benford Frequencies 1-9: [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]

    Location_Northing_OSGR 1-9: [36.09, 17.47, 18.78, 12.83, 5.43, 5.25, 1.17, 1.27, 1.7]
    
    matplotlib.pyplot object generated with seaborn and matplotlib.pyplot in the backend(see code).
    """
    a = [str(i) for i in list(series)]
    n = len(a)
    a1 = [i for i in a if i.startswith('1')==True]
    a2 = [i for i in a if i.startswith('2')==True]
    a3 = [i for i in a if i.startswith('3')==True]
    a4 = [i for i in a if i.startswith('4')==True]
    a5 = [i for i in a if i.startswith('5')==True]
    a6 = [i for i in a if i.startswith('6')==True]
    a7 = [i for i in a if i.startswith('7')==True]
    a8 = [i for i in a if i.startswith('8')==True]
    a9 = [i for i in a if i.startswith('9')==True]
    b = {
        'Input Frequency of 1':round((len(a1)/n)*100,2),
        'Input Frequency of 2':round((len(a2)/n)*100,2),
        'Input Frequency of 3':round((len(a3)/n)*100,2),
        'Input Frequency of 4':round((len(a4)/n)*100,2),
        'Input Frequency of 5':round((len(a5)/n)*100,2),
        'Input Frequency of 6':round((len(a6)/n)*100,2),
        'Input Frequency of 7':round((len(a7)/n)*100,2),
        'Input Frequency of 8':round((len(a8)/n)*100,2),
        'Input Frequency of 9':round((len(a9)/n)*100,2),
    }
    c = {
        'Benford Frequency of 1':30.1,
        'Benford Frequency of 2':17.6,
        'Benford Frequency of 3':12.5,
        'Benford Frequency of 4':9.7,
        'Benford Frequency of 5':7.9,
        'Benford Frequency of 6':6.7,
        'Benford Frequency of 7':5.8,
        'Benford Frequency of 8':5.1,
        'Benford Frequency of 9':4.6,
    }
    d = list(b.values())
    e = list(c.values())
    m_e_d = round((abs(d[0]-e[0])+abs(d[1]-e[1])+abs(d[2]-e[2])+abs(d[3]-e[3])+abs(d[4]-e[4])+abs(d[5]-e[5])+abs(d[6]-e[6])+abs(d[7]-e[7])+abs(d[8]-e[8]))/9,2)
    print(f"For the '{series.name}' column:")
    print(f'1) There are {len(series)} entries.\n')
    print(f'2) The Mean Absolute Error from the Benford Frequencies is {m_e_d}')
    print(f"\n3) '{series.name}' Frequencies 1-9: {d}\n\n4) Benford Frequencies 1-9: {e}\n\n")
    from seaborn import lineplot
    from matplotlib.pyplot import legend, grid, figure
    figure(figsize=(8, 5))
    lineplot(x=list(range(1,10)),y=[30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6],label='Benford Curve')
    lineplot(x=list(range(1,10)),y=list(b.values()),label=series.name)
    legend()
    grid(b=True)