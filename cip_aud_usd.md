# AUD/USD Covered Interest Parity (CIP) Model  
*Finance Models Portfolio — Interest Parity & FX Pricing*

## Overview  
This project tests whether AUD/USD exchange-rate movements follow the Covered Interest Parity (CIP) condition. Using 10 years of monthly data from FRED, OECD, and Yahoo Finance, I compared the CIP-implied forward rate with the actual forward market price. The goal was to see where theoretical parity holds and where liquidity frictions or basis spreads appear.

## What I Did  
- Collected AUD/USD spot, forward rates, and 3-month US/AU interest rates.  
- Resampled all series to monthly frequency.  
- Calculated the CIP-implied forward rate using interest-rate differentials.  
- Compared deviations between theory and market.  
- Interpreted basis spread behaviour across regimes.

## How I Did It  
Data was pulled using `pandas_datareader`, cleaned in Python, and merged into a single time series.  
The CIP identity was applied:


Residuals between actual and theoretical forwards were plotted and analysed.

## Why It Matters  
CIP is a cornerstone of FX pricing. Persistent deviations reveal funding pressure, market segmentation, and risk premia. This project demonstrates practical interest-parity testing used in global macro and FX strategy teams.

---

## Figures  
![Figure 1: AUD/USD vs CIP-Implied Forward](figures/PRED VS ACTUAL.png)  
![Figure 2: Residuals Over Time](figures/rEGRESSION Reisduals.png)

---

## Code Reference  
See full code in the Finance Models repository:  
`/finance-models/cip_aud_usd.ipynb`
---
layout: default
title: AUD/USD CIP Model
---
