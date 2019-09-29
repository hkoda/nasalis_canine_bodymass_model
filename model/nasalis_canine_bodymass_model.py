# coding: utf-8
# This is the mathematical models accounting for the observational data (Matuda et al. 2019 under reivew or submission) of canine length and body mass, measured in wild habitat of proboscis monkeys. The model descriptions are reported in the supplementary online materials of the journal website, after confirming the acceptance of the main manuscript.
# The code is worked under python3 or anaconda3 with:
# matplotlib                3.0.1            py36h54f8f79_0  
# numpy                     1.15.2           py36h6a91979_1  
# pandas                    0.23.4           py36h6440ff4_0  
# python                    3.6.7                haf84260_0  
# seaborn                   0.9.0                    py36_0  
# (c) Hiroki Koda. 2019. All Rights Reserved.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# main model part for body mass development
def bodymass_model(a,c,alpha,t,t_0,t_1,A,K,A_3,T,t_2,harem):
    if t < t_0:
        case_t = -a * t
        denom = 1 + A * np.exp(case_t)
        m = K / denom
    elif t < t_1:
        case_t = (1/2) * a * c * alpha * (t_0**2) + (1/2) * a * c * alpha * (t**2) - a * t * (1 + c * alpha * t_0) 
        denom = 1 + A * np.exp(case_t)
        m = K / denom
    elif t <= T:
        case_t = (1/2) * a * c * alpha * (t_0**2) - (1/2) * a * c * alpha * (t_1 ** 2) - a * t + a * c * alpha * t_1 * t -a * c * alpha * t_0*t
        denom = 1 + A * np.exp(case_t)
        m = K / denom
    elif harem == 'Harem':
        case_t = (1/2) * a * c * alpha * (t_0**2) - (1/2) * a * c * alpha * (t_1 ** 2) - a * t + a * c * alpha * t_1 * t -a * c * alpha * t_0*t
        denom = 1 + A * np.exp(case_t)
        m = K / denom
    elif t < t_2:
        beta = a * (1 - c * alpha * t_1 + c * alpha * t_0)/(t_2 - T)
        case_t = (1/2) * beta * t * t - beta * t_2 * t
        denom = 1 + A_3 * np.exp(case_t)
        m = K / denom
    else:
        beta = a * (1 - c * alpha * t_1 + c * alpha * t_0)/(t_2 - T)
        case_t = (1/2) * beta * t_2 * t_2 - beta * t_2 * t_2
        denom = 1 + A_3 * np.exp(case_t)
        m = K / denom
    return m

# main model part for canine mass development
def canine_model(t,t_0,t_1,c,alpha):
    if t < t_0:
        z = 0
    elif t < t_1:
        z = alpha * (t - t_0)#(2 * t - 1) /c
    else:
        z = alpha * (t_1 - t_0)#(2 * t_1 - 1)/c 
    return z

# making figure of the interaction between body mass and canine development
def mk_plot(df,c):
    g = sns.scatterplot(data = df, x ='m', y='z',style = 'Status')
    g.set_xlabel('Simulated body mass (kg)')
    g.set_ylabel('Normalized canine size')
    g.set_title('Cost parameter: %1.2f' % c)
    g.set_xlim(8,26)
    return g

# making figure of the growth curves of the body mass
def mk_growth_plot(a,c,alpha,t_0,t_1_s,A,K,T,t_2,harem):
    t_range = np.linspace(0,2)
    m_growth_s = []
    t_s = []
    t_1_s_s = []
    z_s = []
    for t_1 in t_1_s:
        for t in t_range:
            A_3 = calc_A_3(K,a,c,alpha,t_0,t_1,A,T,t_2)
            m_growth = bodymass_model(a,c,alpha,t,t_0,t_1,A,K,A_3,T,t_2,harem)
            m_growth_s.append(m_growth)
            # z = canine_model(T,t_0,t_1,c,alpha)
            t_s.append(t)
            t_1_s_s.append(t_1)
            # z_s.append(z)
    # store the results in temporary dataframe for the figure visualization
    df = pd.DataFrame(
        {
            'm':m_growth_s,
            't':t_s,
            't_1':t_1_s_s,
        }
    )
    df['canine'] = df.t_1.apply(lambda x: alpha * (T - x))
    g = sns.scatterplot(data = df, x ='t', y='m', style = 't_1')
    g.set_ylim(0,25.5+1)
    g.set_xlabel('$t$, Normalized age')
    g.set_ylabel('$m$, Simulated body mass (kg)')
    g.set_title('%s at %1.2f cost' % (harem, c))
    return g

# calcuration function of parameter A_3, an important parameter in the body mass model. 
def calc_A_3(K,a,c,alpha,t_0,t_1,A_0,T,t_2):
    beta = a * (1 - c * alpha * t_1 + c * alpha * t_0)/(t_2 - T)
    f1 = (1/2) * a * c * alpha * t_0 * t_0
    f2 = (-1/2) * a * c * alpha * t_1 * t_1
    f3 = -a * T
    f4 = a * c * alpha * t_1 * T
    f5 = - a * c * alpha * t_0 * T
    f6 = - beta * (1/2 * T * T - t_2 * T)
    fomula = f1 + f2 + f3 + f4 + f5 + f6
    A_3 = A_0 * np.exp(fomula)
    return A_3

# main loop of the simulation, data visualization.
def main():
    # set initial parameters common for male and female.
    t = 2
    T = 1
    t_0 = 0.5
    c_s = [0.01,0.50,0.99]
    m_0 = 0.45
    m_1 = 6.5
    z_sex_ratio = 10.0/24.0 # famale_to_male ratio
    status_s = ['Harem','Non-harem','Female']

    # ititialize saved variables
    m_star_s = []
    z_star_s = []
    t_1_parameters = []
    c_parameters = []
    s_parameters =[]

    # simulation for the body mass and canine size at the time, t = 2, ca. 8 years old. The loops are peformed for each status, i.e., harem male, non-harem male or female. The simulation is performed for each of status, independently.
    for harem in status_s:
        if harem == 'Female':
            # set initial parameter for female.
            K = 14.5
            T = 6/8 # female stop the body growth around 6 yo, ealiear than male, based on the previous evidence, Masuda and Sha 201X.
            t_1_s = np.linspace(0.5,T)
            alpha_m = 1/(T - t_0)
            alpha = alpha_m * z_sex_ratio
            t_2 = 6/8 + 0.1

        else:
            # set initial parameter for male
            K = 25.5
            T = 1
            t_1_s = np.linspace(0.5,T)
            alpha_m = 1/(T - t_0)
            alpha = alpha_m
            t_2 = 1 + 0.1

        # set initial parameter after determining the sex-specific intial parameter 
        A = K/m_0 - 1
        a = - (1/t_0) * np.log((K - m_1)/(A * m_1))
        print('a: %1.3f; A_0: %1.3f' % (a, A))
        # run simulations
        for t_1 in t_1_s:
            for c in c_s:
                A_3 = calc_A_3(K,a,c,alpha,t_0,t_1,A,T,t_2)
                print('A_3: %1.3f of t_1 = %f' % (A_3,t_1))
                m_star = bodymass_model(a,c,alpha,t,t_0,t_1,A,K,A_3,T,t_2,harem)
                z_star = canine_model(t,t_0,t_1,c,alpha)
                m_star_s.append(m_star)
                z_star_s.append(z_star)
                t_1_parameters.append(t_1)
                c_parameters.append(c)
                s_parameters.append(harem)

    # store the results in dataframe
    df = pd.DataFrame(
        {
            'm':m_star_s,
            'z':z_star_s,
            't_1':t_1_parameters,
            'c':c_parameters,
            'Status':s_parameters
        }
    )

    # make figure for the paper.
    fig = plt.figure(figsize = (5,5))
    g = mk_plot(df[df['c'] == 0.99],0.99)
    plt.tight_layout()
    plt.savefig('fig_simulation.png', dpi = 600)
    plt.clf()

    # visualize results of all
    fig = plt.figure(figsize = (9,3))
    for i, c in enumerate(c_s):
        df_c = df[df['c'] == c]
        g = fig.add_subplot(1,3,i+1)
        g = mk_plot(df_c,c)
    plt.tight_layout()
    plt.savefig('simulation_results_bm_vs_canine_status_all_cost.png',dpi=600)
    plt.clf()

    # simulation for the body mass development from t=0 to t = 2, ca. 8 years old. The loops are peformed for each status, i.e., harem male, non-harem male or female. The simulation is performed for each of status, independently. 
    fig = plt.figure(figsize = (9,9))
    i = 0 # counter of the index of figure locations in axes.
    for harem in status_s:
        if harem == 'Female':
            K = 14.5
            T = 6/8 # female stop the body growth around 6 yo, ealiear than male, based on the previous evidence, Masuda and Sha 201X.
            t_1_s = np.linspace(0.5,T)
            alpha_m = 1/(T - t_0)
            alpha = alpha_m * z_sex_ratio
            t_2 = 6/8 + 0.1

        else:
            K = 25.5
            T = 1
            t_1_s = np.linspace(0.5,T)
            alpha_m = 1/(T - t_0)
            alpha = alpha_m
            t_2 = 1 + 0.1

        A = K/m_0 - 1
        a = - (1/t_0) * np.log((K - m_1)/(A * m_1))

        for c in c_s:
            i += 1
            fig.add_subplot(3,3,i)
            t_1_s = [0.51,(0.5 + T)/2,T - 0.01]
            g = mk_growth_plot(a,c,alpha,t_0,t_1_s,A,K,T,t_2,harem)
    plt.tight_layout()
    plt.savefig('simulation_results_bm_growth.png',dpi = 600)
    plt.clf()

if __name__ == "__main__":
    main()