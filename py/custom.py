def for_launches_df(df):
    a = []
    b = []
    c = ""
    d = []
    for i in df['rocket']:
        a.append(i['rocket']['id'])
    for i in df['ships']:
        if i:
            b.append(i[0]['id'])
        else:
            b.append(c)
    for i in df['mission_id']:
        if i:
            d.append(i[0])
        else:
            d.append(c)
    df['rocket_id']=a
    df['mis_id']=d
    df['ships_id']=b
    df.drop(columns=['mission_id'], axis = 1, inplace=True)
    df.drop(columns=['rocket'], axis = 1, inplace=True)
    df.drop(columns=['ships'], axis = 1, inplace=True)
    return df
    
def for_links_df(df):
    z=""
    a = []
    b = []
    c = []
    d = []  
    e = []
    f = []
    g = []
    for i in df['links']:
        if i : 
            a.append(i['article_link']) 
        else : 
            a.append(z)
        if i : 
            b.append(i['mission_patch']) 
        else : 
            b.append(z)
        if i : 
            c.append(i['reddit_campaign']) 
        else : 
            c.append(z)
        if i : 
            d.append(i['reddit_launch']) 
        else : 
            d.append(z)
        if i : 
            e.append(i['reddit_media']) 
        else : 
            e.append(z)
        if i : 
            f.append(i['reddit_recovery']) 
        else : 
            f.append(z)
        if i : 
            g.append(i['wikipedia']) 
        else : 
            g.append(z)
    df['link']=a
    df['mis_pat']=b
    df['red_camp']=c
    df['red_laun']=d
    df['red_med']=e   
    df['red_rec']=f
    df['wiki'] = g
    df.drop(columns=['links'], axis = 1, inplace=True)
    return df


def for_histories_df(df):
    #links
    z=""
    a = []
    b = []
    c = []
    for i in df['links']:
        if i : 
            a.append(i['article']) 
        else : 
            a.append(z)
        if i : 
            b.append(i['reddit']) 
        else : 
            b.append(z)
        if i : 
            c.append(i['wikipedia']) 
        else : 
            c.append(z)
    df['article']=a
    df['reddit']=b
    df['wikipedia']=c
    df.drop(columns=['links'], axis = 1, inplace=True)
    a = []
    for i in df['flight']:
        if i : 
            a.append(i['id']) 
        else : 
            a.append(z)
    df['flight_id'] = a
    df.drop(columns=['flight'], axis = 1, inplace=True)
    return(df)


