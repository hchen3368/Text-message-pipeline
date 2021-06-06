import sys
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sqlalchemy import create_engine

def extract_data():
    """
    Function to read data from sys.argv

    Output:
    messages - pd.dataframe (data read from the file path given by sys.argv[1])
    categories - pd.dataframe (data read from the file path given by sys.argv[2])
    database_path - str (file path for database to save transformed data to,
    read from the file path given by sys.argv[3], default = 'Disaster_Response.db')
    table_name - str (table name to save transformed data under,
    read from the file path given by sys.argv[4], default = 'labelled_messages')
    """
    # Extract data
    messages = pd.read_csv(sys.argv[1])
    categories = pd.read_csv(sys.argv[2])

    # check if the numbers of rows in both dataframes are the same
    if messages.shape[0]!=categories.shape[0]:
        print('Warning: the numbers of rows in the two input datasets are different.')

    # read database name, default = 'Disaster_Response.db'
    if len(sys.argv)>3:
        database_path = sys.argv[3]
    else:
        database_path = 'Disaster_Response.db'

    # read table name, default = 'labelled_messages'
    if len(sys.argv)>4:
        table_name = sys.argv[4]
    else:
        table_name = 'labelled_messages'

    return messages, categories, database_path, table_name



def transform_data(messages, categories):
    """
    Transform the text data into a dataframe with category encoding

    Input:

    message - pd.DataFrame: contains 4 columns 'id', 'message', 'source', 'genre'.

    categories - pd.DataFrame: contains 2 columns 'id', 'categories', where each value in the 'categories' columns
    is string indicating the categories that the message belongs to, example: 'related-1;request-0;offer-0;....'

    Output:

    return a dataframe merging the two input dataframes and dummy encoded the message categories.

    """

    #df = messages.join(categories.set_index('id'), on='id').drop('id', axis=1)

    # read off the names of all categories, store in a list 'columns'
    text = categories.iloc[0].categories
    columns = [x[:-2] for x in text.split(';')]

    # extract all category labels into a dataframe df_labels

    # 2 auxilary functions to process the 'categories' columns in categories
    split = lambda x: x.split(';')
    extract_label = lambda lst: [int(y[-1]) for y in lst]

    # read off the labels
    labels = categories[['categories']].applymap(split).applymap(extract_label).values

    # transform into a list of lists
    labels = list(map(lambda x: list(x[0]), labels))

    # transform into a dataframe
    df_labels = pd.DataFrame(labels, columns=columns)

    # concatenate with the messages dataframe
    df = pd.concat([messages, df_labels], axis=1)

    df = df.drop_duplicates()

    return df



def load_data(df, database_path, table_name):
    # Load data.
    engine = create_engine('sqlite:///'+database_path)

    df.to_sql(table_name, engine, index=False, if_exists='replace')
    print(f'Successfully loaded data, saved in sqlite database "{database_path}" as table "{table_name}".')



def main():
    """
    Main function for process_messages.py.
    Implement ETL process for the input data.
    """

    # Extract data
    try:
        messages, categories, database_path, table_name = extract_data()
        print('Successfully extracted data.')
    except:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument (default: "Disaster_Response.db"), and the table name to save the transformed data'\
               ' as the fourth argument (default: "labelled_messages") \n\nExample: python3 etl_pipeline.py '\
              'messages.csv categories.csv '\
              'Disaster_Response.db ')
        return None


    # Transform data.
    df = transform_data(messages, categories)
    print('Successfully transformed data.')

    # Load data.
    load_data(df, database_path, table_name)



if __name__ == "__main__":
    main()
