import quandl
import numpy as np
import scipy
import matplotlib.pyplot as plt
import xlsxwriter
import pandas as pd
import yahoo_finance
from yahoo_finance import Share
import datetime
from datetime import datetime
import statistics
import pandas_datareader.data as wb

now = datetime.now()

today_date = str(now.year) + "-" + str(now.month) + "-" + str(now.day)

quandl.ApiConfig.api_key = "HMbMEXCjrykoHnyB6PVC"

day = "2017-08-24"

AAPL_df = quandl.get("WIKI/AAPL.11", start_date="2006-12-15", end_date = day, transform = "rdiff")
AAPL_df = AAPL_df.rename(columns={'Adj. Close': 'AAPL'})

MSFT_df = quandl.get("WIKI/MSFT.11", start_date="2006-12-15", end_date = day, transform = "rdiff")
MSFT_df = MSFT_df.rename(columns={'Adj. Close': 'MSFT'})

AMZN_df = quandl.get("WIKI/AMZN.11", start_date="2006-12-15", end_date = day, transform = "rdiff")
AMZN_df = AMZN_df.rename(columns={'Adj. Close': 'AMZN'})

CVS_df = quandl.get("WIKI/CVS.11", start_date="2006-12-15",end_date = day, transform = "rdiff")
CVS_df = CVS_df.rename(columns={'Adj. Close': 'CVS'})

XOM_df = quandl.get("WIKI/XOM.11", start_date="2006-12-15",end_date = day, transform = "rdiff")
XOM_df = XOM_df.rename(columns={'Adj. Close': 'XOM'})

JNJ_df = quandl.get("WIKI/JNJ.11", start_date="2006-12-15",end_date = day, transform = "rdiff")
JNJ_df = JNJ_df.rename(columns={'Adj. Close': 'JNJ'})

#BRK_df = quandl.get("WIKI/BRK.11", start_date="2006-11-01", transform = "rdiff")
#BRK_df = BRK_df.rename(columns={'Adj. Close': 'BRK'})

JPM_df = quandl.get("WIKI/JPM.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
JPM_df = JPM_df.rename(columns={'Adj. Close': 'JPM'})

GOOGL_df = quandl.get("WIKI/GOOGL.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
GOOGL_df = GOOGL_df.rename(columns={'Adj. Close': 'GOOGL'})

GE_df = quandl.get("WIKI/GE.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
GE_df = GE_df.rename(columns={'Adj. Close': 'GE'})

WFC_df = quandl.get("WIKI/WFC.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
WFC_df = WFC_df.rename(columns={'Adj. Close': 'WFC'})

T_df = quandl.get("WIKI/T.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
T_df = T_df.rename(columns={'Adj. Close': 'T'})

BAC_df = quandl.get("WIKI/BAC.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
BAC_df = BAC_df.rename(columns={'Adj. Close': 'BAC'})

PG_df = quandl.get("WIKI/PG.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
PG_df = PG_df.rename(columns={'Adj. Close': 'PG'})

CVX_df = quandl.get("WIKI/CVX.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
CVX_df = CVX_df.rename(columns={'Adj. Close': 'CVX'})

PFE_df = quandl.get("WIKI/PFE.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
PFE_df = PFE_df.rename(columns={'Adj. Close': 'PFE'})

VZ_df = quandl.get("WIKI/VZ.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
VZ_df = VZ_df.rename(columns={'Adj. Close': 'VZ'})

HD_df = quandl.get("WIKI/HD.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
HD_df = HD_df.rename(columns={'Adj. Close': 'HD'})

CMCSA_df = quandl.get("WIKI/CMCSA.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
CMCSA_df = CMCSA_df.rename(columns={'Adj. Close': 'CMCSA'})

GS_df = quandl.get("WIKI/GS.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
GS_df = GS_df.rename(columns={'Adj. Close': 'GS'})

INTC_df = quandl.get("WIKI/INTC.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
INTC_df = INTC_df.rename(columns={'Adj. Close': 'INTC'})

MRK_df = quandl.get("WIKI/MRK.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
MRK_df = MRK_df.rename(columns={'Adj. Close': 'MRK'})

USB_df = quandl.get("WIKI/USB.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
USB_df = USB_df.rename(columns={'Adj. Close': 'USB'})

DIS_df = quandl.get("WIKI/DIS.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
DIS_df = DIS_df.rename(columns={'Adj. Close': 'DIS'})

UNH_df = quandl.get("WIKI/UNH.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
UNH_df = UNH_df.rename(columns={'Adj. Close': 'UNH'})

CSCO_df = quandl.get("WIKI/CSCO.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
CSCO_df = CSCO_df.rename(columns={'Adj. Close': 'CSCO'})

C_df = quandl.get("WIKI/C.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
C_df = C_df.rename(columns={'Adj. Close': 'C'})

KO_df = quandl.get("WIKI/KO.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
KO_df = KO_df.rename(columns={'Adj. Close': 'KO'})

PEP_df = quandl.get("WIKI/PEP.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
PEP_df = PEP_df.rename(columns={'Adj. Close': 'PEP'})

MO_df = quandl.get("WIKI/MO.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
MO_df = MO_df.rename(columns={'Adj. Close': 'MO'})

IBM_df = quandl.get("WIKI/IBM.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
IBM_df = IBM_df.rename(columns={'Adj. Close': 'IBM'})

ORCL_df = quandl.get("WIKI/ORCL.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
ORCL_df = ORCL_df.rename(columns={'Adj. Close': 'ORCL'})

AMGN_df = quandl.get("WIKI/AMGN.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
AMGN_df = AMGN_df.rename(columns={'Adj. Close': 'AMGN'})

MMM_df = quandl.get("WIKI/MMM.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
MMM_df = MMM_df.rename(columns={'Adj. Close': 'MMM'})

MCD_df = quandl.get("WIKI/MCD.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
MCD_df = MCD_df.rename(columns={'Adj. Close': 'MCD'})

WMT_df = quandl.get("WIKI/WMT.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
WMT_df = WMT_df.rename(columns={'Adj. Close': 'WMT'})

MDT_df = quandl.get("WIKI/MDT.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
MDT_df = MDT_df.rename(columns={'Adj. Close': 'MDT'})

MA_df = quandl.get("WIKI/MA.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
MA_df = MA_df.rename(columns={'Adj. Close': 'MA'})

BA_df = quandl.get("WIKI/BA.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
BA_df = BA_df.rename(columns={'Adj. Close': 'BA'})

TXN_df = quandl.get("WIKI/TXN.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
TXN_df = TXN_df.rename(columns={'Adj. Close': 'TXN'})

SLB_df = quandl.get("WIKI/SLB.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
SLB_df = SLB_df.rename(columns={'Adj. Close': 'SLB'})

HON_df = quandl.get("WIKI/HON.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
HON_df = HON_df.rename(columns={'Adj. Close': 'HON'})

CELG_df = quandl.get("WIKI/CELG.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
CELG_df = CELG_df.rename(columns={'Adj. Close': 'CELG'})

BMY_df = quandl.get("WIKI/BMY.11", start_date="2006-12-15",end_date = day, transform = "rdiff")
BMY_df = BMY_df.rename(columns={'Adj. Close': 'BMY'})

UNP_df = quandl.get("WIKI/UNP.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
UNP_df = UNP_df.rename(columns={'Adj. Close': 'UNP'})

AGN_df = quandl.get("WIKI/AGN.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
AGN_df = AGN_df.rename(columns={'Adj. Close': 'AGN'})

SBUX_df = quandl.get("WIKI/SBUX.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
SBUX_df = SBUX_df.rename(columns={'Adj. Close': 'SBUX'})

PCLN_df = quandl.get("WIKI/PCLN.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
PCLN_df = PCLN_df.rename(columns={'Adj. Close': 'PCLN'})

GILD_df = quandl.get("WIKI/GILD.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
GILD_df = GILD_df.rename(columns={'Adj. Close': 'GILD'})

UTX_df = quandl.get("WIKI/UTX.11", start_date="2006-12-15", end_date = day,transform = "rdiff")
UTX_df = UTX_df.rename(columns={'Adj. Close': 'UTX'})

df = AAPL_df.join(MSFT_df).join(AMZN_df).join(CVS_df).join(XOM_df).join(JNJ_df).join(JPM_df).join(GOOGL_df).join(GE_df).join(WFC_df).join(T_df).join(BAC_df).join(PG_df).join(CVX_df).join(PFE_df).join(VZ_df).join(HD_df).join(CMCSA_df).join(GS_df).join(INTC_df).join(MRK_df).join(USB_df).join(DIS_df).join(UNH_df).join(CSCO_df).join(C_df).join(KO_df).join(PEP_df).join(MO_df).join(IBM_df).join(ORCL_df).join(AMGN_df).join(MMM_df).join(MCD_df).join(WMT_df).join(MDT_df).join(MA_df).join(BA_df).join(SLB_df).join(HON_df).join(CELG_df).join(BMY_df).join(UNP_df).join(AGN_df).join(SBUX_df).join(PCLN_df).join(GILD_df).join(UTX_df).join(TXN_df)

i = 0

DateList = list(AAPL_df.index)

while i < len(DateList):
    DateList[i] = DateList[i].date().strftime('%m-%d-%Y')
    i = i + 1

removeIndex = 0

while removeIndex < 30:
    DateList.remove(DateList[0])
    removeIndex = removeIndex + 1

variances = []
i = 0
while(i < len(AAPL_df.values.tolist())):
    toCalculate = [AAPL_df.values.tolist()[i], TXN_df.values.tolist()[i], UTX_df.values.tolist()[i], GILD_df.values.tolist()[i], PCLN_df.values.tolist()[i], SBUX_df.values.tolist()[i], AGN_df.values.tolist()[i], UNP_df.values.tolist()[i], BMY_df.values.tolist()[i], CELG_df.values.tolist()[i], HON_df.values.tolist()[i], SLB_df.values.tolist()[i], BA_df.values.tolist()[i], MA_df.values.tolist()[i], MDT_df.values.tolist()[i], WMT_df.values.tolist()[i], MCD_df.values.tolist()[i], MMM_df.values.tolist()[i], AMGN_df.values.tolist()[i], ORCL_df.values.tolist()[i], IBM_df.values.tolist()[i], MO_df.values.tolist()[i], PEP_df.values.tolist()[i], KO_df.values.tolist()[i], C_df.values.tolist()[i], CSCO_df.values.tolist()[i], UNH_df.values.tolist()[i], DIS_df.values.tolist()[i], USB_df.values.tolist()[i], MRK_df.values.tolist()[i], INTC_df.values.tolist()[i], GS_df.values.tolist()[i], CMCSA_df.values.tolist()[i], HD_df.values.tolist()[i], VZ_df.values.tolist()[i], PFE_df.values.tolist()[i], CVX_df.values.tolist()[i], PG_df.values.tolist()[i], BAC_df.values.tolist()[i], T_df.values.tolist()[i], WFC_df.values.tolist()[i], GE_df.values.tolist()[i], GOOGL_df.values.tolist()[i], JPM_df.values.tolist()[i], JNJ_df.values.tolist()[i], XOM_df.values.tolist()[i], CVS_df.values.tolist()[i], AMZN_df.values.tolist()[i], MSFT_df.values.tolist()[i]] 
    variances.append(np.var(toCalculate))
    i = i + 1

a = 30

finalVar = []
while(a < len(variances)):
    total = 0
    countIndex = a - 30
    while(countIndex < a):
        total = total + variances[countIndex]
        countIndex = countIndex + 1
    average = total/30
    finalVar.append(average)
    a = a + 1

b = 0
while b < 30:
    finalVar.remove[0]
    b = b + 1
    
columnVar = ["30 Day Variance", ]
finalVarDF = pd.DataFrame({'Date': DateList, '30 Day Variance': finalVar})
