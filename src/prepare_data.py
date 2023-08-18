import pandas as pd
import numpy as np

def clean_data(df):

    
    df['date']=pd.to_datetime(df['date'])
    # string_columns = df.apply(lambda x: x.tolist() if x.dtype == 'object' else None)

    # for c in string_columns:
    #     df[c]=df[c].lower()

    return df

def debit_credit_flag(df):

    df['transaction_type'] = np.where(df['transaction_amount'] > 0, 'income', 'expense')
    df = df.loc[df.transaction_type=='expense']

    return df

def get_category(col):

    if 'MCDONALDS' in col:
        return 'eat out'
    elif 'ROYAL COPENHAGEN' in col:
        return 'eat out'
    elif 'MEMET ARSLAN MANLY' in col:
        return 'eat out'
    elif 'BURGERS' in col:
        return 'eat out'
    elif 'CRUST' in col:
        return 'eat out'
    elif 'PEPPER' in col:
        return 'eat out'
    elif 'KFC' in col:
        return 'eat out'
    elif 'GRILLD' in col:
        return 'eat out'
    
    elif 'ACUPUNCTURE MASSAG' in col:
        return 'health & welbeing'
    elif 'healthSave Chemist Erina AU' in col:
        return 'health & welbeing'


    elif 'TRANSPORTFORNSW OPAL' in col:
        return 'transport'
    elif 'WILSON PARKING' in col:
        return 'transport'


    elif 'COLES' in col:
        return 'grocery'
    elif 'Namaste Australian' in col:
        return 'grocery'
    elif 'MAYALU' in col:
        return 'grocery'
    elif 'Canva' in col:
        return 'aamas recipes'
    elif 'CRAZY BARGAIN' in col:
        return 'grocery'
    elif 'WOOLWORTHS' in col:
        return 'grocery'
    


    elif 'OFFICEWORKS' in col:
        return 'stationary'
    elif 'DAN' in col:
        return 'beverage'
    
    elif 'HEALTH SERVICES UNION' in col:
        return 'professional membership - kb'
    

    elif 'SERVICE NSW' in col:
        return 'Vehicle'
    elif 'BINGLE' in col:
        return 'Vehicle'
    elif 'QBE Insurance' in col:
        return 'Vehicle'
    elif 'ULTRA' in col:
        return 'vehicle'
    elif '7-ELEVEN' in col:
        return 'fuel'
    elif 'AMPOL' in col:
        return 'fuel'
    elif 'MOBIL' in col:
        return 'fuel'


    elif 'HOLLARD INSURANCE' in col:
        return 'property insurance'

    elif 'COMMONWEALTH INSURANCE' in col:
        return 'insurance'
    elif 'BT LIFE' in col:
        return 'life insurance'
    elif 'AIA' in col:
        return 'life insurance'
    elif 'MEDIBANK' in col:
        return 'health insurance'
    
    
    
    
    elif 'Netflix' in col:
        return 'streaming service'
    elif 'NETFLIX' in col:
        return 'streaming service'


    elif 'CHEMIST' in col:
        return 'chemist'

    elif 'Electrics' in col:
        return 'electronics'
    elif 'KINCUMBER SAND' in col:
        return 'gardening'
    
    elif 'Redhill' in col:
        return 'holidays'
    elif 'PARK VIEW' in col:
        return 'holidays'
    
    elif 'myCheck' in col:
        return 'health & welbeing'
   
    elif 'MYER' in col:
        return 'clothing'
    elif 'EXETEL' in col:
        return 'internet'
    elif 'WILLIAMS THE SHOEMEN' in col:
        return 'clothing'
    elif 'BUNNINGS' in col:
        return 'gardening'
    elif 'PLASDENE' in col:
        return 'aamas recipes'
    elif 'HFM' in col:
        return 'grocery'
    elif 'CONNOR' in col:
        return 'clothing'
    
    elif 'MUNCHMONITOR' in col:
        return 'grocery'
    elif 'KATHMANDU EXPRESS' in col:
        return 'grocery'
    elif 'AMAZON' in col:
        return 'grocery'
    elif 'ETOLL' in col:
        return 'vehicle'
    elif 'INTNL TRANSACTION FEE' in col:
        return 'nepal expense'
    elif 'BIG W' in col:
        return 'clothing'
    elif 'CROWN INDIAN' in col:
        return 'eat out'
    elif 'CATCH' in col:
        return 'grocery'
    elif 'INDIAN NEPALES' in col:
        return 'grocery'
    elif 'CROWN INDIAN' in col:
        return 'eat out'
    elif 'SUSHI' in col:
        return 'eat out'
    elif 'PHOENIX PACKAGING' in col:
        return 'aamas recipes'
    elif 'IWOOHOO' in col:
        return 'aamas recipes'
    elif 'APPLE.COM' in col:
        return 'electronics'
    elif '92 CHILLI' in col:
        return 'eat out'
    elif 'Menulog' in col:
        return 'eat out'
    elif 'RIVERS' in col:
        return 'clothing'
    elif 'FAIRLIGHT' in col:
        return 'eat out'
    elif 'LIQUORLAND' in col:
        return 'beverage'
    elif 'Domino' in col:
        return 'eat out'
    elif 'KARIONG CHINESE' in col:
        return 'eat out'
    elif 'ChemistOutletErinaCen' in col:
        return 'health & welbeing'
    elif 'ACCOM BUSINESS HOLDING' in col:
        return 'holidays'
    elif 'AGA ROADASSIST' in col:
        return 'holidays'
    elif 'AGA ROADASSIST' in col:
        return 'aask smsf'
    elif '3P VENTURES' in col:
        return 'aamas recipes'
    elif 'HOME AND BEYOND' in col:
        return 'grocery'
    elif 'GET PACKED' in col:
        return 'aamas recipes'
    elif 'FOOD SAFETY' in col:
        return 'aamas recipes'
    elif 'FAST PRINTING' in col:
        return 'aamas recipes'
    elif 'COURIERS PLEASE' in col:
        return 'aamas recipes'
    elif 'COASTAL DENTAL' in col:
        return 'health & welbeing'
    elif 'COASTAL AIR' in col:
        return 'langford dr maintenance'
    elif 'BARCODESAUSTRALIA.COM' in col:
        return 'aamas recipes'
    elif 'AGL SALES 0308' in col:
        return 'AGL - Electricity'
    elif 'AGL RETAIL ENERGY' in col:
        return 'AGL - GAS'
    elif 'Aarnav' in col:
        return 'aarnav pocket money'
    elif 'Aarav' in col:
        return 'aarav pocket money'
    elif 'Loan Repayment LN REPAY 565288515' in col:
        return 'langford dr - variable'
    elif 'Loan Repayment LN REPAY 565288523' in col:
        return 'langford dr - fixed'
    elif 'Loan Repayment LN REPAY 467079445' in col:
        return 'faunce st - variable 1'
    elif 'Loan Repayment LN REPAY 784415158' in col:
        return 'faunce st - variable 2'
    elif 'Loan Repayment LN REPAY 466013145' in col:
        return 'faunce st - fixed'
    elif 'Loan Repayment LN REPAY 566498311' in col:
        return 'trevor st - fixed'
    elif 'C.C.A.S. NetBank BPAY 94482' in col:
        return 'kids education'
    elif 'Transfer to xx9452 CommBank app Credit card' in col:
        return 'credit card payments'
    elif 'Transfer to xx9452 NetBank Credit card' in col:
        return 'credit card payments'
    elif 'TAX OFFICE PAYMENTS' in col:
        return 'ato payments'
    else:
        return np.NaN

def prepare(datasets):
    
    credit_dataset = datasets["credit_dataset"]
    saving_dataset = datasets["saving_dataset"]
    df = pd.concat([credit_dataset, saving_dataset])
    
    df = clean_data(df)
    df = debit_credit_flag(df)
    df['expense_category'] = df['merchant'].apply(get_category)

    return df