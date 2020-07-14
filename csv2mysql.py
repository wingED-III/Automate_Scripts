import pandas as pd
from sqlalchemy import create_engine
from getpass import getpass


def main():
    df = pd.read_csv('myResource/building_location_edit.csv')
    df.drop(columns=['zone'],inplace=True)
    df.rename(columns={'number':'locationID','latitude':'lat','longtitude':'lon'},inplace = True)
    df['id'] = range(1,1+len(df))
    df = df[['id','locationID','lon','lat']]
    #df = df[df['locationID'] != 1]
    #create_engine('mysql://user:pass@127.0.0.1/database')
    print(df.columns)
    print(df.shape)
    print(df.head(20))
    user = input('user:')
    pwd = getpass('password:')
    serverAndDB = input('enter in format "server_address/database_name" :')

    arg = 'mysql+mysqlconnector://'+user+':'+pwd+'@'+serverAndDB
    mysqlEngine = create_engine(arg)

    tableName= input('table name:')
    df.to_sql(tableName,mysqlEngine,if_exists='replace',index=False)  # if_exists : fail,append,replace # defaul = fail




if __name__ == "__main__":
    main()

