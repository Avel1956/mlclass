
def split_sample(df, vect_text):
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(vect_text, df.Apropiado, 
                                                    test_size=0.5, random_state=3)
    return(X_train, X_test, y_train, y_test)