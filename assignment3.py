import pandas as pd
data = {
    'Refund' : ['yes','no','no','yes','no','no','yes','no','no','no',],
    'Marital Status' : ['single','married','single','married','divorced','married','divorced','single','married','single'],
    'Texable Income' : [125,100,70,120,95,60,220,85,75,90],
    'Cheat' : ['no','no','no','no','yes','no','no','yes','no','yes']
}
df=pd.DataFrame(data)
print(df)