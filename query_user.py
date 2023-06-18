import pandas as pd


def get_row(user_id):
    """
    Given the user's ID, return the rest of their info from the .csv
    :param user_id: user ID
    :return: row of pandas dataframe as list
    """
    path = "users_hackathon.csv"
    df = pd.read_csv(path)
    row = df.loc[df["UserNum"] == user_id]
    row_list = row.values.tolist()[0]
    return row_list


def return_info(user_id):
    """
    Turns df row into assorted info
    :param user_id: user ID
    :return: a tuple of all the user info
    """
    row = get_row(user_id)
    return (*row[1:],)


