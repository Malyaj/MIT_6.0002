# -*- coding: utf-8 -*-

# Markov Chains in Python: Beginner Tutorial
# https://www.datacamp.com/community/tutorials/markov-chains-python-tutorial

import PySimpleGUI as sg
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import PySimpleGUI as sg

states = ["ND", "1-30", "31-60", "61-90", "91-180", "180-360", "360+", "Closed"]

layout = [[sg.Text('States:'.ljust(60)), sg.Text(", ".join(states))],
          [sg.InputText('Transition Matrix', size=(10,1), key="_transition_file_", disabled = True), sg.FileBrowse('Select Transition Matrix',size=(50,1))],
          [sg.InputText('Current AR', size=(10,1), key="_current_ar_", disabled = True), sg.FileBrowse('Select Current AR', size=(50,1))],
          [sg.InputText('monthlyNDforecast', size=(10,1), key="_monthlyNDforecast_", disabled = True), sg.FileBrowse('Select monthlyNDforecast', size=(50,1))],
          [sg.Text('Month: '.ljust(50)), sg.Slider(range=(1, 12), orientation='h', size=(45, 10), default_value=6, key="_months_")],
          [sg.Text('activityToday'.ljust(50)), sg.DropDown(states, size=(40,1), key="_activityToday_")],
          [sg.RButton('Run', size=(100,1))],
          [sg.Exit(size=(100,1))],
          ]


window = sg.Window('Forecast Tool', grab_anywhere=False).Layout(layout).Finalize()

window.Resizable = True
window.TextJustification = True


while True:      
    e, v = window.Read()      
    if e in [None, 'Exit']:      
        break
    if e in ['Run']:
        try:
            print(v)
            #transitionMatrix
            months = v['_months_']


            
            #states = [i.strip() for i in v["__IN__"].split(",")]
            path = r"D:\Users\703143501\Documents\Genpact Internal\Debu_GUI"
            os.chdir(path)
            # Import data set
            transitionName1 = pd.read_csv('transitionName.csv', encoding = 'ISO-8859-1')

            transitionMatrix1 = pd.read_csv(v['_transition_file_'], encoding = 'ISO-8859-1')
            
            #transitionMatrix1 = pd.read_csv('transitionMatrix.csv', encoding = 'ISO-8859-1')

            Data = pd.read_csv('Data_Amount_Lines_Jan16.csv', encoding = 'ISO-8859-1')
            amount = pd.DataFrame(Data.iloc[:,1:2])
            #print("Amount: ")
            #print(amount)
            lines = pd.DataFrame(Data.iloc[:,2:3])
            print("lines: ")
            print(lines)
            monthlyNDforecastData = pd.read_csv('monthlyNDforecast.csv', encoding = 'ISO-8859-1')
            monthlyNDforecast = pd.DataFrame(monthlyNDforecastData.iloc[:,1:2])

            #Combine all details
            transitionName = pd.DataFrame(transitionName1.iloc[:,1:9])
            transitionMatrix = pd.DataFrame(transitionMatrix1.iloc[:,1:9])

            #states = transitionMatrix.columns.values
            states = list(transitionMatrix)

            #print(states)

            states = ["ND", "1-30", "31-60", "61-90", "91-180", "180-360", "360+", "Closed"]

            # Possible sequences of events
            transitionName = [["_".join([str(states[i]), str(states[j])]) for j in range(len(states))] for i in range(len(states))]

            # Probabilities matrix (transition matrix)

            '''
            transitionMatrix = np.array(
                [[0.22,	0.22,	0.00,	0.00,	0.00,	0.00,	0.00,	0.56],
                 [0.00,	0.00,	0.49,	0.01,	0.00,	0.00,	0.00,	0.50],
                 [0.00,	0.00,	0.00,	0.75,	0.01,	0.00,	0.00,	0.24],
                 [0.00,	0.00,	0.00,	0.00,	0.85,	0.00,	0.00,	0.15],
                 [0.00,	0.00,	0.00,	0.00,	0.59,	0.26,	0.00,	0.15],
                 [0.00,	0.00,	0.00,	0.00,	0.00,	0.83,	0.10,	0.07],
                 [0.00,	0.00,	0.00,	0.00,	0.00,	0.00,	0.96,	0.04],
                 [0.00,	0.00,	0.00,	0.00,	0.00,	0.00,	0.00,	1.00]])
            '''

            print(transitionMatrix)

            transitionMatrixSanity = all([not j for j in [bool(sum(transitionMatrix[i,:]) - 1.0) for i in range(len(transitionMatrix))]])

            if transitionMatrixSanity:
                print("All is gonna be okay, you should move on!! ;)")
            else:
                print("Somewhere, something went wrong. Transition matrix, perhaps?")

            #months = 12
            # take months as an input

            # Entry states
            activityToday = v["_activityToday_"]
            #activityToday = "ND"

            #*******************************************
            # Forecast
            # Lines
            Lines1= np.matrix(lines.iloc[:8,0])
            #print(Lines1)
            #print(monthlyNDforecast.iloc[1,0])


            #Need to check forecast_lines0 return value
            #print("Volume (#Lines) forecast after " + str(months) + " months for the scenario where starting state is " + activityToday  + " : ")
            forecast_lines0 = transitionMatrix.T * Lines1.T
            #print(transitionMatrix)
            #print(Lines1)
            #print(forecast_lines0)


            #monthlyNDforecastM1 = np.matrix([monthlyNDforecast.iloc[0,0],0,0,0,0,0,0,0]).T
            #print(monthlyNDforecastM1)
            #LinesM1 = (forecast_lines0 + monthlyNDforecastM1)
            #print(LinesM1)
            #forecast_linesM = transitionMatrix.T * LinesM1
            #print(forecast_linesM)
            
            #monthlyNDforecastM = np.matrix([monthlyNDforecast.iloc[i,0],0,0,0,0,0,0,0]).T
            #LinesM = (LinesM + monthlyNDforecastM)
            #forecast_linesM = transitionMatrix.T * LinesM.T
            
            #monthlyNDforecastM = np.matrix([monthlyNDforecast.iloc[0,0],0,0,0,0,0,0,0]).T
            #print(monthlyNDforecastM)
            #print(forecast_lines0)
            #LinesM = (forecast_lines0 + monthlyNDforecastM)
            #print(LinesM)
            
            #forecast_linesM = transitionMatrix * LinesM.T
            #print(forecast_linesM)        
            #**************************************
            # Choose the starting state
            forecast_linesM0 = transitionMatrix.T*(forecast_lines0 + np.matrix([monthlyNDforecast.iloc[0,0],0,0,0,0,0,0,0]).T)
            #forecast_linesM0
            forecast_linesM1 = transitionMatrix.T*(forecast_linesM0 + np.matrix([monthlyNDforecast.iloc[1,0],0,0,0,0,0,0,0]).T)
            #forecast_linesM1
            forecast_linesM2 = transitionMatrix.T*(forecast_linesM1 + np.matrix([monthlyNDforecast.iloc[2,0],0,0,0,0,0,0,0]).T)
            #forecast_linesM2
            forecast_linesM3 = transitionMatrix.T*(forecast_linesM2 + np.matrix([monthlyNDforecast.iloc[3,0],0,0,0,0,0,0,0]).T)
            #forecast_linesM3


            def activity_forecast(months, activityToday):
                activityList = [forecast_lines0]
                i = 0
                forecast_linesM = (forecast_lines0)
        
                while i != months:
                    monthlyNDforecastM = np.matrix([monthlyNDforecast.iloc[i,0],0,0,0,0,0,0,0]).T
                    forecast_linesM = transitionMatrix.T * (forecast_linesM + monthlyNDforecastM)
                    activityList.append(forecast_linesM)
                    i += 1
                return activityList
    
            # To save every activityList
            list_activity = []
        
            activity_forecast(months, activityToday)
            activity_forecast1 = np.asarray(activity_forecast(months, activityToday))
            activity_forecast2 = activity_forecast1.T
            shape =(8, months+1)
    
            activity_forecast3= activity_forecast2.reshape(shape)
            
            import matplotlib
            
    
    
            index = np.arange(months+20)
            plt.xlabel('Months', fontsize=12)
            plt.ylabel('No of lines', fontsize=12)
            plt.xticks(index, fontsize=12, rotation=30)
    
            plt.title(("Volume (#Lines) forecast for " + str(months) + " months for the scenario where starting state is " + activityToday  + " : "))

            ## re-factor this
            index_range = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
            #colors = ['c', 'b', 'k', 'y', 'm', 'r', 'g']

            p0=plt.bar(index_range, np.array(activity_forecast3[0,:]))
            p1=plt.bar(index_range, np.array(activity_forecast3[1,:]), bottom = np.array(activity_forecast3[0,:]),color='c')
            p2=plt.bar(index_range, np.array(activity_forecast3[2,:]), bottom = np.array(activity_forecast3[0,:])+np.array(activity_forecast3[1,:]),color='b')
            p3=plt.bar(index_range, np.array(activity_forecast3[3,:]), bottom = np.array(activity_forecast3[0,:])+np.array(activity_forecast3[1,:])+np.array(activity_forecast3[2,:]),color='k')
            p4=plt.bar(index_range, np.array(activity_forecast3[4,:]), bottom = np.array(activity_forecast3[0,:])+np.array(activity_forecast3[1,:])+np.array(activity_forecast3[2,:])+np.array(activity_forecast3[3,:]),color='y')
            p5=plt.bar(index_range, np.array(activity_forecast3[5,:]), bottom = np.array(activity_forecast3[0,:])+np.array(activity_forecast3[1,:])+np.array(activity_forecast3[2,:])+np.array(activity_forecast3[3,:])+np.array(activity_forecast3[4,:]),color='m')
            p6=plt.bar(index_range, np.array(activity_forecast3[6,:]), bottom = np.array(activity_forecast3[0,:])+np.array(activity_forecast3[1,:])+np.array(activity_forecast3[2,:])+np.array(activity_forecast3[3,:])+np.array(activity_forecast3[4,:])+np.array(activity_forecast3[5,:]),color='r')
            p7=plt.bar(index_range, np.array(activity_forecast3[7,:]), bottom = np.array(activity_forecast3[0,:])+np.array(activity_forecast3[1,:])+np.array(activity_forecast3[2,:])+np.array(activity_forecast3[3,:])+np.array(activity_forecast3[4,:])+np.array(activity_forecast3[5,:])+np.array(activity_forecast3[6,:]),color='g')

            #ps = plt.bar(index_range), np.array(activity_forecast3[i, :], bottom = 
            ps = [p0, p1, p2, p3, p4, p5, p6, p7]
            
            plt.legend([p[0] for p in ps], states, loc=2, fontsize=8)

            plt.show()

            matplotlib.use('Agg')
            plt.savefig('myfig')

        except:
            sg.Popup("Invalid Entry: Try Again!")

window.Close()

## this needs to be more modular
## explore how to import a function from another file

