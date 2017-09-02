import quandl
import numpy as np
import scipy
import matplotlib.pyplot as plt
import xlsxwriter
import pandas as pd

quandl.ApiConfig.api_key = "HMbMEXCjrykoHnyB6PVC"

AAPL_df = quandl.get("WIKI/AAPL.11", start_date="2006-11-01", transform = "rdiff")
AAPL_df = AAPL_df.rename(columns={'Adj. Close': 'AAPL'})

MSFT_df = quandl.get("WIKI/MSFT.11", start_date="2006-11-01", transform = "rdiff")
MSFT_df = MSFT_df.rename(columns={'Adj. Close': 'MSFT'})

AMZN_df = quandl.get("WIKI/AMZN.11", start_date="2006-11-01", transform = "rdiff")
AMZN_df = AMZN_df.rename(columns={'Adj. Close': 'AMZN'})

CVS_df = quandl.get("WIKI/CVS.11", start_date="2006-11-01", transform = "rdiff")
CVS_df = CVS_df.rename(columns={'Adj. Close': 'CVS'})

XOM_df = quandl.get("WIKI/XOM.11", start_date="2006-11-01", transform = "rdiff")
XOM_df = XOM_df.rename(columns={'Adj. Close': 'XOM'})

JNJ_df = quandl.get("WIKI/JNJ.11", start_date="2006-11-01", transform = "rdiff")
JNJ_df = JNJ_df.rename(columns={'Adj. Close': 'JNJ'})

#BRK_df = quandl.get("WIKI/BRK.11", start_date="2006-11-01", transform = "rdiff")
#BRK_df = BRK_df.rename(columns={'Adj. Close': 'BRK'})

JPM_df = quandl.get("WIKI/JPM.11", start_date="2006-11-01", transform = "rdiff")
JPM_df = JPM_df.rename(columns={'Adj. Close': 'JPM'})

GOOGL_df = quandl.get("WIKI/GOOGL.11", start_date="2006-11-01", transform = "rdiff")
GOOGL_df = GOOGL_df.rename(columns={'Adj. Close': 'GOOGL'})

GE_df = quandl.get("WIKI/GE.11", start_date="2006-11-01", transform = "rdiff")
GE_df = GE_df.rename(columns={'Adj. Close': 'GE'})

WFC_df = quandl.get("WIKI/WFC.11", start_date="2006-11-01", transform = "rdiff")
WFC_df = WFC_df.rename(columns={'Adj. Close': 'WFC'})

T_df = quandl.get("WIKI/T.11", start_date="2006-11-01", transform = "rdiff")
T_df = T_df.rename(columns={'Adj. Close': 'T'})

BAC_df = quandl.get("WIKI/BAC.11", start_date="2006-11-01", transform = "rdiff")
BAC_df = BAC_df.rename(columns={'Adj. Close': 'BAC'})

PG_df = quandl.get("WIKI/PG.11", start_date="2006-11-01", transform = "rdiff")
PG_df = PG_df.rename(columns={'Adj. Close': 'PG'})

CVX_df = quandl.get("WIKI/CVX.11", start_date="2006-11-01", transform = "rdiff")
CVX_df = CVX_df.rename(columns={'Adj. Close': 'CVX'})

PFE_df = quandl.get("WIKI/PFE.11", start_date="2006-11-01", transform = "rdiff")
PFE_df = PFE_df.rename(columns={'Adj. Close': 'PFE'})

VZ_df = quandl.get("WIKI/VZ.11", start_date="2006-11-01", transform = "rdiff")
VZ_df = VZ_df.rename(columns={'Adj. Close': 'VZ'})

HD_df = quandl.get("WIKI/HD.11", start_date="2006-11-01", transform = "rdiff")
HD_df = HD_df.rename(columns={'Adj. Close': 'HD'})

CMCSA_df = quandl.get("WIKI/CMCSA.11", start_date="2006-11-01", transform = "rdiff")
CMCSA_df = CMCSA_df.rename(columns={'Adj. Close': 'CMCSA'})

GS_df = quandl.get("WIKI/GS.11", start_date="2006-11-01", transform = "rdiff")
GS_df = GS_df.rename(columns={'Adj. Close': 'GS'})

INTC_df = quandl.get("WIKI/INTC.11", start_date="2006-11-01", transform = "rdiff")
INTC_df = INTC_df.rename(columns={'Adj. Close': 'INTC'})

MRK_df = quandl.get("WIKI/MRK.11", start_date="2006-11-01", transform = "rdiff")
MRK_df = MRK_df.rename(columns={'Adj. Close': 'MRK'})

USB_df = quandl.get("WIKI/USB.11", start_date="2006-11-01", transform = "rdiff")
USB_df = USB_df.rename(columns={'Adj. Close': 'USB'})

DIS_df = quandl.get("WIKI/DIS.11", start_date="2006-11-01", transform = "rdiff")
DIS_df = DIS_df.rename(columns={'Adj. Close': 'DIS'})

UNH_df = quandl.get("WIKI/UNH.11", start_date="2006-11-01", transform = "rdiff")
UNH_df = UNH_df.rename(columns={'Adj. Close': 'UNH'})

CSCO_df = quandl.get("WIKI/CSCO.11", start_date="2006-11-01", transform = "rdiff")
CSCO_df = CSCO_df.rename(columns={'Adj. Close': 'CSCO'})

C_df = quandl.get("WIKI/C.11", start_date="2006-11-01", transform = "rdiff")
C_df = C_df.rename(columns={'Adj. Close': 'C'})

KO_df = quandl.get("WIKI/KO.11", start_date="2006-11-01", transform = "rdiff")
KO_df = KO_df.rename(columns={'Adj. Close': 'KO'})

PEP_df = quandl.get("WIKI/PEP.11", start_date="2006-11-01", transform = "rdiff")
PEP_df = PEP_df.rename(columns={'Adj. Close': 'PEP'})

MO_df = quandl.get("WIKI/MO.11", start_date="2006-11-01", transform = "rdiff")
MO_df = MO_df.rename(columns={'Adj. Close': 'MO'})

IBM_df = quandl.get("WIKI/IBM.11", start_date="2006-11-01", transform = "rdiff")
IBM_df = IBM_df.rename(columns={'Adj. Close': 'IBM'})

ORCL_df = quandl.get("WIKI/ORCL.11", start_date="2006-11-01", transform = "rdiff")
ORCL_df = ORCL_df.rename(columns={'Adj. Close': 'ORCL'})

AMGN_df = quandl.get("WIKI/AMGN.11", start_date="2006-11-01", transform = "rdiff")
AMGN_df = AMGN_df.rename(columns={'Adj. Close': 'AMGN'})

MMM_df = quandl.get("WIKI/MMM.11", start_date="2006-11-01", transform = "rdiff")
MMM_df = MMM_df.rename(columns={'Adj. Close': 'MMM'})

MCD_df = quandl.get("WIKI/MCD.11", start_date="2006-11-01", transform = "rdiff")
MCD_df = MCD_df.rename(columns={'Adj. Close': 'MCD'})

WMT_df = quandl.get("WIKI/WMT.11", start_date="2006-11-01", transform = "rdiff")
WMT_df = WMT_df.rename(columns={'Adj. Close': 'WMT'})

MDT_df = quandl.get("WIKI/MDT.11", start_date="2006-11-01", transform = "rdiff")
MDT_df = MDT_df.rename(columns={'Adj. Close': 'MDT'})

MA_df = quandl.get("WIKI/MA.11", start_date="2006-11-01", transform = "rdiff")
MA_df = MA_df.rename(columns={'Adj. Close': 'MA'})

BA_df = quandl.get("WIKI/BA.11", start_date="2006-11-01", transform = "rdiff")
BA_df = BA_df.rename(columns={'Adj. Close': 'BA'})

TXN_df = quandl.get("WIKI/TXN.11", start_date="2006-11-01", transform = "rdiff")
TXN_df = TXN_df.rename(columns={'Adj. Close': 'TXN'})

SLB_df = quandl.get("WIKI/SLB.11", start_date="2006-11-01", transform = "rdiff")
SLB_df = SLB_df.rename(columns={'Adj. Close': 'SLB'})

HON_df = quandl.get("WIKI/HON.11", start_date="2006-11-01", transform = "rdiff")
HON_df = HON_df.rename(columns={'Adj. Close': 'HON'})

CELG_df = quandl.get("WIKI/CELG.11", start_date="2006-11-01", transform = "rdiff")
CELG_df = CELG_df.rename(columns={'Adj. Close': 'CELG'})

BMY_df = quandl.get("WIKI/BMY.11", start_date="2006-11-01", transform = "rdiff")
BMY_df = BMY_df.rename(columns={'Adj. Close': 'BMY'})

UNP_df = quandl.get("WIKI/UNP.11", start_date="2006-11-01", transform = "rdiff")
UNP_df = UNP_df.rename(columns={'Adj. Close': 'UNP'})

AGN_df = quandl.get("WIKI/AGN.11", start_date="2006-11-01", transform = "rdiff")
AGN_df = AGN_df.rename(columns={'Adj. Close': 'AGN'})

SBUX_df = quandl.get("WIKI/SBUX.11", start_date="2006-11-01", transform = "rdiff")
SBUX_df = SBUX_df.rename(columns={'Adj. Close': 'SBUX'})

PCLN_df = quandl.get("WIKI/PCLN.11", start_date="2006-11-01", transform = "rdiff")
PCLN_df = PCLN_df.rename(columns={'Adj. Close': 'PCLN'})

GILD_df = quandl.get("WIKI/GILD.11", start_date="2006-11-01", transform = "rdiff")
GILD_df = GILD_df.rename(columns={'Adj. Close': 'GILD'})

UTX_df = quandl.get("WIKI/UTX.11", start_date="2006-11-01", transform = "rdiff")
UTX_df = UTX_df.rename(columns={'Adj. Close': 'UTX'})

df = AAPL_df.join(MSFT_df).join(AMZN_df).join(CVS_df).join(XOM_df).join(JNJ_df).join(JPM_df).join(GOOGL_df).join(GE_df).join(WFC_df).join(T_df).join(BAC_df).join(PG_df).join(CVX_df).join(PFE_df).join(VZ_df).join(HD_df).join(CMCSA_df).join(GS_df).join(INTC_df).join(MRK_df).join(USB_df).join(DIS_df).join(UNH_df).join(CSCO_df).join(C_df).join(KO_df).join(PEP_df).join(MO_df).join(IBM_df).join(ORCL_df).join(AMGN_df).join(MMM_df).join(MCD_df).join(WMT_df).join(MDT_df).join(MA_df).join(BA_df).join(TXN_df).join(SLB_df).join(HON_df).join(CELG_df).join(BMY_df).join(UNP_df).join(AGN_df).join(SBUX_df).join(PCLN_df).join(GILD_df).join(UTX_df)
#print(df)
writer = pd.ExcelWriter('S&P 500 Data_Percent.xlsx', engine = 'xlsxwriter')

df.to_excel(writer, sheet_name = 'Sheet1')
writer.save()

